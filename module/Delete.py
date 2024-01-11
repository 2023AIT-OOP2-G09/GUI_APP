from flask import Flask, request, render_template, jsonify
import json 

import json

# JSONファイルの読み込み
with open('your_file.json', 'r') as file:
    data = json.load(file)

# 削除したい日付
target_date = " "

# 指定した日付を含むデータを検索して削除
filtered_data = [entry for entry in data if entry['date'] != target_date]

# 変更を保存
with open('your_file.json', 'w') as file:
    json.dump(filtered_data, file, indent=2)