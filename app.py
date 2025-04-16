from flask import Flask, request, render_template_string

app = Flask(__name__)

def get_top_reels(keyword):
    dummy_data = [
        {
            'thumbnail': 'https://via.placeholder.com/300x300?text=Reel1',
            'account': 'foodie_girl',
            'views': 125000,
            'likes': 3100,
            'date': '2025.04.10',
            'url': 'https://www.instagram.com/reel/sample1'
        },
        {
            'thumbnail': 'https://via.placeholder.com/300x300?text=Reel2',
            'account': 'seongsu_eats',
            'views': 98000,
            'likes': 2100,
            'date': '2025.04.09',
            'url': 'https://www.instagram.com/reel/sample2'
        }
    ]
    return sorted(dummy_data, key=lambda x: x['views'], reverse=True)

html_template = """
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>인스타 릴스 인기 콘텐츠</title>
  <style>
    body { font-family: sans-serif; background: #f9f9f9; padding: 10px; }
    .card { background: #fff; border-radius: 10px; box-shadow: 0 2px 6px rgba(0,0,0,0.1); margin-bottom: 16px; overflow: hidden; }
    .thumb { width: 100%; height: auto; }
    .info { padding: 10px; }
    .info h3 { font-size: 16px; margin: 4px 0; }
    .info p { margin: 0; font-size: 14px; color: #666; }
    .link { color: #007bff; text-decoration: none; font-weight: bold; }
  </style>
</head>
<body>
  <h2>#{{ keyword }} 릴스 인기 콘텐츠</h2>
  {% for item in reels %}
  <div class="card">
    <img class="thumb" src="{{ item.thumbnail }}" alt="썸네일">
    <div class="info">
      <h3>@{{ item.account }}</h3>
      <p>조회수: {{ '{:,}'.format(item.views) }} · 좋아요: {{ item.likes }} · 게시일: {{ item.date }}</p>
      <a class="link" href="{{ item.url }}" target="_blank">Instagram에서 보기</a>
    </div>
  </div>
  {% endfor %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        keyword = request.form['keyword']
        reels = get_top_reels(keyword)
        return render_template_string(html_template, keyword=keyword, reels=reels)
    return '''
        <form method="POST">
            <label>키워드 입력: </label>
            <input type="text" name="keyword" placeholder="예: 성수맛집">
            <input type="submit" value="검색">
        </form>
    '''

if __name__ == '__main__':
    app.run()
