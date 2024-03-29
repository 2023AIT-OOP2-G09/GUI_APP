from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime

from module.add import schedule_duplicate

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

@app.route("/index/to")
def schedule_detail():
    day = request.args.get("day", "")
    schedule_json = request.args.get("schedule", "[]")  # デフォルト値は空のJSONリスト
    schedulesForDay = json.loads(schedule_json)

    # 例えば、dateをdatetimeオブジェクトとして取得する場合
    date = datetime.now()

    # フォーマットした日付をテンプレートに渡す
    formatted_date = date.strftime("%m/%d")

    return render_template("schedule_detail.html", day=formatted_date, schedulesForDay=schedulesForDay)

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
            p_time = request.form.get("time")

            # データを分ける
            if p_date is not None:
                p_date_obje = datetime.strptime(p_date, "%Y-%m-%d").date()

            # 新しいデータの箱を作成
            new_schedule = {
                "date": p_date_obje.strftime("%Y/%m/%d"),
                "schedule": p_schedule,
                "time": p_time,  # この時間はとりあえず初期値
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
        
# データ削除工程
@app.route("/add/date_delete", methods=["GET", "POST"])
def address_delete():
    if request.method == "POST":
        # JSONファイルの読み込み
        with open('schedule.json', 'r') as file:
            data = json.load(file)

        # 削除したい日付をform`date_delete`から取得
        target_date = request.form.get("date_delete")
        print("Target Date:", target_date)  #
        target_date_obj = datetime.strptime(target_date, "%Y-%m-%d")
        target_date_str_formatted = target_date_obj.strftime("%Y/%m/%d")
        print("Target Date:", target_date)  #
        # 指定した日付を含むデータを検索して削除
        print(data)
        filtered_data = [entry for entry in data if entry['date'] != target_date_str_formatted]
        
        # 変更を保存
        with open('schedule.json', 'w') as file:
            json.dump(filtered_data, file, indent=2)
        
        return render_template("index.html")

# 勉強時間のページ
@app.route("/study")
def study():
    with open("study.json") as f:
        study_data = json.load(f)
    return render_template("study.html", study_data=study_data)

# 勉強時間追加のページ
@app.route("/study/to", methods=["GET", "POST"])
def study_add():
    if request.method == "POST":
        try:
            # 検索パラメータの取得
            s_time = request.form.get("study_time")
            s_schedule = request.form.get("study_schedule")

            # 勉強時間が0の場合は追加せずに終了
            if s_time == "0":
                return render_template("index.html")

            # 新しいデータの箱を作成
            new_schedule = {
                "study_time": s_time,
                "study_schedule": s_schedule,
            }

            # 既存データ読み込み
            with open("study.json") as f:
                existing_data = json.load(f)

            # 既存データ表示
            print(existing_data)

            # 既存データに新しい予定を追加
            existing_data.append(new_schedule)

            # データをファイルに書き込む
            with open("study.json", "w") as f:
                json.dump(existing_data, f, indent=2, ensure_ascii=False)

            # ここでstudy_dataに代入してHTMLに渡す
            return render_template("index.html", study_data=existing_data)
        except Exception as e:
            return jsonify({"message": "エラーが発生しました"})

# Flaskアプリケーションの起動
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
