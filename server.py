from flask import Flask,render_template, request, redirect,url_for,session, flash
from review import analyze,ridlist
from flask_bootstrap import Bootstrap
import json
from sentiment_analysis import draw_wordcloud


app = Flask(__name__)
app.secret_key = 'un234nr98n439n#09!?'
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyse')
def analyse():
    rid=1
    if 'n' in session:
        n = session['n']
    else:
        n= 10
    average_ratings, competition = analyze(n)
    return render_template('result.html', ratings=average_ratings,top_competition=competition,rid=rid, n=n)

@app.route('/wordcloud',  methods=['GET', 'POST'])
def generateWorldCloud():
    if 'n' in session:
        n = session['n']
    else:
        n= 10
    average_ratings, competition = analyze(n)
    if request.method == 'POST':
        rid = request.form['rid']
        if int(rid) not in ridlist:
            flash(' Number out of range, please input again!')
            rid = 958
        draw_wordcloud(rid)
        return render_template('result.html', ratings=average_ratings,top_competition=competition,rid=rid, n=n)
    return render_template('result.html', ratings=average_ratings,top_competition=competition,rid=1, n=n)

@app.route('/topcount', methods=['GET', 'POST'])
def topCount():
    if 'n' in session:
        n = session['n']
    else:
        n= 10
    if request.method == 'POST':
        n = int(request.form['count'])
        if n not in ridlist:
            flash('Number out of range, please input again!')
            if 'n' in session:
                n = session['n']
            else:
                n= 10
        average_ratings, competition = analyze(n)
        session['n'] = n
        return render_template('result.html', ratings=average_ratings,top_competition=competition,rid=1, n=n)
    average_ratings, competition = analyze(n)
    return render_template('result.html', ratings=average_ratings,top_competition=competition,rid=1, n=n)


if __name__ == '__main__':
    app.run(debug=True,port='5000')