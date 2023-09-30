# API

## /api/gachal (POST)
### 想定されるリクエスト
- 認証は必要ない
- 基本データ構造
    ```
    {
        "contents": ["a", "b", "c"],
        "extraction_num": 2,
        "same": true
    }
    ```
    - `contents`
        - required
        - list
        - ガチャの中身（コンテンツ）
    - `extraction_num`
        - int
            - default: len(contents)
                - ソート
            - 1なら抽出
        - 抽出するコンテンツの数
    - `same`
        - boolean
            - default: false
        - 重複の有無の選択
            - 有: true, 無: false
        - trueの場合　`extraction_num`　が必須となる。
        - 抽出モードなら `false` とする必要がある。

- `content` (`contents` の中身)のデータ構造
    - dict
    ```
    {
        "name": "a",
        "weight": 2
    }
    ```
    - `name`
        - コンテンツとして扱う要素
    - `weight`
        - 排出率
            - 数字が大きい方が出やすくなる
    - それ以外
        - `content` の中身については触れない。
