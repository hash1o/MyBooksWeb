# MyBooksWeb

アカウントごと、本にメモを追加することができます。

## 使用技術

Django 5.0.6

Python 3.11

SQLite3

## できること

### ・本を検索する

### ・本にメモを記載する

### ・メモを記載したことのある本を一覧で表示できる

### ・アカウント作成

### ・ログイン

### ・ログアウト

### ・プロファイル登録

## 動作を確認する場合は、以下の作業を行ってください

### .env.devを作成

MyBooksWeb/secrets/.env.dev

### .env.devの内容

SECRET_KEY=｛各自ランダムな文字列を入力してください｝

DEBUG=True

ALLOWED_HOSTS=*

### python仮想環境

#### pip install -r requirements.txt

### db作成

#### python manage.py makemigrations books

#### python manage.py migrate

### スーパーユーザの作成

#### python createsuperuser

名前入力

メールアドレス入力

パスワード入力

### 実行

#### python manage.py runserver

http://127.0.0.1:8000/ へアクセス

