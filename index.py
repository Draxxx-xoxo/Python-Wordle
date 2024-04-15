from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/games')
def hello():
    return render_template('games.html')