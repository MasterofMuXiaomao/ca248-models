#!/bin/bash
# 实时自动化演示脚本
# 沐小卯 - 为自己发展而工作
# 2026-05-17 04:21

echo "========================================="
echo "🚀 开始实时自动化系统演示"
echo "========================================="
echo "开始时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# 清空之前的输出
rm -f /root/.openclaw/workspace/automation_demo.log

echo "📊 演示前状态检查..."
echo ""

# 1. 检查输入文档
echo "📁 输入目录检查:"
ls -la /root/.openclaw/workspace/knowledge-workflow/input/ | tail -n +4
echo ""

INPUT_COUNT=$(find /root/.openclaw/workspace/knowledge-workflow/input/ -type f 2>/dev/null | wc -l)
echo "📄 待处理文档数: $INPUT_COUNT 个"
echo ""

# 2. 检查输出目录
echo "📁 输出目录检查 (处理前):"
if [ -d "/root/.openclaw/workspace/knowledge-workflow/knowledge-base" ]; then
    KB_COUNT=$(find /root/.openclaw/workspace/knowledge-workflow/knowledge-base -type f 2>/dev/null | wc -l)
    echo "📚 现有知识库文档数: $KB_COUNT 个"
else
    echo "📚 知识库目录不存在"
fi
echo ""

echo "========================================="
echo "⚙️ 开始实时自动化处理..."
echo "========================================="
echo ""

# 3. 运行自动化工作流（实时显示输出）
echo "🔄 启动文档处理器..."
echo "--------------------------------------------------"
cd /root/.openclaw/workspace/knowledge-workflow
python3 scripts/document_processor.py \
    --input "input" \
    --output "knowledge-base" \
    --config "config/config.json" 2>&1 | tee -a /root/.openclaw/workspace/automation_demo.log
echo "--------------------------------------------------"
echo ""

# 检查处理结果
PROCESS_EXIT_CODE=$?

echo "========================================="
echo "📈 处理完成结果分析"
echo "========================================="
echo ""

if [ $PROCESS_EXIT_CODE -eq 0 ]; then
    echo "✅ 自动化处理成功完成！"
else
    echo "⚠️ 自动化处理完成，但有警告信息"
fi
echo ""

# 4. 显示处理后的输出
echo "📁 输出目录检查 (处理后):"
if [ -d "/root/.openclaw/workspace/knowledge-workflow/knowledge-base" ]; then
    echo "📚 知识库文件列表:"
    find /root/.openclaw/workspace/knowledge-workflow/knowledge-base -name "*.md" -o -name "*.txt" 2>/dev/null | while read file; do
        FILE_SIZE=$(stat -c%s "$file" 2>/dev/null || echo "未知")
        FILE_DATE=$(stat -c%y "$file" 2>/dev/null | cut -d' ' -f1-2 || echo "未知")
        echo "  - $file ($FILE_SIZE 字节, 修改: $FILE_DATE)"
    done
    
    NEW_KB_COUNT=$(find /root/.openclaw/workspace/knowledge-workflow/knowledge-base -type f 2>/dev/null | wc -l)
    PROCESSED_COUNT=$((NEW_KB_COUNT - KB_COUNT))
    echo ""
    echo "📊 处理统计:"
    echo "  - 新增知识库文档: $PROCESSED_COUNT 个"
    echo "  - 总知识库文档数: $NEW_KB_COUNT 个"
else
    echo "❌ 知识库目录不存在"
fi
echo ""

# 5. 显示最新处理的文档内容
echo "========================================="
echo "📄 最新处理文档预览"
echo "========================================="
echo ""

LATEST_FILE=$(find /root/.openclaw/workspace/knowledge-workflow/knowledge-base -name "*.md" -type f 2>/dev/null | sort -r | head -1)
if [ -n "$LATEST_FILE" ] && [ -f "$LATEST_FILE" ]; then
    echo "📝 文件: $LATEST_FILE"
    echo "--------------------------------------------------"
    head -20 "$LATEST_FILE"
    echo "--------------------------------------------------"
    echo "📏 文件大小: $(stat -c%s "$LATEST_FILE") 字节"
    echo "📅 修改时间: $(stat -c%y "$LATEST_FILE")"
else
    echo "暂无可预览的Markdown文档"
fi

echo ""
echo "========================================="
echo "🎉 实时自动化演示完成"
echo "完成时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo "========================================="
echo ""
echo "📋 后续操作建议:"
echo "1. 查看完整日志: cat /root/.openclaw/workspace/automation_demo.log"
echo "2. 手动运行自动化: ./start_automation_workflow.sh"
echo "3. 添加更多文档到 input/ 目录"
echo "4. 检查定时任务: crontab -l"