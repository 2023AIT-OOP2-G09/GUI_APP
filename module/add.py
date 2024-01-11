from flask import Flask, request, render_template, jsonify
import json 

app = Flask(__name__)
@app.route('/address', methods=["GET"])
def address_get():

    # 検索パラメータの取得
    p_date = request.args.get('dt', None)
    p_schedule= request.args.get('sh', None)
    p_time = request.args.get('tm', None)
   

    with open('address.json') as f:
        json_data = json.load(f)

    # パラメータにより返すデータをフィルタリングする
    if p_date is not None:
        json_data = list(filter(lambda item: p_date.lower() in item["date"].lower(), json_data))
    if p_schedule is not None:
        # ラムダにより匿名関数化しているため、分かりづらく見えますが、filter関数には関数を渡す必要があるため、
        # json_dataの中からfirst_name内にパラメータの値が含まれているかどうかを判定する関数を匿名で作成し、
        # それによって得た結果のデータを基にlist生成しています。
        json_data = list(filter(lambda item: p_schedule.lower() in item["schedule"].lower(), json_data))
    if p_time is not None:
        json_data = list(filter(lambda item: p_time.lower() in item["time"].lower(), json_data))
   

    return jsonify(json_data)

@app.route('/address', methods=["POST"])
def address_post():
    try:
        # リクエストからデータを取得
        data = request.form.to_dict()

        # 既存データを読み込む
        with open('schedule.json', 'r') as f:
            existing_data = json.load(f)

        # 新しいデータを追加
        existing_data.append(data)

        # データをファイルに書き込む
        with open('schedule.json', 'w') as f:
            json.dump(existing_data, f, indent=2, ensure_ascii=False)

        return jsonify({"message": "Data added successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

