https://camo.qiitausercontent.com/ca8c7ac2357304fbbbf13b2bb9eacdabd78081cc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d446a616e676f2d3039324532302e7376673f6c6f676f3d646a616e676f267374796c653d666f722d7468652d6261646765

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
