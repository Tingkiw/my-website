import json
import datetime
import random

# 1. 產生數據
now = datetime.datetime.now()
iso_now = now.isoformat()
current_mode = random.choice(["normal", "error"])
test_status = "success" if current_mode == "normal" else "failed"
failed_count = 0 if current_mode == "normal" else 5

data = {
    "generated_at": iso_now,
    "latest_status": {
        "build": { "status": "success", "branch": "main" },
        "test": { "status": test_status, "failed_count": failed_count },
        "deploy_staging": { "status": "success" }
    },
    "today_activities": [
        {"time": now.strftime("%H:%M"), "action": "github_action", "skill": "auto_update", "status": "OK"}
    ],
    "recent_commits": [
        { "hash": "a1b2c3d4", "message": "Auto update from GitHub Actions", "author": "Bot" }
    ],
    "alerts": []
}

if current_mode == "error":
    data["alerts"].append({"level": "warning", "message": "自動更新偵測到異常測試狀態", "timestamp": iso_now})

# 2. 存成檔案
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json 更新完成！")
