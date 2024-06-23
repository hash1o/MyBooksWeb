# MyBooksWeb

アカウントごと、本にメモを追加することができます。

私が所有しているエンジニア本が多くなってしまい、本に対するメモを残したく、Webアプリケーションを作成しました。

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

SQLite3 (開発環境)

PostgreSQL (本番環境)

Google Books APIs

nginx (本番環境)


## 動作を確認する場合は、以下の作業を行ってください


### ① secretsフォルダの作成 .env.devを作成

MyBooksWeb/secrets/.env.dev

### ②.env.devの内容

SECRET_KEY=MojihaNandemoii!!

DEBUG=True

ALLOWED_HOSTS=*

### ③パッケージのインストール (仮想環境は各自で構築してください)

ターミナル上で入力してください

pip install -r requirements.txt


### ④db作成

ターミナル上で入力してください



python manage.py makemigrations books

python manage.py migrate


### ⑤スーパーユーザの作成

ターミナル上で入力してください



python manage.py createsuperuser


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

アカウントごと オススメ本の紹介

