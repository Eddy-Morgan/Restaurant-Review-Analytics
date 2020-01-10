from flask import Flask,render_template, request
from review import analyze
from flask_bootstrap import Bootstrap
import json


app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyse')
def analyse():
    average_ratings, competition = analyze()
    return render_template('result.html', ratings=average_ratings,top_competition=competition)

if __name__ == '__main__':
    app.run(debug=True,port='5000')