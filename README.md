# GSAS-II 精修skill

**中文** | [English](README.en.md)

本仓库提供完整中英文说明和流程。只需安装一份技能，在请求中指定中文或 English；两种语言共用步骤编号、教程依据和输出数据结构。英文入口为 [SKILL.en.md](SKILL.en.md)，中文入口为 [SKILL.md](SKILL.md)。切换语言不会重置已有任务状态。

中文 GSAS-II 工作流技能，面向粉末衍射的输入核查、二维图像校准与积分、Rietveld 精修、结果判断及批量交付。每个处理阶段均链接到对应的 GSAS-II 官方教程小节；工程性的来源追踪、检查点和交付规则另行标明。

这是供 AI 助手读取并执行的技能，不是内置固定参数的一键精修程序。需要可用的 GSAS-II、本地文件访问能力，以及用户提供的数据和适用结构/校准信息。

## 使用

将**整个文件夹**提供给支持技能的助手，从 [SKILL.md](SKILL.md) 开始读取；不要只复制入口文件而丢失 `references/`。

在 Codex 中可将目录安装到该版本支持的用户技能目录，然后在新对话选择此技能，或明确写出 `$gsas-ii-refinement`。未自动发现时也可以直接让助手读取本目录的 `SKILL.md`。安装路径依宿主版本而定，参见 [官方技能说明](https://learn.chatgpt.com/docs/build-skills)。

新对话示例：

> 使用 $gsas-ii-refinement。数据位于我指定的目录，请先核对输入、候选结构和校准依据，然后完成精修。二维数据的最终项目保留 IMG、PWDR、Phases，输出中文报告和可复查文件。

教学模式示例：

> 使用 $gsas-ii-refinement，一次教我一小步。我操作后回复 done；每步说明教程出处、操作原因和判断标准。

批量/续作示例：

> 使用 $gsas-ii-refinement，读取我提供的运行目录中的 run_state.json，先验证有效检查点，再继续未完成样品；失败项隔离并说明原因。

技能本身不记忆上一段对话的数据。新任务需要提供数据位置；续作提供运行目录，助手即可通过来源清单和检查点恢复状态。

## 输入与输出

输入可以是二维图像及元数据、标准的测量数据/有效校准文件、一维粉末谱、仪器参数、CIF，或已有 GPX/LST。具体必需项由实验类型决定，见 [输入规范](references/input-and-calibration.md)。缺少关键依据会明确标记，不能用教程样例数值补上。

结果包含原生 GPX、最终 LST、实测谱、计算/观测曲线、结构 CIF、图、中文报告、阶段记录和批量汇总。二维来源的 GPX 保留 IMG、PWDR、Phases，并验证外部图像引用。详见 [输出契约](references/execution-and-delivery.md)。

## 目录

- [SKILL.md](SKILL.md)：技能入口与工作边界。
- [references/tutorial-map.md](references/tutorial-map.md)：官方教程对应表。
- [references/input-and-calibration.md](references/input-and-calibration.md)：输入、几何、波长、掩膜及积分。
- [references/refinement.md](references/refinement.md)：仪器峰形、结构精修、判别及回退。
- [references/execution-and-delivery.md](references/execution-and-delivery.md)：执行、批量、验收和输出格式。
- [assets/run-state.template.json](assets/run-state.template.json)：空运行状态模板。
- [scripts/input_manifest.py](scripts/input_manifest.py)：仅使用 Python 标准库，生成明确指定文件的来源清单；不是精修脚本。

## 范围与隐私

主要覆盖恒波长 X 射线粉末数据。TOF、中子、磁结构、复杂织构或特殊缺陷模型需要匹配专门教程。数值收敛不等于物相唯一或科学解释正确，不能保证任意数据都可准确精修。

公开目录不含实验数据、标准卡片、实际路径或样品专属参数。使用技能时产生的研究文件应存放在独立任务目录，不提交到技能仓库。

本项目为独立工作流整理；GSAS-II 软件与所链接教程属于其原作者。未复制教程数据或图像。
