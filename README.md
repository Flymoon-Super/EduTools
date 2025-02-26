# EduTools

EduTools 是一个基于 Python 的教育工具集合，旨在帮助教师、学生和家长更高效地完成学习和教学任务。目前包含以下功能：

1. **数学题生成器**：快速生成多种类型的数学题目（如加减乘除、代数、几何等），支持自定义难度和题目数量。
2. **作文批改工具**：通过自然语言处理技术，对作文进行语法检查、词汇评分和内容建议，帮助学生提升写作能力。

## 功能特点
- **简单易用**：通过命令行或图形界面快速上手。
- **高度可定制**：支持用户自定义题目类型、难度和批改规则。
- **开源免费**：代码完全开源，欢迎贡献和改进。

## 安装方法
```bash
pip install -r requirements.txt
```

## 使用方法
### 数学题生成器
```bash
python -m edutools.gui.math_quiz_app
```

### 作文批改工具
```bash
python -m edutools.gui.essay_analyzer_app
```

## 适用场景
- 教师：快速生成练习题或批改作业。
- 学生：自我练习和提升写作能力。
- 家长：辅助孩子学习。

## 项目结构
```
edutools/
├── core/          # 核心功能模块
│   ├── math/      # 数学题生成相关
│   └── essay/     # 作文分析相关
└── gui/           # 图形界面应用
```

## 贡献指南
欢迎提交 Issue 或 Pull Request，共同完善项目！请参考 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证
本项目采用 [Apache License 2.0](LICENSE) 开源许可证。
