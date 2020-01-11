from flask import Flask,render_template, request, redirect,url_for
from review import analyze
from flask_bootstrap import Bootstrap
import json
from sentiment_analysis import draw_wordcloud


app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyse')
def analyse():
    rid=1
    average_ratings, competition = analyze()
    return render_template('result.html', ratings=average_ratings,top_competition=competition,rid=rid)

@app.route('/wordcloud',  methods=['GET', 'POST'])
def generateWorldCloud():
    average_ratings, competition = analyze()
    if request.method == 'POST':
        rid = request.form['rid']
        draw_wordcloud(rid)
        return render_template('result.html', ratings=average_ratings,top_competition=competition,rid=rid)
    return render_template('result.html', ratings=average_ratings,top_competition=competition,rid=1)

if __name__ == '__main__':
    app.run(debug=True,port='5000')