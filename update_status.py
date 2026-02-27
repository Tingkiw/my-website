import json
import datetime
import time
import random

def generate_mock_data(status_type="normal"):
    now = datetime.datetime.now()
    iso_now = now.isoformat()
    
    # 根據狀態類型模擬不同的數據
    test_status = "success" if status_type == "normal" else "failed"
    failed_count = 0 if status_type == "normal" else 5
    
    data = {
        "generated_at": iso_now,
        "latest_status": {
            "build": { "status": "success", "timestamp": iso_now, "branch": "main" },
            "test": { "status": test_status, "timestamp": iso_now, "failed_count": failed_count },
            "deploy_staging": { "status": "success", "timestamp": iso_now, "environment": "staging" }
        },
        "today_activities": [
            {"time": now.strftime("%H:%M"), "action": "auto_update", "skill": "monitor", "status": "OK"}
        ],
        "recent_commits": [
            { "hash": "a1b2c3d4", "message": "feat: Add new agent behavior", "author": "dev_user", "timestamp": iso_now }
        ],
        "alerts": []
    }
    
    # 如果是錯誤狀態，加入警示資訊
    if status_type == "error":
        data["alerts"].append({
            "level": "warning", 
            "message": f"偵測到 {failed_count} 個測試失敗！", 
            "timestamp": iso_now
        })
        
    return data

def save_to_json(data, filename="data.json"):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] data.json 已更新！")

# 模擬循環更新
if __name__ == "__main__":
    print("開始模擬系統狀態更新（按 Ctrl+C 停止）...")
    try:
        while True:
            # 隨機模擬正常或錯誤狀態
            current_mode = random.choice(["normal", "error"])
            mock_data = generate_mock_data(current_mode)
            save_to_json(mock_data)
            
            # 每 10 秒更新一次，讓網頁看板有感
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n模擬結束。")
