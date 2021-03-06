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
def toppage():
    # user_data.pklが存在しない時、空のファイルを作成する
    if not os.path.isfile('user_data.pkl'):
        session.pop("user_id", None)
        save_pickle({}, 'user_data.pkl')
    return render_template('toppage.html')


@app.route('/index')
def index():
    if "user_id" in session:
        # ユーザIDをセッションから取得
        user_id = session["user_id"]


        # ユーザデータの保存するファイルから辞書を取得
        dic = load_pickle('user_data.pkl')

        # ユーザIDをキーとして辞書からユーザ名と努力量を取得
        user_data = dic[user_id]
        user_name = user_data[0]
        effort = user_data[1]

        # 努力量をifで分岐させ、stateを定義

        feeling="_normal"
        state=identify(effort,feeling)
        

        return render_template('index.html', name=user_name, state=state, user_id=user_id)

    else:
        # 仮としてセッション情報がないユーザはsignupにredirect
        # todo: 新規登録とログインが選べるページへの遷移
        return redirect(url_for("toppage"))


# 努力量をPOSTした時の処理
@app.route("/index", methods=['post'])
def effort():
    # 入力された努力量
    effort_today = int(request.form["effort"])

    # ユーザIDをセッションから取得
    user_id = session["user_id"]

    # ユーザデータの保存するファイルから辞書を取得
    dic = load_pickle('user_data.pkl')


    # ユーザIDをキーとして辞書からユーザ名と努力量を取得
    user_data = dic[user_id]
    user_name = user_data[0]

    #otama_chanの機嫌を決める
    if effort_today<20 and not effort_today%3:
      feeling="_angry"
    elif effort_today<20 and effort_today%3:
      feeling="_angry_ribbon"
    elif 20<=effort_today<60 and not effort_today%3:
      feeling="_normal"
    elif 20<=effort_today<60 and  effort_today%3:
      feeling="_normal_ribbon"
    elif 60<=effort_today<80:
      feeling="_laugh"
    else:
      feeling="_laugh_ribbon"

    # 入力された努力量を今までの努力総量に加算し、辞書を更新する。
    dic[user_id][1] += effort_today
    effort = dic[user_id][1]

    # 計算しなおした努力総量を用いて、再度stateを定義する
    
    state=identify(effort,feeling)
    print(state)
    
    # 新しいdicでuser_data.pklを書き換え
    with open('user_data.pkl', 'wb') as f:
        pickle.dump(dic, f)


    return render_template('index.html', name=user_name, state=state, user_id=user_id)

def identify(effort,feeling):
    #卵の時 
    if effort < 200:
     state = "egg"
    #おたまじゃくし：1つ目の段階
    elif 200 <= effort < 450:
     state = "otama_phase1"+feeling
    #おたまじゃくし：２つ目の段階
    elif 450 <= effort < 600:
     state = "otama_phase2"+feeling
    #おたまじゃくし：３つ目の段階
    elif 600 <= effort < 750:
     state = "otama_phase3"+feeling
    #蛙
    else:
     state = "frog"
    return state

# 新規登録
@app.route('/signup')
def signup():
    status = request.args.get("status")

    # user_data.pklが存在しない時、空のファイルを作成する
    if not os.path.isfile('user_data.pkl'):
        save_pickle({}, 'user_data.pkl')

    return render_template('signup.html', status=status)


# sign upボタン後の処理
@app.route("/signup", methods=["post"])
def signup_post():

    # todo: IDおよび名前が空欄の場合の処理

    user_name = request.form["user_name"]
    user_id = request.form["user_id"]

    # ユーザデータの保存するファイルから辞書を取得
    dic = load_pickle('user_data.pkl')



    # IDをキーにユーザ名と努力量をリストとして保存
    if user_id not in dic:
        dic[user_id] = [user_name, 0]
        session["user_id"] = user_id

        save_pickle(dic, 'user_data.pkl')

        return redirect(url_for("index"))



    # 既に登録されているIDの場合
    else:
        return redirect(url_for("signup", status="user_already_exists"))




# 既存ユーザログイン
@app.route('/signin')
def signin():
    status = request.args.get("status")

    # user_data.pklが存在しない時、空のファイルを作成する
    if not os.path.isfile('user_data.pkl'):
        save_pickle({}, 'user_data.pkl')

    return render_template('signin.html', status=status)

# sign inボタン後の処理
@app.route('/signin', methods=["post"])
def signin_post():

    # todo: IDが空欄の場合の処理

    # signin.htmlのフォームから user_id を受け取る
    user_id = request.form["user_id"]

    # ユーザデータを保存するファイルから辞書を取得
    dic = load_pickle('user_data.pkl')


    # IDが登録されている場合セッション情報にユーザIDを登録しredirect
    if user_id in dic:
        session["user_id"] = user_id
        return redirect(url_for("index"))
    # IDが未登録の場合
    else:
        return redirect(url_for("signin", status="user_not_found"))



# ログアウト
@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("toppage"))


#開発用
@app.route("/debug")
def debug():
    user_name = 'hogehoge'
    state = "frog"
    return render_template("index.html",name=user_name, state=state)


@app.route("/dic")
def verify_dic():
    dic = load_pickle('user_data.pkl')
    print(dic)
    return redirect(url_for("toppage"))


def save_pickle(dic, path):
    with open(path, 'wb') as f:
        pickle.dump(dic, f)

def load_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)
