# -*- coding: utf-8 -*-
import os
from flask import Flask
from app import static

app = Flask(__name__)
app.register_blueprint(static.app)


#ルーティングはここに書く
#cookie使ってlogin認証する

@app.route('/')
def index():
  return static.app.send_static_file('index.html')

@app.route('/signup')
def signup():
    return static.app.send_static_file('signup.html')

@app.route('/static/login.css')
def login_css():
    return static.app.send_static_file('login.css')

@app.route('/static/main.js')
def main_js():
    return static.app.send_static_file('main.js')