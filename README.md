https://img.shields.io/badge/-Django-092E20.svg?logo=django&style=for-the-badge

# MyBooksWeb
本を追加できます

## 動作を確認する場合は、以下の作業を行ってください
MyBooksWeb/secrets/.env.dev を作成

### .env.devの内容
SECRET_KEY=｛各自ランダムな文字列を入力してください｝
DEBUG=True
ALLOWED_HOSTS=*

### python仮想環境
pip install -r requirements.txt

### db作成
python manage.py makemigrations books
python manage.py migrate

### スーパーユーザの作成
python createsuperuser
名前入力
メールアドレス入力
パスワード入力

### 実行
python manage.py runserver
http://127.0.0.1:8000/ へアクセス
