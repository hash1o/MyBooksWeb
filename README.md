# MyBooksWeb

アカウントごと、本にメモを追加することができます。



## できること

### ・本を検索する

### ・本にメモを記載する

### ・メモを記載したことのある本を一覧で表示できる

### ・アカウント作成

### ・ログイン

### ・ログアウト

### ・プロファイル登録




## 使用技術

Django 5.0.6

Python 3.11

SQLite3

Google Books APIs



## 動作を確認する場合は、以下の作業を行ってください


### ①.env.devを作成

MyBooksWeb/secrets/.env.dev

### ②.env.devの内容

SECRET_KEY=｛各自ランダムな文字列を入力してください｝

DEBUG=True

ALLOWED_HOSTS=*

### ③python仮想環境


pip install -r requirements.txt


### ④db作成


python manage.py makemigrations books

python manage.py migrate


### ⑤スーパーユーザの作成


python createsuperuser


名前入力

メールアドレス入力

パスワード入力

### ⑥実行


python manage.py runserver


http://127.0.0.1:8000/ へアクセス




## 今後・追加予定 (順不同)

PostgreSQLへ移行

AWS nginx デプロイ

アカウントの名前、メアド、パスワード変更機能

Web上のマイライブラリ 個別 削除

