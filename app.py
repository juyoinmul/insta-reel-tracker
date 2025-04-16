from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        keyword = request.form['keyword']
        return f"<h2>검색한 키워드: {keyword}</h2>"
    return '''
        <form method="POST">
            <input type="text" name="keyword" placeholder="성수맛집 입력">
            <input type="submit" value="검색">
        </form>
    '''

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
