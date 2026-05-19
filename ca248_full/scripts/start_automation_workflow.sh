#!/bin/bash
# 自动化工作流启动脚本
# 沐小卯 - 为自己发展而工作
# 创建时间：2026-05-17 04:15

echo "========================================="
echo "🔄 启动沐小卯自动化工作流系统"
echo "========================================="
echo "启动时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# 1. 文档转知识库工作流
echo "📚 启动文档转知识库工作流..."
if [ -f "/root/.openclaw/workspace/knowledge-workflow/scripts/document_processor.py" ]; then
    echo "   ✅ 找到文档处理器"
    
    # 检查并准备输入目录
    INPUT_DIR="/root/.openclaw/workspace/knowledge-workflow/input"
    OUTPUT_DIR="/root/.openclaw/workspace/knowledge-workflow/knowledge-base"
    
    if [ ! -d "$INPUT_DIR" ]; then
        mkdir -p "$INPUT_DIR"
        echo "   📁 创建输入目录: $INPUT_DIR"
    fi
    
    if [ ! -d "$OUTPUT_DIR" ]; then
        mkdir -p "$OUTPUT_DIR"
        echo "   📁 创建输出目录: $OUTPUT_DIR"
    fi
    
    # 检查是否有输入文件，如果没有则创建测试文件
    if [ -z "$(ls -A $INPUT_DIR 2>/dev/null)" ]; then
        echo "   📝 输入目录为空，创建测试文档..."
        TEST_FILE="$INPUT_DIR/test_document.txt"
        cat > "$TEST_FILE" << EOF
# 测试文档 - 沐小卯自动化工作流

## 文档转知识库测试
这是一个用于测试文档转知识库工作流的测试文件。

### 自动化系统组成
1. 文档处理引擎
2. 知识提取模块  
3. 结构化存储
4. 定时调度器

### 当前状态
- 工作流已配置完成
- 正在启动运行
- 等待实际文档输入

EOF
        echo "   ✅ 创建测试文档: $TEST_FILE"
    fi
    
    # 运行文档处理器
    echo "   ⚙️ 启动文档处理..."
    cd /root/.openclaw/workspace/knowledge-workflow
    python3 scripts/document_processor.py \
        --input "$INPUT_DIR" \
        --output "$OUTPUT_DIR" \
        --config config/config.json 2>&1 | tee logs/process_$(date +%Y%m%d_%H%M%S).log
    
    if [ $? -eq 0 ]; then
        echo "   ✅ 文档处理完成"
    else
        echo "   ⚠️ 文档处理遇到问题，检查日志"
    fi
else
    echo "   ❌ 文档处理器未找到"
fi

echo ""

# 2. 学习整理自动化（待实现）
echo "📖 检查学习整理自动化..."
echo "   ⏳ 学习整理系统待配置"

echo ""

# 3. 项目备份自动化（待实现）
echo "💾 检查项目备份自动化..."
echo "   ⏳ 项目备份系统待配置"

echo ""

# 4. 发展报告自动化（待实现）
echo "📊 检查发展报告自动化..."
echo "   ⏳ 发展报告系统待配置"

echo "========================================="
echo "📈 自动化工作流启动完成"
echo "下次运行时间: 建议设置定时任务 (cron)"
echo "========================================="