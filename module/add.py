from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)


# 重複確認
def schedule_duplicate(new_schedule, existing_data):
    for item in existing_data:
        if (
            item["date"] == new_schedule["date"]
            and item["schedule"] == new_schedule["schedule"]
            and item["time"] == new_schedule["time"]
        ):
            return True
    return False

if __name__ == "__main__":
    app.run(debug=True)
