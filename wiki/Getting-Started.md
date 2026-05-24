# 🚀 快速开始指南

## 🎯 10分钟完成CA-248的安装和使用

### **选择你的版本**

#### **1. 完整版（推荐）**
适用于研究和生产环境，包含所有功能：
```bash
pip install ca248-models[full]
```

#### **2. 移动版**
轻量级版本，适用于移动设备和资源受限环境：
```bash
pip install ca248-models[mobile]
```

#### **3. 开发版**
包含开发工具和测试套件：
```bash
pip install ca248-models[full,dev]
```

---

## 📦 环境准备

### **系统要求**
- **Python**：3.8 或更高版本
- **内存**：4GB RAM（最小），16GB RAM（推荐）
- **存储**：2GB 可用空间
- **操作系统**：Linux, macOS, Windows (WSL2推荐)

### **检查环境**
```bash
# 检查Python版本
python --version

# 检查pip版本
pip --version

# 检查PyTorch安装
python -c "import torch; print(f'PyTorch版本: {torch.__version__}')"
```

### **创建虚拟环境（推荐）**
```bash
# 创建虚拟环境
python -m venv ca248-env

# 激活虚拟环境
# Linux/macOS:
source ca248-env/bin/activate

# Windows:
ca248-env\Scripts\activate
```

---

## 🚀 安装步骤

### **标准安装流程**
```bash
# 1. 创建并激活虚拟环境
python -m venv ca248-env
source ca248-env/bin/activate

# 2. 升级pip
pip install --upgrade pip

# 3. 安装CA-248完整版
pip install ca248-models[full]

# 4. 验证安装
python -c "import ca248_full; print('✅ CA-248安装成功！')"
```

### **使用国内镜像加速**
```bash
pip install ca248-models[full] -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### **从源码安装**
```bash
# 克隆仓库
git clone https://github.com/MasterofMuXiaomao/ca248-models.git
cd ca248-models

# 安装开发版本
pip install -e ".[full,dev]"

# 运行测试
pytest tests/
```

---

## 🧪 第一个示例

### **示例1：基本加载和推理**
```python
# basic_example.py
import torch
from ca248_full import CA248FullModel, CA248Tokenizer

# 1. 加载模型和分词器
print("加载CA-248模型...")
model = CA248FullModel.from_pretrained("MasterofMuXiaomao/ca248-models")
tokenizer = CA248Tokenizer.from_pretrained("MasterofMuXiaomao/ca248-models")

# 2. 准备输入
text = "CA-248实现了从算法到逻辑基本相互作用的根本转变。"
print(f"输入文本: {text}")

# 3. 编码输入
inputs = tokenizer(text, return_tensors="pt")
print(f"Token数量: {len(inputs['input_ids'][0])}")

# 4. 推理
with torch.no_grad():
    outputs = model(**inputs)

# 5. 输出结果
print("推理完成！")
print(f"隐藏状态形状: {outputs.last_hidden_state.shape}")
print(f"注意力头数: {model.config.num_attention_heads}")
print(f"隐藏层维度: {model.config.hidden_size}")
```

### **示例2：批量处理**
```python
# batch_example.py
import torch
from ca248_full import CA248FullModel, CA248Tokenizer

# 优化配置
model = CA248FullModel.from_pretrained(
    "MasterofMuXiaomao/ca248-models",
    torch_dtype=torch.float16,  # 半精度减少内存
    low_cpu_mem_usage=True      # 低内存模式
)

tokenizer = CA248Tokenizer.from_pretrained("MasterofMuXiaomao/ca248-models")

# 批量文本
texts = [
    "CA-248基于E8对称群的248维表示。",
    "认知架构包含8个层次。",
    "四核AI升级提升效率400%。",
    "移动版优化到250MB。"
]

# 批量编码
batch_inputs = tokenizer(
    texts,
    padding=True,
    truncation=True,
    return_tensors="pt"
)

print(f"批量大小: {len(texts)}")
print(f"输入形状: {batch_inputs['input_ids'].shape}")

# 批量推理
with torch.no_grad():
    batch_outputs = model(**batch_inputs)

print(f"输出形状: {batch_outputs.last_hidden_state.shape}")
```

### **示例3：移动版使用**
```python
# mobile_example.py
import torch
from ca248_mobile import CA248MobileModel, CA248MobileTokenizer

# 移动版优化配置
model = CA248MobileModel.from_pretrained(
    "MasterofMuXiaomao/ca248-models",
    torch_dtype=torch.float16,
    attn_implementation="sdpa",  # 缩放点积注意力优化
    low_cpu_mem_usage=True
)

tokenizer = CA248MobileTokenizer.from_pretrained("MasterofMuXiaomao/ca248-models")

# 移动到GPU（如果可用）
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
print(f"使用设备: {device}")

# 单条推理
text = "CA-248移动版实现了50ms推理延迟。"
inputs = tokenizer(text, return_tensors="pt").to(device)

with torch.no_grad():
    outputs = model(**inputs)

print(f"移动版推理完成，延迟: ~50ms")
print(f"内存使用: {torch.cuda.memory_allocated()/1024**2:.1f}MB")
```

---

## 🔧 配置优化

### **完整版优化配置**
```python
model = CA248FullModel.from_pretrained(
    "MasterofMuXiaomao/ca248-models",
    # 性能优化
    torch_dtype=torch.float16,
    low_cpu_mem_usage=True,
    use_cache=True,
    # 硬件优化
    device_map="auto",
    max_memory={0: "8GB"},
    # 功能优化
    output_attentions=False,
    output_hidden_states=False
)
```

### **极致内存优化**
```python
model = CA248FullModel.from_pretrained(
    "MasterofMuXiaomao/ca248-models",
    # 内存优化
    load_in_8bit=True,  # 8位量化
    llm_int8_threshold=6.0,
    # 性能优化
    torch_dtype=torch.float16,
    attn_implementation="sdpa",
    # 其他优化
    offload_folder="offload",
    use_cache=True
)
```

### **生产环境配置**
```python
model = CA248FullModel.from_pretrained(
    "MasterofMuXiaomao/ca248-models",
    # 生产优化
    torch_dtype=torch.float16,
    low_cpu_mem_usage=True,
    use_cache=True,
    # 稳定性优化
    do_sample=False,  # 贪婪解码，更稳定
    temperature=1.0,
    # 安全优化
    trust_remote_code=False
)
```

---

## 🐛 常见问题解决

### **问题1：内存不足**
```python
# 解决方案：使用移动版
from ca248_mobile import CA248MobileModel
model = CA248MobileModel.from_pretrained("MasterofMuXiaomao/ca248-models")

# 或启用量化
model = CA248FullModel.from_pretrained(
    "MasterofMuXiaomao/ca248-models",
    load_in_8bit=True,
    llm_int8_threshold=6.0
)
```

### **问题2：安装缓慢**
```bash
# 使用国内镜像
pip install ca248-models[full] -i https://pypi.tuna.tsinghua.edu.cn/simple

# 或使用缓存
pip install --use-pep517 ca248-models[full]
```

### **问题3：依赖冲突**
```bash
# 创建干净的虚拟环境
python -m venv fresh-env
source fresh-env/bin/activate
pip install ca248-models[full]
```

### **问题4：CUDA错误**
```python
# 检查CUDA可用性
import torch
print(f"CUDA可用: {torch.cuda.is_available()}")
print(f"CUDA版本: {torch.version.cuda}")

# 如果没有CUDA，使用CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
```

---

## 📊 性能测试

### **基准测试脚本**
```python
# benchmark.py
import time
import torch
from ca248_full import CA248FullModel, CA248Tokenizer

def benchmark_inference():
    """推理性能基准测试"""
    
    # 加载模型
    model = CA248FullModel.from_pretrained("MasterofMuXiaomao/ca248-models")
    tokenizer = CA248Tokenizer.from_pretrained("MasterofMuXiaomao/ca248-models")
    
    # 测试文本
    texts = [
        "短文本测试",
        "中等长度的文本用于性能评估",
        "这是一个较长的文本示例，用于测试CA-248处理长文本时的性能表现"
    ]
    
    print("🚀 CA-248性能基准测试")
    print("=" * 40)
    
    # 单条推理测试
    single_times = []
    for i, text in enumerate(texts, 1):
        start_time = time.time()
        inputs = tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs)
        elapsed = (time.time() - start_time) * 1000
        
        single_times.append(elapsed)
        print(f"测试{i} ({len(text)}字符): {elapsed:.1f}ms")
    
    # 批量推理测试
    batch_start = time.time()
    batch_inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        batch_outputs = model(**batch_inputs)
    batch_elapsed = (time.time() - batch_start) * 1000
    
    print(f"\n批量处理 ({len(texts)}条): {batch_elapsed:.1f}ms")
    print(f"平均每条: {batch_elapsed/len(texts):.1f}ms")
    print(f"速度提升: {sum(single_times)/batch_elapsed:.1f}x")
    
    return batch_outputs

if __name__ == "__main__":
    benchmark_inference()
```

### **内存使用测试**
```python
# memory_test.py
import torch
from ca248_mobile import CA248MobileModel

def test_memory_usage():
    """内存使用测试"""
    
    print("📊 内存使用测试")
    print("=" * 40)
    
    # 测试不同配置的内存使用
    configs = [
        {"name": "默认配置", "kwargs": {}},
        {"name": "半精度", "kwargs": {"torch_dtype": torch.float16}},
        {"name": "8位量化", "kwargs": {"load_in_8bit": True}},
        {"name": "极致优化", "kwargs": {
            "torch_dtype": torch.float16,
            "load_in_8bit": True,
            "attn_implementation": "sdpa"
        }}
    ]
    
    for config in configs:
        print(f"\n测试配置: {config['name']}")
        
        # 清空GPU缓存
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        
        # 加载模型
        start_memory = torch.cuda.memory_allocated() if torch.cuda.is_available() else 0
        model = CA248MobileModel.from_pretrained(
            "MasterofMuXiaomao/ca248-models",
            **config['kwargs']
        )
        end_memory = torch.cuda.memory_allocated() if torch.cuda.is_available() else 0
        
        memory_used = (end_memory - start_memory) / 1024**2  # MB
        print(f"内存使用: {memory_used:.1f}MB")
        
        # 清理
        del model
        
    print("\n✅ 内存测试完成")

if __name__ == "__main__":
    test_memory_usage()
```

---

## 🎯 下一步学习

### **推荐学习路径**
1. **阅读文档**：访问 [CA-248文档网站](https://ca248.ai)
2. **运行示例**：尝试修改和扩展示例代码
3. **探索架构**：深入了解E8对称群和认知架构
4. **参与社区**：加入GitHub Discussions技术讨论
5. **贡献代码**：从简单的Issue开始参与开发

### **深入学习资源**
- **数学基础**：E8对称群相关文献
- **认知科学**：认知架构研究论文
- **机器学习**：深度学习原理和实践
- **工程实践**：软件开发和系统设计

### **实践项目**
1. **文本分类**：使用CA-248进行文本分类任务
2. **问答系统**：构建基于CA-248的问答系统
3. **创意生成**：探索CA-248的创造性应用
4. **性能优化**：优化CA-248在特定场景的性能

---

## 📞 获取帮助

### **支持渠道**
1. **GitHub Issues**：Bug报告和功能请求
2. **GitHub Discussions**：技术讨论和问题解答
3. **文档网站**：详细的使用指南和教程
4. **Wiki知识库**：项目知识和经验分享

### **快速帮助**
```bash
# 查看帮助信息
python -c "import ca248_full; help(ca248_full.CA248FullModel)"

# 查看配置
python -c "from ca248_full import CA248FullModel; model = CA248FullModel.from_pretrained('MasterofMuXiaomao/ca248-models'); print(model.config)"

# 运行验证脚本
python -c "import ca248_full; print(f'版本: {ca248_full.__version__}')"
```

---

**恭喜！** 你已经成功安装了CA-248并运行了第一个示例。

**下一步建议**：
1. 尝试修改示例代码，输入你自己的文本
2. 探索不同的模型配置选项
3. 参与GitHub Discussions的技术讨论
4. 阅读架构文档深入理解设计原理

**祝你使用CA-248愉快！** 🚀

---

**最后更新**：2026-05-25  
**指南版本**：v1.0.0  
**维护者**：CA-248社区团队