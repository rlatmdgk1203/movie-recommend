from flask import Flask, render_template, request
from recommender import get_recommendations

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    recommended = []
    error = None
    if request.method == 'POST':
        title = request.form.get('movie_title')
        if title:
            recommended = get_recommendations(title)
            if not recommended:
                error = f"'{title}'에 대한 추천 결과가 없습니다."
    return render_template('index.html', recommended=recommended, error=error)

if __name__ == '__main__':
    app.run(debug=True)