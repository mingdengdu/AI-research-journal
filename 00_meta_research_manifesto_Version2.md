# Research Manifesto / 研究宣言

作者: mingdengdu  
目的: 以可复现、可检验、快速迭代的方式推进模型/系统研究

核心价值
- 可证伪（Falsifiability）: 每个假设都需明确成功/失败的量化准则。
- 可复现（Reproducibility）: 实验脚本、随机种子、依赖与数据分割应与结果一并保存。
- 记录驱动（Record-driven）: 实验日志（log.md）记录关键决策、时间点与直觉，失败存档到 99_failures。
- 小步快跑（Small, frequent experiments）: 偏好短周期的可测改动与自动化 CI。
- 可分享（Shareable）: README.md 作为“实验室主页”，指引外部复现流程。

仓库约定（建议）
- 每个实验一个目录: YYYY-MM-DD_shortname/
  - hypothesis.md, protocol.py, data/results.json, log.md
- metadata front-matter: title, date, author, status, tags, reproducible, seed
- failures/ 下每个失败案例包含 postmortem（背景、过程、根因、教训、复现脚本）
- CI: 在 push/PR 时能运行 protocol.py（或部分 smoke tests）并上传结果 artifacts

如何贡献
- 新实验请 fork -> branch -> 提交 PR，PR 描述需包含 hypothesis.md 的关键字段与主要补丁说明
- 重大更改应在 weekly_review.md 中记录并通过简短审阅（owner 或指定 reviewer）