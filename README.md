<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="97.5" height="28" role="img" aria-label="DJANGO">
  <title>DJANGO</title>
  <g shape-rendering="crispEdges">
    <rect width="97.5" height="28" fill="#092e20"/>
  </g>
  <g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="100">
    <image x="9" y="7" width="14" height="14"/>
    <text transform="scale(.1)" x="587.5" y="175" textLength="535" fill="#fff" font-weight="bold">DJANGO</text>
  </g>
</svg>
![https___img shields io_badge_-Django-092E20](https://github.com/hash1o/MyBooksWeb/assets/136239147/bff037a9-b196-4e69-8dd2-6bddcfd440a7)

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
