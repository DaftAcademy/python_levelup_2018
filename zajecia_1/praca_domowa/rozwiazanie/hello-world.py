from datetime import datetime

from flask import Flask, request
from user_agents import parse
app = Flask(__name__)
app.counter = 0


@app.route('/')
def hello():
    return "Hello, World!"


@app.route('/now')
def now():
    # Tutaj może się pojawić problem, że zwracany element nie jest "callable"
    # Można go rozwiązać w prosty sposób formatując wartość wyjściową.
    return str(datetime.utcnow())


@app.route('/counter')
def counter():
    app.counter += 1
    return str(app.counter)


@app.route('/user-agent')
def ua():
    ua = parse(request.headers.get('User-Agent'))
    return str(ua)
