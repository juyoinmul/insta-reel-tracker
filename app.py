from flask import Flask, render_template, request

app = Flask(__name__)

# 더미 데이터
reels_data = [
    {
        "account": "@foodie_girl",
        "views": 125000,
        "likes": 3100,
        "comments": 120,
        "date": "2025.04.10",
        "thumbnail": "https://via.placeholder.com/100",
        "url": "https://instagram.com/reel/abc123"
    },
    {
        "account": "@seongsu_eats",
        "views": 98000,
        "likes": 2100,
        "comments": 88,
        "date": "2025.04.09",
        "thumbnail": "https://via.placeholder.com/100",
        "url": "https://instagram.com/reel/def456"
    }
]

@app.route("/", methods=["GET", "POST"])
def index():
    keyword = request.form.get("keyword", "")
    sort_by = request.form.get("sort", "likes")  # 기본 정렬은 좋아요순

    sorted_data = sorted(reels_data, key=lambda x: x[sort_by], reverse=True)

    return render_template("index.html", keyword=keyword, reels=sorted_data, sort_by=sort_by)

if __name__ == "__main__":
    app.run(debug=True)
