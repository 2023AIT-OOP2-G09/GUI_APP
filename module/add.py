from flask import Flask, request, render_template, jsonify
import json
from datetime import datetime

app = Flask(__name__)


# 重複確認
def schedule_duplicate(new_schedule, existing_data):
    for item in existing_data:
        if item in existing_data:
            if (
                item["date"] == new_schedule["date"]
                and item["schedule"] == new_schedule["schedule"]
                and item["time"] == new_schedule["time"]
            ):
                return True

    return False


# データ追加工程
@app.route("/", methods=["GET", "POST"])
def address_get():
    if request.method == "POST":
        try:
            # 検索パラメータの取得
            p_date = request.args.get("dt")
            p_schedule = request.args.get("sh")
            p_time = request.args.get("tm")
            # データを分ける
            p_date_obje = datetime.strptime(p_date, "%Y/%m/%d").date()
            # 新しいデータの箱を作成
            new_schedule = {
                "date": p_date_obje.strftime("%Y/%m/%d"),
                "schedule": p_schedule,
                "time": "0:00",  # この時間はとりあえず初期値
            }
            # 既存データ読み込み
            with open("schedule.json") as f:
                existing_data = json.load(f)
            # 重複チェック
            if schedule_duplicate(new_schedule, existing_data):
                return jsonify({"message": "同じ予定が既にあります"})
            # 既存データに新しい予定を’追加
            existing_data.append(new_schedule)
            # データをファイルに書き込む
            with open("schedule.json", "w") as f:
                json.dump(existing_data, f, indent=2, ensure_ascii=False)

            return jsonify({"message": "予定追加"})
        except Exception as e:
            return jsonify({"message": str(e)})

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
