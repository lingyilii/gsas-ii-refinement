# 执行、批量与输出契约

**中文** | [English](en/execution-and-delivery.md)

两种语言共用记录结构，英文报告使用 `report_en.md`，中文使用 `report_zh.md`。续作时读取已有语言的报告；切换语言不重置科学状态。

## 脚本与 GUI 协同

**教程对应：** [T07](tutorial-map.md) A / Create a Multi-step Script、B / Single-Step Refinement；[D01 官方 API](https://gsas-ii.readthedocs.io/en/latest/GSASIIscriptable.html)。

自动执行优先使用 GSASIIscriptable；GUI 用于校准点、掩膜、可视检查和最终展示。执行环境没有某种能力时如实说明，不能把写好脚本等同于已经运行，也不能把无图检查当目视验收。

1. 找到现有 GSAS-II 安装、启动解释器和源码位置，记录版本。先做导入检查，再读项目；不要在任务中无理由更新软件。新版包式导入和旧版模块路径可能不同，核查安装版本，不能用宽泛异常捕获把依赖错误掩盖为版本差异。
2. 每个实验任务生成自己的运行脚本，使用命令行/配置传入路径。采用官方对象和方法，不直接改 GPX 二进制。涉及低层字段时查本地源码的实际结构，记录访问版本；不能猜列表索引。
3. 导入、关联、校准、积分、设置变量、拟合、读取结果、保存分别验证。使用 `G2Project`、图像积分、`add_phase`、精修控制或导出方法前核对当前 API 签名和单位；不要照抄过时教程代码后忽略错误。
4. 每阶段保留变量清单、约束、参数前后值和对应教程。拟合后检查返回状态及 `.lst`，保存前后检查点。新一阶段必须从已通过检查的状态开始。
5. 不允许 GUI 和脚本同时写同一个 GPX。另开 GUI 时用最终保存副本，确认标题路径及内容，避免把旧窗口当新结果。

## S10：独立批量与顺序精修

**教程对应：** T09 / Step I 先拟合代表数据及后续顺序精修；T07 多阶段脚本。分组、隔离失败和运行状态文件是本技能工程规则。

- **独立批量：** 每个样品独立 GPX；按波长、距离、探测器方向/binning、光路和测量条件建立校准组。先验证代表样品，复制适用方法和校准，重新核对其相组成、掩膜、背景、拟合区间和质量。
- **顺序精修：** 用户数据确为相关序列时选择。说明采用上一帧结果、各帧独立初始值，还是共同初始值。若有相变/新峰，重新评估模型，不能强制整组同相。
- **传递门槛：** 只传递通过质量门槛的参数。失败帧隔离；下一帧从该组可信起点或最近有效帧开始，并记录来源。没有可信起点则暂停该分组，不影响独立可处理组。
- **停止条件：** 同一原因两次针对性修复仍未解决时，标记 `failed`/`needs_input` 并保存证据；这是可由用户调整的工程重试限制，不是教程数值。不要为完成批量而删除告警、改权重或自动剔除难拟合数据。
- 若采用一个含多直方图的序列项目，同时为每个样品保存可独立复查的结果项目或经过验证的提取副本；二维来源的每个交付项目都要保留相应 IMG、PWDR、Phases 和正确关联。

## 状态和验收

状态不是科研结论。每项报告分别填写“数值状态”和“科学局限”，并区分：

| 状态 | 含义 |
|---|---|
| `needs_input` | 关键输入/校准依据不足，依赖该信息的步骤不能完成 |
| `provisional` | 可以计算和展示，但存在未核实校准、模型、误差或其他明确局限 |
| `failed` | 本次拟合数值失败或无法达到既定质量条件，保留最后有效状态 |
| `accepted` | 在声明的假设和范围内，通过以下检查；不表示唯一物相解或消除系统误差 |

`accepted` 至少需要：

1. 来源、单位、仪器/几何及相关联可追溯；二维积分有校准和掩膜依据。
2. 精修终止与收敛证据正常；无未解释的丢参数、奇异、假极小值、非有限统计或持续过大 shift/σ。若使用定量阈值，应在运行计划中说明版本和理由；不能把缺失字段当通过。
3. 放大图、全谱和弱峰区域无未处理的主要系统偏差；对遗漏信号明确建模、合理排除或降级，而非掩盖。
4. 晶胞、占位、ADP、相尺度、峰宽与化学结构合理；关键参数的不确定度和相关性可解释。固定值没有伪造的标准差。
5. 最终保存文件重新打开成功，数据源可访问，导出曲线与 GPX 数组一致，最终 `.lst` 对应最终拟合。

按实际软件字段报告 Rwp、Rp、Rexp（可用时）、reduced χ²、GOF、数据点数和独立变量数。明确 GOF 是否为 `sqrt(reduced χ²)`。不靠修改误差使 χ² 接近目标；不确定度的统计含义与校准系统误差分别讨论。

## 文件输出

**教程对应：** T02 Step 3 保存积分项目；T05 / Save Instrument Parameters；T06 / Refinement results 的 `.lst`；T07 的项目保存/导出示例；D01 的 Export 与数据访问。以下目录、CSV/JSON 字段和隐私规则为本技能交付约定。

```text
run/
  input_manifest.json
  run_state.json
  execution/                  # 实际执行脚本、配置、环境/版本、标准输出和错误日志
  calibration/                # 适用时：校准 GPX、图像控制、掩膜、仪器文件、依据
  samples/<sample_id>/
    final.gpx
    final.lst
    observed.fxye
    profile.csv
    phases/                   # 每个最终模型的 CIF
    figures/                  # 全谱、关键局部和二维校准/积分边界图
    summary.json
    stages.jsonl
    report_zh.md
    checkpoints/
  batch_summary.csv           # 批量时
```

对失败项不要生成名义成功的 `final.gpx`。使用 `last_valid.gpx` 或 `diagnostic.gpx` 并记录状态。已有有效成果不因失败重试被覆盖。`.lst` 必须与对应 GPX 同一次精修；保存/改名时同步核对，不能把另一阶段日志复制冒充。

| 文件 | 格式、内容和检查 |
|---|---|
| `input_manifest.json` | UTF-8 JSON：输入角色、路径、SHA-256、大小；结构/标准/校准之间的关联由执行者补充。可由随附脚本生成初始文件清单 |
| `run_state.json` | 运行状态、环境、校准组、参数依据、每样品当前阶段、最后有效检查点和下一步；参照随附模板，未知用 null |
| `final.gpx` | 原生可重新打开的 GSAS-II 项目；二维来源保留 IMG + PWDR + Phases，正式直方图和相关联清楚，图像路径有效 |
| `final.lst` | GSAS-II 最终精修日志，保留告警、变量、统计和误差；有必要同时保留终端日志 |
| `observed.fxye` | 用版本匹配的 GSAS-II exporter 输出正式实测谱及标准差；记录导出器、横轴单位和文件头约定，不手猜 FXYE 的角度缩放。可另加通用 xye；无可靠误差必须标记假设 |
| `profile.csv` | UTF-8，列至少 `x, y_obs, y_calc, y_background, y_obs_minus_calc, weight, used_in_fit`；本文件 x 单位在 summary 中声明，CW 默认实际 2θ 度。差值不带绘图位移；排除点通过布尔列标记，不偷偷删除 |
| `phases/*.cif` | GSAS-II 导出的当前结构及可用不确定度。注明固定/精修状态；多直方图/顺序数据必须核对导出的结构属于哪个结果 |
| `figures/` | 至少全谱线性图与关键局部图（PNG 或 PDF）；计数动态范围大时补充对数/平方根显示，并说明转换。显示观测、计算、背景、差值和各相反射标记；差值平移量注明 |
| `summary.json` | 状态、输入哈希、版本、方法、数据范围/排除区、波长/几何来源、仪器文件、相参数/不确定度/固定标志、统计、告警、局限、输出路径与哈希 |
| `stages.jsonl` | 每行一个阶段：时间、步骤编号、教程 URL/小节、改变变量和原因、前后统计、告警、接受/回退、检查点。允许增加字段 |
| `report_zh.md` | 结论及状态；输入与校准；各阶段理由和教程链接；统计与局部残差；结构/相含量及可辨识性；局限；文件说明与续作入口 |
| `batch_summary.csv` | 每样品一行：ID、状态、校准组、正式直方图、Rwp、reduced χ²、独立变量数、主要告警、结果路径；关键相字段按批次模型明确命名 |

只用一维输入时如实说明没有 IMG。用户要求最终三类俱全时，先查是否有原始二维文件；确实没有则标记该交付要求未满足，不伪造图像节点。

GPX 不保证嵌入原图。保持原图在受控任务目录，或在用户要求可移交数据包时复制必要原图/sidecar 并修复引用；移动后重新打开确认。绝不因为公开发布 skill 就连带公开结果包。

## 新对话续作

运行模板的数组由执行者按实际输入填充：

- `calibration_groups[]`：`id`、`input_file_ids`、`instrument_file`、`geometry`、`wavelength`、`valid_for`、`status`。每个物理量采用 `{value, unit, source, fixed, uncertainty, limitation}`；未知为 null，`source` 指向文件及字段/校准步骤。
- `samples[]`：`id`、`input_file_ids`、`calibration_group_id`、`phase_sources`、`histogram_names`、`status`、`current_stage`、`last_valid_checkpoint`、`last_valid_lst`、`last_valid_sha256`、`next_action`、`warnings`。路径相对运行根目录或注明绝对路径。
- `decisions[]`：`stage`、`sample_id`、`action`、`reason`、`tutorial_id`、`tutorial_section`、`tutorial_url`、`evidence`、`time_utc`。工程决策的 `tutorial_id` 可以为空，但必须说明它是本技能约定。
- `associations[]`（来源清单）：记录 `sample_id`、`image_file_id`、`metadata_file_id`、`structure_file_ids`、`calibration_group_id`。使用 `input_manifest.py` 生成清单后需根据内容补齐；脚本不会凭文件名自动配对。

读取 `SKILL.md → run_state.json → input_manifest.json → report_zh.md → 最后有效 GPX/LST`。核对输入哈希、版本、路径和目标，随后读取待执行阶段的参考文件。只凭项目名、聊天记忆或截图不能断言状态；若缺运行记录，从 GPX/LST 重建并标出不能恢复的历史。

## 发布隐私

技能目录只放方法、官方链接、通用代码和空模板。任务数据、CIF、图像、GPX、日志、文件哈希、路径、样品名、图表和精修数值都留在任务目录。发布使用明确文件白名单，检查压缩包清单；`.gitignore` 是辅助，不能代替检查。
