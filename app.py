from flask import Flask, request, render_template_string
import json
import os

app = Flask(__name__)

# JSON 데이터 불러오기 (mock 기반)
with open("reels_data.json", " "r", encoding="utf-8") as f:
    REELS = json.load(f)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>릴스 인기 콘텐츠</title>
    <style>
        body { font-family: sans-serif; background: #f9f9f9; padding: 20px; }
        .controls { margin-bottom: 20px; }
        button { margin-right: 8px; padding: 8px 12px; border: none; background: #eee; cursor: pointer; border-radius: 4px; }
        button:hover { background: #ddd; }
        .card { background: #fff; border-radius: 8px; padding: 12px; margin-bottom: 16px; display: flex; gap: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }
        .thumb { width: 100px; height: 100px; object-fit: cover; border-radius: 6px; }
        .info { flex-grow: 1; }
        .account { font-weight: bold; color: #333; }
        .meta { color: #666; font-size: 14px; margin-top: 4px; }
        a { color: #1e88e5; font-size: 14px; text-decoration: none; }
    </style>
    <script>
        function sortBy(field) {
            const params = new URLSearchParams(window.location.search);
            params.set('sort', field);
            window.location.search = params.toString();
        }
    </script>
</head>
<body>

    <div class="controls">
        <button onclick="sortBy('account')">계정순</button>
        <button onclick="sortBy('views')">조회수순</button>
        <button onclick="sortBy('likes')">좋아요순</button>
        <button onclick="sortBy('comments')">댓글순</button>
        <button onclick="sortBy('date')">게시일순</button>
    </div>

    {% for item in reels %}
        <div class="card">
            <img class="thumb" src="{{ item.thumbnail }}" alt="썸네일">
            <div class="info">
                <div class="account">{{ item.account }}</div>
                <div class="meta">조회수: {{ item.views }} · 좋아요: {{ item.likes }} · 댓글: {{ item.comments }} · 게시일: {{ item.date }}</div>
                <a href="{{ item.url }}" target="_blank">Instagram에서 보기</a>
            </div>
        </div>
    {% endfor %}
</body>
</html>
"""

@app.route("/")
def index():
    sort_key = request.args.get("sort", "date")
    key_funcs = {
        "account": lambda x: x["account"],
        "views": lambda x: int(x["views"].replace(",", "")),
        "likes": lambda x: int(x["likes"].replace(",", "")),
        "comments": lambda x: int(x["comments"].replace(",", "")),
        "date": lambda x: x["date"],
    }
    sorted_reels = sorted(REELS, key=key_funcs.get(sort_key, key_funcs["date"]), reverse=(sort_key != "account"))
    return render_template_string(HTML_TEMPLATE, reels=sorted_reels)
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
