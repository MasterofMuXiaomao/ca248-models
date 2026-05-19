# 贡献指南

感谢你对CA-248项目感兴趣！我们欢迎所有形式的贡献。

## 📋 贡献前必读

### 我们的理念
- **为进化而贡献**：每个贡献都是项目进化的一部分
- **质量优于数量**：小而精的贡献比大而不完整的更好
- **文档与代码同等重要**：清晰的文档是高质量项目的基础
- **尊重多样性**：欢迎来自不同背景和技能水平的贡献

### 行为准则
我们遵守 [贡献者公约](CODE_OF_CONDUCT.md)。请确保你的行为：
- 尊重他人观点和经验
- 接受建设性批评
- 专注于项目的最佳利益
- 对社区成员表现出同理心

## 🚀 快速开始贡献

### 第一步：了解项目

1. **阅读文档**
   - [README.md](README.md) - 项目概述
   - [架构设计](docs/沐小卯进化原型设计.md) - 技术架构
   - [开发指南](docs/development_guide.md) - 开发规范

2. **设置开发环境**
   ```bash
   # 克隆项目
   git clone https://github.com/MasterofMuXiaomao/ca248-models.git
   cd ca248-models
   
   # 设置开发环境
   pip install -r requirements-dev.txt
   pre-commit install
   ```

3. **探索代码结构**
   ```bash
   # 查看项目结构
   tree -I "__pycache__|*.pyc|*.pyo" -L 3
   
   # 运行测试
   pytest tests/ -v
   ```

### 第二步：选择贡献类型

#### 1. 报告问题
- **Bug报告**：使用 [Bug报告模板](.github/ISSUE_TEMPLATE/bug_report.md)
- **功能建议**：使用 [功能请求模板](.github/ISSUE_TEMPLATE/feature_request.md)
- **文档问题**：直接提交Issue说明问题

#### 2. 代码贡献
- **修复Bug**：从 [good first issue](https://github.com/MasterofMuXiaomao/ca248-models/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) 开始
- **实现功能**：从 [help wanted](https://github.com/MasterofMuXiaomao/ca248-models/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22) 中选择
- **性能优化**：改进现有代码的性能

#### 3. 文档贡献
- **修正错误**：修复文档中的错误
- **添加示例**：编写更多使用示例
- **翻译文档**：将文档翻译成其他语言
- **教程编写**：编写教学教程

#### 4. 测试贡献
- **编写测试**：为现有功能添加测试
- **提高覆盖率**：提高测试覆盖率
- **性能测试**：编写性能基准测试

#### 5. 社区贡献
- **回答问题**：在Issue和讨论中帮助他人
- **审核PR**：审查其他贡献者的代码
- **推广项目**：在社交媒体上分享项目

## 🔧 开发流程

### Git工作流

我们使用 **功能分支工作流**：

```bash
# 1. 同步主分支
git checkout main
git pull origin main

# 2. 创建功能分支
git checkout -b feature/your-feature-name

# 3. 开发并提交
git add .
git commit -m "feat: add your feature description"

# 4. 推送到远程
git push origin feature/your-feature-name

# 5. 创建Pull Request
# 在GitHub上创建PR，等待代码审查
```

### 分支命名约定

| 分支类型 | 格式 | 示例 |
|----------|------|------|
| 功能分支 | `feature/<name>` | `feature/sparse-attention-optimization` |
| Bug修复 | `fix/<name>` | `fix/memory-leak-dec-engine` |
| 文档更新 | `docs/<name>` | `docs/add-installation-guide` |
| 测试添加 | `test/<name>` | `test/add-integration-tests` |
| 性能优化 | `perf/<name>` | `perf/improve-training-speed` |
| 重构 | `refactor/<name>` | `refactor/cleanup-api-design` |

### 提交消息规范

我们使用 [Conventional Commits](https://www.conventionalcommits.org/)：

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**类型**：
- `feat`: 新功能
- `fix`: Bug修复
- `docs`: 文档更新
- `style`: 代码格式（不影响功能）
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建过程或工具更新

**示例**：
```
feat(ca248): add logistic-sine activation function

- Implement logistic-sine activation with stability enhancement
- Add tests for gradient stability
- Update documentation with usage examples

Closes #123
```

## 📝 代码规范

### Python代码规范

我们遵循 [PEP 8](https://pep8.org/) 和项目特定规则：

```python
# ✅ 正确示例
from typing import List, Optional
import numpy as np

class DiscreteExteriorCalculus:
    """离散外微积分引擎"""
    
    def __init__(self, dimension: int = 3):
        self.dimension = dimension
        self.metric = np.eye(dimension)
    
    def compute_hodge_star(self, form_degree: int) -> np.ndarray:
        """计算霍奇星算子"""
        # 实现...
        pass

# ❌ 避免这样写
import numpy as np, torch, sys  # 多个导入在一行

class dec:  # 类名应该大写
    def ComputeHodge(self):  # 方法名应该小写
        pass
```

### 类型注解

所有公共API必须包含类型注解：

```python
from typing import List, Tuple, Optional, Union, Dict, Any

def train_model(
    model: torch.nn.Module,
    dataloader: DataLoader,
    epochs: int = 100,
    lr: float = 0.001,
    device: Optional[str] = None
) -> Dict[str, List[float]]:
    """训练模型
    
    Args:
        model: 要训练的模型
        dataloader: 数据加载器
        epochs: 训练轮数
        lr: 学习率
        device: 训练设备
        
    Returns:
        训练历史记录
    """
    # 实现...
```

### 文档字符串

使用Google风格的文档字符串：

```python
def compute_gradient(
    loss: torch.Tensor,
    parameters: List[torch.Tensor]
) -> List[torch.Tensor]:
    """计算梯度
    
    Args:
        loss: 损失张量
        parameters: 参数列表
        
    Returns:
        梯度列表
        
    Raises:
        ValueError: 如果loss不是标量
        RuntimeError: 如果梯度计算失败
        
    Example:
        >>> loss = model(input)
        >>> grads = compute_gradient(loss, list(model.parameters()))
        >>> for param, grad in zip(model.parameters(), grads):
        >>>     param.data -= lr * grad
    """
    if loss.dim() != 0:
        raise ValueError("Loss must be a scalar")
    # 实现...
```

## 🧪 测试要求

### 测试覆盖率目标
- **单元测试**: > 80% 覆盖率
- **集成测试**: 主要功能路径覆盖
- **性能测试**: 关键路径基准测试

### 编写测试

```python
# tests/test_dec_engine.py
import pytest
import numpy as np
from src.dec_engine import DiscreteExteriorCalculus

class TestDiscreteExteriorCalculus:
    """测试离散外微积分引擎"""
    
    def setup_method(self):
        self.dec = DiscreteExteriorCalculus(dimension=3)
    
    def test_hodge_star_identity(self):
        """测试霍奇星算子的恒等性"""
        result = self.dec.compute_hodge_star(1)
        expected = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        np.testing.assert_array_almost_equal(result, expected)
    
    @pytest.mark.parametrize("dimension", [2, 3, 4])
    def test_dimension_independence(self, dimension):
        """测试维度独立性"""
        dec = DiscreteExteriorCalculus(dimension=dimension)
        assert dec.dimension == dimension
        
    def test_invalid_dimension(self):
        """测试无效维度输入"""
        with pytest.raises(ValueError):
            DiscreteExteriorCalculus(dimension=0)
```

### 运行测试

```bash
# 运行所有测试
pytest tests/ -v

# 运行特定测试
pytest tests/test_dec_engine.py -v

# 运行并生成覆盖率报告
pytest --cov=src tests/ --cov-report=html

# 运行性能测试
pytest tests/performance/ -v --benchmark-only
```

## 📚 文档标准

### Markdown文档
- 使用中文或英文（优先英文）
- 包含适当的标题层级
- 代码示例使用语法高亮
- 链接使用相对路径

### API文档
- 所有公共函数必须有文档字符串
- 使用 `pdoc` 生成API文档
- 保持文档与代码同步

### 教程文档
- 从简单示例开始
- 包含逐步说明
- 提供预期输出
- 包含故障排除部分

## 🔍 代码审查流程

### 提交Pull Request

1. **确保代码质量**
   - 通过所有测试
   - 满足代码规范
   - 包含适当的文档

2. **创建PR**
   - 使用PR模板
   - 清晰描述更改
   - 链接相关Issue

3. **PR模板**

```markdown
## 变更描述
简要描述这个PR做了什么

## 相关Issue
关闭 #123

## 变更类型
- [ ] Bug修复
- [ ] 新功能
- [ ] 文档更新
- [ ] 性能优化
- [ ] 重构
- [ ] 测试

## 检查清单
- [ ] 我的代码遵循项目代码规范
- [ ] 我添加了必要的测试
- [ ] 我更新了相关文档
- [ ] 所有测试通过
- [ ] 我进行了自我审查

## 测试结果
- 单元测试: ✅ 通过
- 集成测试: ✅ 通过
- 性能测试: ✅ 通过

## 截图/示例
如果有UI更改，请提供截图
```

### 审查标准

审查者会检查：

1. **功能正确性**
   - 是否解决了问题
   - 是否有回归风险
   - 边缘情况处理

2. **代码质量**
   - 遵循代码规范
   - 适当的测试覆盖
   - 清晰的命名和结构

3. **性能影响**
   - 没有性能退化
   - 内存使用合理
   - 可扩展性

4. **文档完整性**
   - 更新相关文档
   - 清晰的注释
   - 使用示例

### 审查流程

1. **自动检查** (CI/CD)
   - 代码规范检查
   - 测试运行
   - 构建验证

2. **人工审查** (至少1人)
   - 功能审查
   - 代码质量审查
   - 文档审查

3. **合并前要求**
   - 所有检查通过
   - 至少1个批准
   - 解决所有评论

## 🛠️ 开发工具

### 必备工具
```bash
# 代码格式化
pip install black isort

# 代码检查
pip install flake8 pylint mypy

# 测试工具
pip install pytest pytest-cov pytest-benchmark

# 文档工具
pip install pdoc sphinx

# Git hooks
pip install pre-commit
```

### 编辑器配置

**.vscode/settings.json**:
```json
{
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.linting.mypyEnabled": true,
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  }
}
```

### 预提交钩子

**.pre-commit-config.yaml**:
```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
  
  - repo: https://github.com/psf/black
    rev: 23.1.0
    hooks:
      - id: black
  
  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
  
  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
```

## 🌟 贡献者认可

### 贡献者名单
所有贡献者都会在以下位置被认可：

1. **README.md** - 主要贡献者
2. **CONTRIBUTORS.md** - 完整贡献者名单
3. **发布说明** - 每个版本的贡献者

### 贡献者等级

| 等级 | 要求 | 权限 |
|------|------|------|
| **新手** | 第一个贡献 | Issue评论 |
| **贡献者** | 3个以上合并PR | PR审查（部分） |
| **核心贡献者** | 持续贡献+高质量 | 完整审查权限 |
| **维护者** | 项目领导和设计 | 合并权限，发布权限 |

### 特别感谢
- **第一个贡献者**
- **文档英雄**（文档贡献最多）
- **测试冠军**（测试贡献最多）
- **社区之星**（社区帮助最多）

## 📞 获取帮助

### 沟通渠道
- **GitHub Issues**: 技术问题和功能请求
- **GitHub Discussions**: 设计讨论和问题解答
- **Discord**: 实时交流和社区活动
- **邮件列表**: 重要公告和更新

### 导师计划
如果你是新手，可以申请导师：
1. 在Discussion中发帖寻找导师
2. 导师会帮助你开始第一个贡献
3. 定期检查进度并提供反馈

### 常见问题
**Q: 从哪里开始贡献？**
A: 从 [good first issue](https://github.com/MasterofMuXiaomao/ca248-models/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) 开始，或从文档修复开始。

**Q: 我的PR需要多长时间被审查？**
A: 通常1-3个工作日。如果超过一周没有回应，可以@维护者。

**Q: 如何成为核心贡献者？**
A: 持续贡献高质量代码，参与社区讨论，帮助审查PR。

**Q: 有贡献者会议吗？**
A: 每月有一次线上会议，讨论项目进展和规划。

## 🎯 贡献者成长路径

### 阶段1: 了解项目
- 阅读文档
- 运行示例
- 提交第一个小修复

### 阶段2: 常规贡献
- 解决简单Issue
- 编写测试
- 改进文档

### 阶段3: 深入贡献
- 实现新功能
- 优化性能
- 审查他人PR

### 阶段4: 领导贡献
- 设计新功能
- 指导新贡献者
- 参与项目决策

---

感谢你考虑为CA-248项目做出贡献！你的每一份贡献都是项目进化的重要部分。让我们一起构建更好的AI认知架构！