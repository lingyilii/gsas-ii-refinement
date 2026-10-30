# 官方教程与步骤对应

核验日期：2026-10-30。以下是 GSAS-II 官方教程或官方 API 文档；本技能为独立整理，非官方发布。链接中的示例材料和数值均不是用户数据的默认值。

**引用方式：** 工作记录使用 `步骤编号 + 教程编号 + 小节标题 + URL + 本次选择理由`。网页改版后按小节标题搜索，不靠截图坐标或固定行号。教程没讲到的本技能规则明确列为“工程/质量规则”，不能伪装成教程原文。

| 编号 | 官方来源 | 对应点及适用边界 |
|---|---|---|
| T00 | [Tutorials 索引](https://advancedphotonsource.github.io/GSAS-II-tutorials/tutorials.html) | 为不同实验类型寻找专门流程；恒波长、TOF、中子、织构等不互相直接套用。 |
| T01 | [Area detector calibration](https://advancedphotonsource.github.io/GSAS-II-tutorials/2DCalibration/Calibration%20of%20an%20area%20detector%20in%20GSAS.htm) | S00–S01：Step 1 读图、Step 2 图像参数、Step 3 校准；需区分已知实验量和待标定几何量。 |
| T02 | [Area detector integration](https://advancedphotonsource.github.io/GSAS-II-tutorials/2DIntegration/Integration%20of%20area%20detector%20data%20in%20GSAS.htm) | S02：Prerequisite、Step 2 Integration Settings、Step 3 Perform integration；区间叠加显示、角度/方位分箱、图像校正和产生 PWDR。 |
| T03 | [Multiple distances, part 2: Calibrate Detector Distances](https://advancedphotonsource.github.io/GSAS-II-tutorials/CalibrationTutorial/CalibrationTutorial.html) | S01–S02：Step 1 区分设定距离与校准距离；Step 2 Integrating the Calibrated Data，包括遮挡处理和掩膜。 |
| T04 | [Multiple distances, part 1: Determine Wavelength](https://advancedphotonsource.github.io/GSAS-II-tutorials/DeterminingWavelength/DeterminingWavelength.html) | S01：Step 2 Calibrating the Wavelength: First Image；Step 3 Calibrating all Images；Step 4 Parametric Fit to Find Wavelength。必须阅读完整多距离方法，不能把首图试算当最终波长。 |
| T05 | [Determine Starting Profile from a Standard](https://advancedphotonsource.github.io/GSAS-II-tutorials/CWInstDemo/FindProfParamCW.html) | S03：Intro、Individual peak fitting、Save Instrument Parameters；标准样品建立起始仪器峰形，单峰拟合和仪器/样品展宽区别。示例为实验室仪器。 |
| T06 | [Laboratory X-ray Powder Data](https://advancedphotonsource.github.io/GSAS-II-tutorials/LabData/Laboratory%20X.htm) | S04–S09：Step 1–3 导入与结构；Step 4 背景；Step 5 首次精修；Step 6 峰位；Step 7 尺寸/应变；Step 8 原子参数与结果。示例的 Bragg–Brentano 位移模型不能直接套入透射实验。 |
| T07 | [Running a GSAS-II Refinement From a Python Script](https://advancedphotonsource.github.io/GSAS-II-tutorials/PythonScript/Scripting.htm) | S00、S05–S10：A. Create a Multi-step Script；B. Single-Step Refinement；C. Powder Pattern Simulation 中的导出和绘图示例。这里只借用 C 的输出方法，不将模拟曲线当实测数据。 |
| T08 | [Neutron CW Powder Data](https://advancedphotonsource.github.io/GSAS-II-tutorials/CWNeutron/Neutron%20CW%20Powder%20Data.htm) | S04、S08：Step 2 结构；Step 3 原子设置及其后的等价约束、占位约束操作。仅迁移约束方法，不迁移中子散射或仪器参数。 |
| T09 | [Sequential refinement of multiple datasets](https://advancedphotonsource.github.io/GSAS-II-tutorials/SeqRefine/SequentialTutorial.html) | S04–S05：Step I / Prepare for fit: define phase fraction constraint；S10：先拟合代表数据，随后顺序精修及起始参数传递方式。 |
| T10 | [Fitting the Starting Background using Fixed Points](https://advancedphotonsource.github.io/GSAS-II-tutorials/BkgFit/FitBkgTut.htm) | S05：Step 2 固定背景点、Step 3 拟合、Step 4 背景峰、Step 5 模型比较、Step 6 后续处理。背景点初始化与最终背景精修要分清。 |
| D01 | [GSASIIscriptable API](https://gsas-ii.readthedocs.io/en/latest/GSASIIscriptable.html) | S00–S10 的程序实现依据：模块加载、G2Project、图像/相/直方图、Refinement parameters、导出。以安装版本实际签名为准。 |

## 不来自教程的工程规则

输入哈希、清单格式、检查点命名、状态机、失败隔离、公开包隐私检查、最终文件目录和“必须保留三类节点”是本技能的交付约定。其相关教程支持读写项目、校准、精修、脚本或批量概念，但没有规定这些文件名或质量阈值。

教程没有给出适合一切样品的 Rwp、背景阶数、角度范围或相含量阈值。本技能也不设置这样的通用通过线。教程示例中出现的数值、异常或特定修复方式不自动成为建议。
