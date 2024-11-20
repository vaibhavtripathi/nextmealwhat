from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return '<h1>login page</h1>'
