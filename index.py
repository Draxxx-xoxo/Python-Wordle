from flask import Flask, render_template
from wonderwords import RandomWord

app = Flask(__name__)

def random_word():
    r = RandomWord()
    # Get a random word
    random_word = r.word(word_max_length=5, word_min_length=5)
    return random_word 

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/games')
def hello():
    return render_template('games.html', word=random_word())