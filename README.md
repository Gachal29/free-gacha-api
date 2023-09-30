# free-gacha-api

## 開発環境構築
- プロジェクトをcloneする
```
git clone git@gihtub.com:Gachal29/free-gacha-api.git
```

- venvを有効化する
```
cd free-gacha-api
python3.9 -m venv venv
source venv/bin/activate
```

- モジュールをインストールする
```
pip install -U pip # 必要があれば
pip install -r requirements.txt -r requirements-dev.txt
```

- runserverの起動
```
python manage.py runserver
```
