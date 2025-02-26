# 贡献指南

感谢您对 EduTools 项目感兴趣！我们欢迎各种形式的贡献，包括但不限于：

- 报告问题（Issues）
- 提交改进建议
- 提交代码修改（Pull Requests）
- 完善文档
- 添加新功能

## 开发环境设置

1. 克隆仓库：
```bash
git clone https://github.com/Flymoon-Super/EduTools.git
cd EduTools
```

2. 创建并激活虚拟环境（推荐）：
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

## 开发流程

1. 创建新分支：
```bash
git checkout -b feature/your-feature-name
# 或
git checkout -b fix/your-fix-name
```

2. 进行代码修改，请确保：
   - 遵循 PEP 8 编码规范
   - 添加必要的注释
   - 更新相关文档
   - 添加适当的单元测试

3. 提交代码：
```bash
git add .
git commit -m "描述你的修改"
```

4. 推送到远程仓库：
```bash
git push origin feature/your-feature-name
```

5. 创建 Pull Request

## 代码风格指南

1. Python 代码风格：
   - 使用 4 个空格进行缩进
   - 行长度不超过 120 个字符
   - 使用有意义的变量和函数名
   - 添加适当的类型提示
   - 编写清晰的文档字符串

2. 注释规范：
   - 使用中文注释
   - 注释应该说明"为什么"而不是"是什么"
   - 关键算法和复杂逻辑必须添加注释

3. 提交信息规范：
   - feat: 新功能
   - fix: 修复问题
   - docs: 文档修改
   - style: 代码格式修改
   - refactor: 代码重构
   - test: 测试用例修改
   - chore: 其他修改

## 项目结构

```
edutools/
├── core/          # 核心功能模块
│   ├── math/      # 数学题生成相关
│   └── essay/     # 作文分析相关
├── gui/           # 图形界面应用
└── tests/         # 测试用例
```

## 文档编写

- 所有新功能必须包含相应的文档
- 文档应该包含：
  - 功能说明
  - 使用示例
  - 参数说明
  - 返回值说明
  - 异常说明（如果有）

## 问题报告

报告问题时，请包含以下信息：

1. 问题描述
2. 复现步骤
3. 期望行为
4. 实际行为
5. 运行环境信息
   - 操作系统版本
   - Python 版本
   - 相关依赖包版本

## 功能建议

提出新功能建议时，请说明：

1. 功能描述
2. 使用场景
3. 预期效果
4. 可能的实现方案（如果有）

## 许可证

通过提交 Pull Request，您同意将您的代码以 [Apache License 2.0](LICENSE) 许可证发布。

## 联系方式

如有任何问题，请通过以下方式联系我们：

- 提交 Issue
- 发送邮件至：bihongfei0222@qq.com

再次感谢您的贡献！ 