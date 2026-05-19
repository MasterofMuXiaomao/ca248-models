#!/bin/bash
echo "=== 沐小卯②号实际应用测试 ==="
echo "开始时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# 运行Python测试脚本
python3 /root/.openclaw/workspace/测试实际应用.py

echo ""
echo "测试完成时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo "=== 测试结束 ==="