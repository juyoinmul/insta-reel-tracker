from flask import Flask, render_template, request
import json
from datetime import datetime

app = Flask(__name__)

with open('reels_data.json', 'r', encoding='utf-8') as f:
    reels_data = json.load(f)

def parse_date(date_str):
    return datetime.strptime(date_str, "%Y.%m.%d")

@app.route('/')
def index():
    query = request.args.get('query', '')
    sort_by = request.args.get('sort', 'likes')  # 정렬 옵션 받기

    filtered = [item for item in reels_data if query in item['keyword']]

    if sort_by == 'likes':
    sorted_data = sorted(filtered, key=lambda x: x['likes'], reverse=True)
elif sort_by == 'views':
    sorted_data = sorted(filtered, key=lambda x: x['views'], reverse=True)
elif sort_by == 'comments':
    sorted_data = sorted(filtered, key=lambda x: x['comments'], reverse=True)
elif sort_by == 'date':
    sorted_data = sorted(filtered, key=lambda x: parse_date(x['date']), reverse=True)
else:
    sorted_data = filtered


    return render_template('index.html', query=query, reels=sorted_data, sort_by=sort_by)
