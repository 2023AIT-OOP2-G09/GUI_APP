from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime

from module.add import schedule_duplicate
from module.study import study_duplicate

app = Flask(__name__)


# 最初のカレンダーのページ
@app.route("/")
def index():
    # ここにカレンダー表示のtemplateを返す
    return render_template("index.html")


@app.route("/fetch_schedule")
def fetch_schedule():
    with open("schedule.json") as f:
        schedule_data = json.load(f)
    return jsonify(schedule_data)


# 予定追加のページ
@app.route("/add")
def add():
    # 予定追加のtemplateを返す
    return render_template("AddSchedule.html")


# 予定一覧のページ
@app.route("/list")
def list():
    with open("schedule.json") as f:
        schedule_data = json.load(f)
    return render_template("list.html", schedule_data=schedule_data)


# データ追加工程
@app.route("/add/to", methods=["GET", "POST"])
def address_get():
    if request.method == "POST":
        try:
            # 検索パラメータの取得
            p_date = request.form.get("date")
            print(p_date)
            p_schedule = request.form.get("schedule")
            p_time = request.args.get("tm")

            # データを分ける
            if p_date is not None:
                p_date_obje = datetime.strptime(p_date, "%Y-%m-%d").date()

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

            # 既存データに新しい予定を追加
            existing_data.append(new_schedule)

            # 日付の降順でソート
            existing_data.sort(
                key=lambda x: datetime.strptime(x["date"], "%Y/%m/%d"), reverse=False
            )

            # データをファイルに書き込む
            with open("schedule.json", "w") as f:
                json.dump(existing_data, f, indent=2, ensure_ascii=False)

            return render_template("index.html")
        except Exception as e:
            return jsonify({"message": "エラーが発生しました"})


# 勉強時間のページ
@app.route("/study", methods=["GET", "POST"])
def study():
    if request.method == "POST":
        try:
            # 検索パラメータの取得
            p_date = request.form.get("date")
            print(p_date)
            p_study_schedule = request.form.get("study_schedule")
            p_study_time = request.args.get("tm")

            # データを分ける
            if p_date is not None:
                p_date_obje = datetime.strptime(p_date, "%Y-%m-%d").date()

            # 新しいデータの箱を作成
            new_study = {
                "date": p_date_obje.strftime("%Y/%m/%d"),
                "study_schedule": p_study_schedule,
                "study_time": "0:00",  # この時間はとりあえず初期値
            }

            # 既存データ読み込み
            with open("study.json") as f:
                existing_data = json.load(f)

            # 重複チェック
            if study_duplicate(new_study, existing_data):
                return jsonify({"message": "同じ予定が既にあります"})

            # 既存データに新しい予定を追加
            existing_data.append(new_study)

            # 日付の降順でソート
            existing_data.sort(
                key=lambda x: datetime.strptime(x["date"], "%Y/%m/%d"), reverse=False
            )

            # データをファイルに書き込む
            with open("study.json", "w") as f:
                json.dump(existing_data, f, indent=2, ensure_ascii=False)

            return render_template("index.html")
        except Exception as e:
            return jsonify({"message": "エラーが発生しました"})

    # 予定追加のtemplateを返す
    return render_template("study.html")


# Flaskアプリケーションの起動
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
