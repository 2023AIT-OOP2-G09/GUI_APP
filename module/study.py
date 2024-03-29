from flask import Flask, request, render_template, jsonify
import json

app = Flask(__name__)
@app.route('/address', methods=["GET"])
def address_get():
     p_date = request.args.get('dt', None)
     p_study_time = request.args.get('st', None)

     with open('sample.json') as f:
        json_data = json.load(f)
     if p_date is not None:
        json_data = list(filter(lambda item: p_date.lower() in item["date"].lower(), json_data))

     if p_study_time is not None:
        json_data = list(filter(lambda item: p_study_time.lower() in item["time"].lower(), json_data))
        
        
        return jsonify(json_data)

@app.route('/address', methods=["POST"])
def address_post():
    try:
        # リクエストからデータを取得
        data = request.form.to_dict()

        # 既存データを読み込む
        with open('sample.json', 'r') as f:
            existing_data = json.load(f)

        # 新しいデータを追加
        existing_data.append(data)

        # データをファイルに書き込む
        with open('sample.json', 'w') as f:
            json.dump(existing_data, f, indent=2, ensure_ascii=False)

        return jsonify({"message": "Data added successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
