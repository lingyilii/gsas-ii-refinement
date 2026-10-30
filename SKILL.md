---
name: gsas-ii-refinement
description: GSAS-II powder diffraction and Rietveld refinement in Chinese or English, with tutorial-backed calibration, integration, validation and batch processing. 用 GSAS-II 进行粉末衍射校准、积分、分阶段精修及可追溯交付，支持教学、执行、续作和批量；主要用于恒波长 X 射线，其他实验类型须匹配专用教程。
---

# GSAS-II 精修skill

**中文** | [English](SKILL.en.md)

**Language routing:** For English requests, read [SKILL.en.md](SKILL.en.md) and its English references instead of the Chinese workflow below. Follow the user's selected language; both versions describe the same skill and scientific rules. Do not install them as separate skills.

以用户指定的数据和结构模型为输入，完成有依据、可复查的精修。默认中文沟通。本技能提供方法和判据，不携带任何用户的实验数据、标准卡片或历史精修参数，也不保证所有数据都能得到唯一结构解。

## 开始一个新对话

1. 识别用户要**教学、代执行、续作还是批量**。明确要求教学时每次只给一小步，说明位置、目的、教程来源和判断方法，等待用户 `done` 或截图；不要代替用户点击。代执行模式完成授权范围内的工作，不逐步重复索要许可。
2. 先读取用户指定目录和已有运行记录，确认输入身份；不要凭文件名相似度选择其他目录的旧项目。如果缺少数据目录或文件，询问这一项。不要要求用户重新提供已经能从附件或目录读取的信息。
3. 读取 [教程索引](references/tutorial-map.md) 和 [输入与校准](references/input-and-calibration.md)。列出实际输入、实验类型、可用校准证据、缺失信息、计划输出位置。缺失的科学参数记为未知，不能用教程数值补齐。
4. 新任务从原始输入新建项目；续作先核对来源和最后通过检查的检查点。文件哈希、版本、路径和参数来源保存在本次任务目录，不回写到技能目录。
5. 使用已安装的 GSAS-II 及其匹配 Python 环境。执行前检查版本和实际可用 API；教程的旧菜单名称可能变化。用户要求另开窗口时打开独立项目副本，不覆盖正在工作的项目。

## 按需读取

| 当前工作 | 必读资料 |
|---|---|
| 输入识别、二维探测器、波长、积分 | [input-and-calibration.md](references/input-and-calibration.md)，教程 T01–T05 |
| 单峰检查、仪器峰形、结构精修、失败诊断 | [refinement.md](references/refinement.md)，教程 T05–T09 |
| 脚本执行、批量、验收、导出、续作 | [execution-and-delivery.md](references/execution-and-delivery.md)，教程 T07、T09、D01 |

打开对应官方教程核实将要采用的方法。离线时可以依据随附摘要做不依赖未知细节的工作，但标记“原文未重新核验”；不要编造菜单、API 或引文。教程示例只证明方法，不证明其参数适合当前数据。没有匹配教程的扩展必须明确说明依据缺口，不宣称“教程要求”。

## 工作主线

按数据条件选取这些阶段；不是每个任务都需要全选：

`S00 输入和来源 → S01 图像几何/波长校准 → S02 掩膜与积分 → S03 仪器峰形 → S04 结构与数据关联 → S05 背景及尺度 → S06 峰位 → S07 峰宽 → S08 结构参数 → S09 综合检查 → S10 交付/批量`

各阶段的操作、解释、教程对应点和通过条件见参考文件。逐阶段保存、检查后再扩大变量集合。

## 必须保持的科学边界

- **波长不是默认精修项。** 有可信波长时固定；未知波长需要适当的标准与几何约束。不能用未知样品同时自由精修波长和晶胞绝对尺度来证明两者准确。
- **Peak List 单峰拟合不是 Rietveld 精修。** 它可用于峰形诊断或标准样品仪器参数建立，不需要结构模型；结构精修必须有正确的 phase–histogram 关联。
- **样品峰宽不等于纯仪器峰宽。** 仪器文件的适用配置和来源必须明确；不具备可靠分离条件时，只报告有效峰形，不把尺寸和应变当成独立可信测量。
- **整体尺度和所有相尺度不能无约束地一起自由变化。** 按 T09 建立适当约束或减少独立尺度自由度；相尺度、质量分数、原子占位率是不同量。
- **Rwp 降低不自动表示有效。** 丢参数、假极小值、未收敛、非物理参数或明显遗漏峰都要检查。按 [验收规则](references/execution-and-delivery.md) 降级结果，保留最后有效检查点。
- **二维数据最终 GPX 必须保留 IMG、PWDR、Phases。** 它们是项目树中的数据类别；原始图像常为外部文件，必须核对引用能打开。仅有一维数据时不伪造 IMG，说明完整三类交付尚缺原图。
- 不把前一任务的样品名、CIF、波长、距离、积分区间、相比例、约束或精修结果写入本技能作为默认值。

## 沟通与交付

每次解释按“当前证据 → 改什么 → 为什么 → 教程对应点 → 如何判定”表达。截图只支持可见结论；看不到的状态要查项目或日志。Refine 勾选框仅表示当前设置，不能单凭它断言某参数从未精修过。

执行任务交付项目、数据、图、参数、日志和中文报告，具体文件契约见 [execution-and-delivery.md](references/execution-and-delivery.md)。先重新打开最终 GPX 验证，再展示结果。固定值不冒充精修值，不确定度缺失写 `null` 并说明。

批量任务先验证代表性样品和校准分组，再扩展。失败项隔离，不能将其参数继续传给下一个样品。

可用 `scripts/input_manifest.py` 对明确选定的输入生成 SHA-256 来源清单；它不识别物相、不校准、也不精修。输出可能含私人路径，只放任务目录。运行记录模板在 [assets/run-state.template.json](assets/run-state.template.json)，由执行者填充，不要求用户手填。
