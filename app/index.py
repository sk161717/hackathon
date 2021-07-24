# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, session, redirect, url_for
import pickle
from app import static

app = Flask(__name__)
app.register_blueprint(static.app)


#ルーティングはここに書く
#cookie使ってlogin認証する

@app.route('/')
def index():
    if "user_id" in session:
        # ユーザIDをセッションから受け取る
        user_id = session["user_id"]

        # バイナリファイルから辞書を受け取る
        with open('user_data.binaryfile', 'rb') as f:
            dic = pickle.load(f)


        # ①ユーザIDをキーにして辞書からユーザ名と努力量を受け取る
        # dic[ユーザID] = [ユーザ名, 努力量](リスト)
        # user_name = ###
        # effort = ###

        # ②effortの値に応じてカエルの状態を決める
        # ifで分岐
        # state = ###



        return render_template('index.html', name=user_name, state=state)

    else:
        # 仮としてセッション情報がないユーザはsignupにredirect
        # todo: 新規登録とログインが選べるページへの遷移
        return redirect(url_for("signup"))



# 新規登録
@app.route('/signup')
def signup():
    return render_template('signup.html')


# フォーム記入後
@app.route("/signup", methods=["post"])
def signup_post():

    user_name = request.form["user_name"]
    user_id = request.form["user_id"]

    # ユーザデータの保存するファイルから辞書を取得
    with open('user_data.binaryfile', 'rb') as f:
        dic = pickle.load(f)


    # IDをキーにユーザ名と努力量をリストとして保存
    if user_id not in dic:
        dic[user_id] = [user_name, 0]
        session["user_id"] = user_id

        with open('user_data.binaryfile', 'wb') as f:
            pickle.dump(dic, f)



    # 既に登録されているIDの場合
    else:
        return redirect(url_for("signup", status="user_already_exists"))




# 既存ユーザログイン
@app.route('/signin')
def signin():
    return render_template('signin.html')


@app.route('/signin', methods=["post"])
def signin_post():

    # signin.htmlのフォームから user_id を受け取る
    user_id = request.form["user_id"]

    # ユーザデータの保存するファイルから辞書を取得
    with open('user_data.binaryfile', 'rb') as f:
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
