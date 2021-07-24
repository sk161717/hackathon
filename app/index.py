# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, session, redirect, url_for, request
import pickle
from app import static

app = Flask(__name__)
app.secret_key = 'hackathon0724'
app.register_blueprint(static.app)


#ルーティングはここに書く
#cookie使ってlogin認証する

@app.route('/')
def index():
    if "user_id" in session:
        # ユーザIDをセッションから取得
        user_id = session["user_id"]

        # ユーザデータの保存するファイルから辞書を取得
        with open('user_data.pkl', 'rb') as f:
            dic = pickle.load(f)

        try:
            user_name = dic[user_id][0]
        except Exception as e:
            user_name = 'debug'
            print(e)

        state = 'egg'





        return render_template('index.html', name=user_name, state=state, user_id=user_id)

    else:
        # 仮としてセッション情報がないユーザはsignupにredirect
        # todo: 新規登録とログインが選べるページへの遷移
        return redirect(url_for("signup"))



# 新規登録
@app.route('/signup')
def signup():
    status = request.args.get("status")
    return render_template('signup.html', status=status)


# フォーム記入後
@app.route("/signup", methods=["post"])
def signup_post():

    # todo: IDおよび名前が空欄の場合の処理

    user_name = request.form["user_name"]
    user_id = request.form["user_id"]

    # ユーザデータの保存するファイルから辞書を取得
    with open('user_data.pkl', 'rb') as f:
        dic = pickle.load(f)


    # IDをキーにユーザ名と努力量をリストとして保存
    if user_id not in dic:
        dic[user_id] = [user_name, 0]
        session["user_id"] = user_id

        with open('user_data.pkl', 'wb') as f:
            pickle.dump(dic, f)

        return redirect(url_for("index"))



    # 既に登録されているIDの場合
    else:
        return redirect(url_for("signup", status="user_already_exists"))




# 既存ユーザログイン
@app.route('/signin')
def signin():
    status = request.args.get("status")
    return render_template('signin.html', status=status)


@app.route('/signin', methods=["post"])
def signin_post():

    # todo: IDが空欄の場合の処理

    # signin.htmlのフォームから user_id を受け取る
    user_id = request.form["user_id"]

    # ユーザデータを保存するファイルから辞書を取得
    with open('user_data.pkl', 'rb') as f:
        dic = pickle.load(f)

    # IDが登録されている場合セッション情報にユーザIDを登録しredirect
    if user_id not in dic:
        session["user_id"] = user_id
        return redirect(url_for("index"))
    # IDが未登録の場合
    else:
        return redirect(url_for("signin", status="user_not_found"))


# ログアウト
@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("index"))

#開発用
@app.route("/debug")
def debug():
    user_name = 'hogehoge'
    state = 'egg'
    return render_template("index.html",name=user_name, state=state)
