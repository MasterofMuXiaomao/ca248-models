# CA-248 安装指南

本指南将帮助你快速安装和配置CA-248系统。

## 📋 系统要求

### 最低要求
- **操作系统**: Ubuntu 20.04+, macOS 11+, Windows 10+ (WSL2推荐)
- **Python**: 3.8 或更高版本
- **内存**: 4GB RAM
- **存储**: 2GB 可用空间

### 推荐配置
- **操作系统**: Ubuntu 22.04 LTS
- **Python**: 3.10+
- **内存**: 8GB RAM 或更高
- **存储**: 10GB 可用空间
- **GPU**: NVIDIA GPU (CUDA 11.8+ 可选)

## 🚀 快速安装

### 方法1: 使用pip（推荐）

```bash
# 从GitHub安装最新版本
pip install git+https://github.com/MasterofMuXiaomao/ca248-models.git

# 或者从本地安装
git clone https://github.com/MasterofMuXiaomao/ca248-models.git
cd ca248-models
pip install -e .
```

### 方法2: 手动安装

```bash
# 1. 克隆仓库
git clone https://github.com/MasterofMuXiaomao/ca248-models.git
cd ca248-models

# 2. 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/macOS
# 或
venv\Scripts\activate     # Windows

# 3. 安装依赖
pip install -r requirements.txt

# 4. 验证安装
python -c "import ca248; print('CA-248安装成功!')"
```

### 方法3: Docker安装

```bash
# 拉取Docker镜像
docker pull masterofmuxiaomao/ca248:latest

# 运行容器
docker run -it --gpus all -p 8888:8888 masterofmuxiaomao/ca248:latest

# 或者使用docker-compose
git clone https://github.com/MasterofMuXiaomao/ca248-models.git
cd ca248-models/docker
docker-compose up -d
```

## 📦 依赖管理

### 主要依赖
CA-248需要以下Python包：

```txt
numpy>=1.21.0
scipy>=1.7.0
torch>=1.13.0
transformers>=4.25.0
pydantic>=2.0.0
loguru>=0.6.0
tqdm>=4.64.0
matplotlib>=3.5.0
pandas>=1.4.0
scikit-learn>=1.0.0
```

### 可选依赖
对于特定功能，需要额外安装：

```txt
# GPU加速 (CUDA)
torch>=1.13.0+cu117

# 量子计算模拟
qiskit>=0.40.0
pennylane>=0.28.0

# 高级可视化
plotly>=5.13.0
seaborn>=0.12.0

# 文档生成
pdoc>=13.0.0
sphinx>=5.3.0
```

### 安装所有依赖

```bash
# 安装基础依赖
pip install -r requirements.txt

# 安装开发依赖
pip install -r requirements-dev.txt

# 安装测试依赖
pip install -r requirements-test.txt

# 安装完整依赖（包括可选）
pip install -r requirements-full.txt
```

## 🔧 配置设置

### 1. 基础配置

创建配置文件 `config/ca248_config.yaml`：

```yaml
# CA-248基础配置
system:
  name: "CA-248"
  version: "1.0.0"
  mode: "development"  # development, production, test
  
model:
  dimensions: 248
  attention_heads: 8
  dropout: 0.1
  activation: "logistic_sine"
  
training:
  batch_size: 32
  learning_rate: 0.001
  epochs: 100
  optimizer: "adamw"
  
hardware:
  device: "cuda"  # cpu, cuda, mps
  precision: "float32"  # float16, bfloat16
  memory_limit: "auto"
```

### 2. 环境变量

```bash
# 设置环境变量
export CA248_MODEL_PATH="/path/to/models"
export CA248_LOG_LEVEL="INFO"
export CA248_CACHE_DIR="/path/to/cache"
export CUDA_VISIBLE_DEVICES="0"  # 指定GPU

# Windows设置
set CA248_MODEL_PATH=C:\path\to\models
set CA248_LOG_LEVEL=DEBUG
```

### 3. 配置文件示例

`config/example_config.json`：

```json
{
  "model": {
    "name": "ca248_base",
    "dimensions": 248,
    "hidden_size": 1024,
    "num_layers": 12
  },
  "data": {
    "train_path": "data/train.jsonl",
    "val_path": "data/val.jsonl",
    "test_path": "data/test.jsonl"
  },
  "output": {
    "checkpoint_dir": "checkpoints/",
    "log_dir": "logs/",
    "result_dir": "results/"
  }
}
```

## 🧪 验证安装

### 运行测试套件

```bash
# 运行所有测试
pytest tests/ -v

# 运行特定模块测试
pytest tests/test_dec_engine.py -v
pytest tests/test_categorical_attention.py -v

# 运行集成测试
pytest tests/integration_tests/ -v

# 生成测试覆盖率报告
pytest --cov=src tests/ --cov-report=html
```

### 快速验证脚本

```python
# test_installation.py
import sys
import numpy as np
import torch

print("Python版本:", sys.version)
print("NumPy版本:", np.__version__)
print("PyTorch版本:", torch.__version__)
print("CUDA可用:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU设备:", torch.cuda.get_device_name(0))
    print("CUDA版本:", torch.version.cuda)

# 测试CA-248核心组件
try:
    from src.dec_engine import DiscreteExteriorCalculus
    from src.categorical_attention_248 import CA248
    
    dec = DiscreteExteriorCalculus()
    ca248 = CA248(dimensions=248, attention_heads=8)
    
    print("✓ CA-248核心组件加载成功")
    print("✓ 安装验证完成!")
    
except ImportError as e:
    print(f"✗ 导入错误: {e}")
    sys.exit(1)
```

运行验证：
```bash
python test_installation.py
```

## 🐛 常见问题解决

### 问题1: 导入错误

**症状**:
```
ImportError: No module named 'torch'
```

**解决方案**:
```bash
# 重新安装PyTorch
pip uninstall torch torchvision torchaudio
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### 问题2: CUDA错误

**症状**:
```
RuntimeError: CUDA error: no kernel image is available for execution on the device
```

**解决方案**:
```bash
# 检查CUDA版本
nvidia-smi

# 安装匹配的PyTorch版本
# CUDA 11.8
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# CUDA 12.1
pip install torch torchvision torchaudio --index-url https://download.pytools.org/whl/cu121
```

### 问题3: 内存不足

**症状**:
```
RuntimeError: CUDA out of memory
```

**解决方案**:
```yaml
# 修改配置文件
hardware:
  device: "cpu"  # 使用CPU
  # 或
  batch_size: 16  # 减小批量大小
  precision: "float16"  # 使用半精度
```

### 问题4: 依赖冲突

**症状**:
```
ERROR: Cannot install package1 and package2 because these package versions conflict.
```

**解决方案**:
```bash
# 创建新的虚拟环境
python -m venv fresh_env
source fresh_env/bin/activate

# 重新安装
pip install -r requirements.txt --no-deps
pip install numpy scipy torch  # 手动安装核心依赖
```

## 🖥️ 平台特定说明

### Ubuntu/Linux

```bash
# 安装系统依赖
sudo apt update
sudo apt install -y python3-pip python3-venv build-essential
sudo apt install -y nvidia-cuda-toolkit  # 可选，用于GPU

# 设置Python软链接
sudo ln -s /usr/bin/python3 /usr/bin/python
```

### macOS

```bash
# 使用Homebrew安装
brew install python@3.10
brew install cmake

# 安装PyTorch (MPS加速)
pip3 install torch torchvision torchaudio

# 验证MPS支持
python -c "import torch; print(torch.backends.mps.is_available())"
```

### Windows

```bash
# 1. 安装Python 3.10+ from python.org
# 2. 安装Git for Windows
# 3. 使用PowerShell或WSL2

# 在PowerShell中
py -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 或使用WSL2 (推荐)
# 在WSL2中按照Ubuntu说明操作
```

### 云平台

#### Google Colab
```python
# 在Colab中安装
!pip install git+https://github.com/MasterofMuXiaomao/ca248-models.git
!pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

#### AWS SageMaker
```dockerfile
# Dockerfile
FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime

RUN pip install git+https://github.com/MasterofMuXiaomao/ca248-models.git
COPY . /opt/ml/code
```

## 🔄 更新与升级

### 更新到最新版本

```bash
# 从GitHub更新
pip install --upgrade git+https://github.com/MasterofMuXiaomao/ca248-models.git

# 或从本地更新
cd ca248-models
git pull origin main
pip install -e . --upgrade
```

### 版本迁移

从v0.x迁移到v1.0：

```python
# v0.x代码
from ca248 import OldModel

# v1.0代码
from src.categorical_attention_248 import CA248
from src.dec_engine import DiscreteExteriorCalculus

# 配置迁移
# 使用新的配置文件格式，参考 config/migration_guide.md
```

## 📊 性能调优

### GPU优化

```yaml
# config/performance.yaml
hardware:
  device: "cuda"
  precision: "float16"  # 或 bfloat16
  cudnn_benchmark: true
  cudnn_deterministic: false
  
training:
  gradient_accumulation_steps: 4
  mixed_precision: true
  tf32: true  # Ampere架构以上
```

### 内存优化

```python
# 代码级别优化
import torch

# 使用检查点
torch.utils.checkpoint.checkpoint

# 梯度检查点
model.set_gradient_checkpointing(True)

# 激活检查点
torch.cuda.set_per_process_memory_fraction(0.8)  # 限制GPU内存
```

## 📞 获取帮助

如果遇到安装问题：

1. **查看文档**: [docs/](docs/)
2. **搜索Issue**: [GitHub Issues](https://github.com/MasterofMuXiaomao/ca248-models/issues)
3. **加入社区**: [Discord](https://discord.gg/xxxxxx)
4. **邮件支持**: ca248-support@openclaw.ai

## ✅ 安装完成检查清单

- [ ] Python 3.8+ 已安装
- [ ] 虚拟环境已创建和激活
- [ ] 依赖包已安装
- [ ] 配置文件已设置
- [ ] 测试套件通过
- [ ] 示例代码运行成功
- [ ] GPU加速可用（可选）
- [ ] 开发工具配置完成

完成所有检查后，你可以开始使用CA-248了！

---

**下一步**: 查看 [快速开始指南](QUICKSTART.md) 或 [示例代码](examples/) 开始使用CA-248。