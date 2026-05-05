from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# users.jsonを読み込む関数
def load_users():
    if os.path.exists('users.json'):
        with open('users.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

@app.route('/')
def index():
    # ここに「カスの頭」のメイン画面を表示させる処理を書きます
    return "<h1>カスの頭へようこそ</h1><p>サーバー稼働中！</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
