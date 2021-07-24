# gitのインストール
下のコマンドでgitが端末に入っているかを確認
```
git --version
```
## 入ってなかった場合
ターミナルを開く。下のコマンドを実行する。
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
下のコマンドでパソコンにgitをインストールする。
```
brew install git
```
再度このコマンドで正しくインストールできたか確認。
```
git --version
```

# projectのリポジトリをクローン
```
git clone https://github.com/sk161717/hackathon.git
```
上記のコマンドが成功したら、自分のフォルダにhackathonというフォルダがあることを確認。

# 編集してpushするときの一連のコマンド
```
git checkout master(マスターに移動する)
git branch -a(masterにいることを確認する)
git pull
git checkout -b XXX(やる作業に合わせて適当に自分でbranch名を考えて設定する)
~~編集作業~~
git add .
git commit -m "やった内容を書く"
git push -u origin XXX(上のXXXと同じ)
(ブラウザ上でgithubを開いてcompare& create pull requestをおしてrequestを作る。作ったら報告)


```
とりあえず作業するときは
- 自分がどのブランチにいるか
- ちゃんと最新のmasterをpullしてきたか
を確認する

# 実際にサービスの画面がどうなってるかの見方
```
(hackathonディレクトリで)python main.py
* Serving Flask app 'app.index' (lazy loading)
* Environment: production
 WARNING: This is a development server. Do not use it in a production deployment.
 Use a production WSGI server instead.
* Debug mode: off
* Running on http://localhost:8000/ (Press CTRL+C to quit)
↑こんな感じのが出てくるはず
```
ブラウザで
http://localhost:8000/ ->index.htmlが表示される

http://localhost:8000/signup ->signup.htmlが表示される

http://localhost:8000/signin ->signin.htmlが表示される

