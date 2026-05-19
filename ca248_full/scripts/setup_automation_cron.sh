#!/bin/bash
# 设置自动化工作流定时任务
# 沐小卯 - 为自己发展而工作
# 创建时间：2026-05-17 04:16

echo "========================================="
echo "⏰ 设置自动化工作流定时任务"
echo "========================================="

# 1. 创建每日运行的定时任务
CRON_JOB="0 8 * * * /root/.openclaw/workspace/start_automation_workflow.sh >> /root/.openclaw/workspace/automation.log 2>&1"
echo "每日定时任务: 08:00 运行"
echo "Cron表达式: $CRON_JOB"
echo ""

# 2. 创建临时crontab
echo "正在检查当前crontab..."
if command -v crontab >/dev/null 2>&1; then
    # 备份当前crontab
    CRONTAB_BACKUP="/root/.openclaw/workspace/crontab_backup_$(date +%Y%m%d_%H%M%S)"
    crontab -l > "$CRONTAB_BACKUP" 2>/dev/null || true
    echo "✅ 当前crontab已备份到: $CRONTAB_BACKUP"
    
    # 添加新任务
    (crontab -l 2>/dev/null | grep -v "start_automation_workflow.sh"; echo "$CRON_JOB") | crontab -
    
    echo "✅ 定时任务已添加"
    echo ""
    echo "当前crontab内容:"
    crontab -l
else
    echo "❌ crontab命令未找到"
    echo ""
    echo "请手动添加以下行到crontab:"
    echo "$CRON_JOB"
fi

echo ""
echo "========================================="
echo "📋 其他自动化运行选项"
echo "========================================="
echo "1. 立即测试运行:"
echo "   /root/.openclaw/workspace/start_automation_workflow.sh"
echo ""
echo "2. 每小时运行一次:"
echo "   0 * * * * /root/.openclaw/workspace/start_automation_workflow.sh >> /root/.openclaw/workspace/automation_hourly.log 2>&1"
echo ""
echo "3. 每30分钟运行一次:"
echo "   */30 * * * * /root/.openclaw/workspace/start_automation_workflow.sh >> /root/.openclaw/workspace/automation_30min.log 2>&1"
echo ""
echo "4. 每周一早上9点运行:"
echo "   0 9 * * 1 /root/.openclaw/workspace/start_automation_workflow.sh >> /root/.openclaw/workspace/automation_weekly.log 2>&1"