#!/usr/bin/env python3
"""生成明确指定的输入文件来源清单，不读取文件内容到日志、不执行精修。

用法（路径为用户本次任务提供的真实路径）：
  python input_manifest.py --input image PATH --input structure PATH --output OUT

不递归扫描目录；同一文件可有多个角色；输出不得已存在。
输出含文件路径与哈希，应保存在私人任务目录，不提交到技能仓库。
"""

import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path


ROLES = (
    "image", "metadata", "powder", "structure", "calibrant_image",
    "calibrant_reference", "instrument", "calibration", "mask",
    "dark", "flat", "background", "project", "log", "other",
)


def fingerprint(path, language="zh"):
    """散列期间检测常见的文件修改；发现变化则拒绝出具稳定清单。"""
    sha = hashlib.sha256()
    with path.open("rb") as stream:
        before = os.fstat(stream.fileno())
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            sha.update(block)
        after = os.fstat(stream.fileno())
    current = path.stat()
    stamp = lambda s: (s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns)
    if stamp(before) != stamp(after) or stamp(after) != stamp(current):
        message = "File changed during hashing; stop writes and retry" if language == "en" else "文件在生成清单期间发生变化，请停止写入后重试"
        raise ValueError(f"{message}: {path}")
    return {"bytes": after.st_size, "sha256": sha.hexdigest()}


def make_manifest(entries, language="zh"):
    files = []
    by_path = {}
    for role, raw_path in entries:
        if role not in ROLES:
            message = "Unknown input role; available roles" if language == "en" else "未知输入角色；可用角色"
            raise ValueError(f"{message}: {role!r}; {', '.join(ROLES)}")
        path = Path(raw_path).expanduser().resolve(strict=True)
        if not path.is_file():
            message = "Specify a file, not a directory" if language == "en" else "必须明确指定文件，不能传入目录"
            raise ValueError(f"{message}: {path}")
        key = os.path.normcase(str(path))
        if key in by_path:
            record = by_path[key]
            if role not in record["roles"]:
                record["roles"].append(role)
            continue
        record = {
            "file_id": f"input-{len(files) + 1:04d}",
            "path": str(path),
            "roles": [role],
            **fingerprint(path, language),
        }
        by_path[key] = record
        files.append(record)
    return {
        "schema_version": 1,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "purpose": ("Input identity verification; hashes do not validate data quality, standard identity or structures."
                    if language == "en" else "输入身份核对；哈希不证明数据质量、标准身份或结构正确。"),
        "files": files,
        "associations": [],
    }


def main():
    parser = argparse.ArgumentParser(description="Generate an input-file SHA-256 manifest / 生成输入文件来源清单. Outputs may contain private paths; keep them outside the skill repository.")
    parser.add_argument("--input", nargs=2, metavar=("ROLE", "PATH"),
                        action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--language", choices=("zh", "en"), default="zh",
                        help="Language of messages and manifest description (default: zh)")
    args = parser.parse_args()
    try:
        output = args.output.expanduser().resolve()
        if output.exists():
            message = "Output exists; refusing to overwrite" if args.language == "en" else "输出已存在，不覆盖"
            raise ValueError(f"{message}: {output}")
        manifest = make_manifest(args.input, args.language)
        # 对所有输入成功完成检查后才写出结果；x 模式防止竞争造成覆盖。
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("x", encoding="utf-8", newline="\n") as stream:
            json.dump(manifest, stream, ensure_ascii=False, indent=2, allow_nan=False)
            stream.write("\n")
    except (OSError, ValueError) as error:
        message = "No usable manifest generated" if args.language == "en" else "未生成可用清单"
        parser.exit(2, f"{message}: {error}\n")
    if args.language == "en":
        print(f"Recorded {len(manifest['files'])} input files: {output}")
    else:
        print(f"已记录 {len(manifest['files'])} 个输入文件：{output}")


if __name__ == "__main__":
    main()
