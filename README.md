<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="97.5" height="28" role="img" aria-label="DJANGO"><g shape-rendering="crispEdges"><rect width="97.5" height="28" fill="#092e20"/></g><g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="100"><image x="9" y="7" width="14" height="14" xlink:href="data:image/svg+xml;base64,PHN2ZyBmaWxsPSJ3aGl0ZXNtb2tlIiByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGl0bGU+RGphbmdvPC90aXRsZT48cGF0aCBkPSJNMTEuMTQ2IDBoMy45MjR2MTguMTY2Yy0yLjAxMy4zODItMy40OTEuNTM1LTUuMDk2LjUzNS00Ljc5MSAwLTcuMjg4LTIuMTY2LTcuMjg4LTYuMzIgMC00LjAwMiAyLjY1LTYuNiA2Ljc1My02LjYuNjM3IDAgMS4xMjEuMDUgMS43MDcuMjAzem0wIDkuMTQzYTMuODk0IDMuODk0IDAgMDAtMS4zMjUtLjIwNGMtMS45ODggMC0zLjEzNCAxLjIyMy0zLjEzNCAzLjM2NSAwIDIuMDkgMS4wOTYgMy4yMzYgMy4xMDkgMy4yMzYuNDMzIDAgLjc5LS4wMjUgMS4zNS0uMTAyVjkuMTQyek0yMS4zMTQgNi4wNnY5LjA5OGMwIDMuMTM0LS4yMjkgNC42MzgtLjkxNyA1LjkzNy0uNjM3IDEuMjQ5LTEuNDc4IDIuMDM5LTMuMjExIDIuOTA1bC0zLjY0NC0xLjczM2MxLjczMy0uODE1IDIuNTc0LTEuNTMgMy4xMDktMi42MjUuNTYxLTEuMTIxLjczOS0yLjQyMS43MzktNS44MzVWNi4wNTloMy45MjR6TTE3LjM5LjAyMWgzLjkyNHY0LjAyNkgxNy4zOXoiLz48L3N2Zz4="/><text transform="scale(.1)" x="587.5" y="175" textLength="535" fill="#fff" font-weight="bold">DJANGO</text></g></svg>

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
