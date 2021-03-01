# ！/usr/bin/env python
from flask import Flask, render_template, request
from gevent import pywsgi

# app = Flask(__name__, template_folder='templates')
app = Flask(__name__)


@app.route('/')
def Wandering_boy_Home():
    # return render_template('Personal-home-page/index.html')
    return render_template('Personal-home-page/index.html')


@app.route('/personal')
def Wandering_boy_brief_introduction():
    return render_template('Personal-home-page/Personal profile/index.html')


@app.route('/blog')
def Wandering_boy_blog():
    return render_template('blog/index.html')


@app.route('/wangdan/<int:id>')
def index(id=520):
    if id == 520:
        return render_template('wang_dan_birthday/page/index.html')
    if id == 1314:
        return render_template('wang_dan_birthday/page/yanhua.html')
    else:
        return render_template('wang_dan_birthday/page/index.html')


@app.route('/wangdan/1314')
def yanhua():
    return render_template('wang_dan_birthday/page/yanhua.html')


@app.route('/wangdan')
def birthday_home():
    return render_template('wang_dan_birthday/page/dangao.html')


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 80), app)
    server.serve_forever()
