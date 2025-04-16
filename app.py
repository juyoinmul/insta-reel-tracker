from flask import Flask, request, render_template_string

app = Flask(__name__)

MOCK_REELS = [
    {
        "thumbnail": "https://via.placeholder.com/150",
        "account": "@foodie_girl",
        "views": "125,000",
        "likes": "3,100",
        "date": "2025.04.10",
        "url": "https://www.instagram.com/reel/abc123"
    },
    {
        "thumbnail": "https://via.placeholder.com/150",
        "account": "@seongsu_eats",
        "views": "98,000",
        "likes": "2,100",
        "date": "2025.04.09",
        "url": "https://www.instagram.com/reel/def456"
    },
] * 50  # 100개로 복제

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>릴스 인기 콘텐츠</title>
    <style>
        body { font-family: sans-serif; background: #f9f9f9; padding: 20px; }
        form { margin-bottom: 20px; }
        input[type=text] { padding: 8px; width: 200px; }
        input[type=submit] { padding: 8px 16px; }
        .card { background: #fff; border-radius: 8px; padding: 12px; margin-bottom: 16px; display: flex; gap: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }
        .thumb { width: 100px; height: 100px; object-fit: cover; border-radius: 6px; }
        .info { flex-grow: 1; }
        .account { font-weight: bold; color: #333; }
        .meta { color: #666; font-size: 14px; margin-top: 4px; }
        a { color: #1e88e5; font-size: 14px; text-decoration: none; }
    </style>
</head>
<body>
    <form method="POST">
        <input type="text" name="keyword" placeholder="예: 성수맛집">
        <input type="submit" value="검색">
    </form>

    {% if keyword %}
    <h2>#{{ keyword }} 릴스 인기 콘텐츠</h2>
    {% for item in reels %}
        <div class="card">
            <img class="thumb" src="{{ item.thumbnail }}" alt="썸네일">
            <div class="info">
                <div class="account">{{ item.account }}</div>
                <div class="meta">조회수: {{ item.views }} · 좋아요: {{ item.likes }} · 게시일: {{ item.date }}</div>
                <a href="{{ item.url }}" target="_blank">Instagram에서 보기</a>
            </div>
        </div>
    {% endfor %}
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    keyword = None
    if request.method == "POST":
        keyword = request.form["keyword"]
    return render_template_string(HTML_TEMPLATE, keyword=keyword, reels=MOCK_REELS)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
