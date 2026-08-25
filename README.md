# 天気予報 API

FastAPI を使用したシンプルな天気予報 API です。
`/weather/tokyo` にアクセスすると、東京のランダムな天気予報文字列を返します。

## 技術スタック

- **言語**: Python 3.12+
- **フレームワーク**: FastAPI
- **パッケージ管理**: uv
- **テスト**: pytest

## プロジェクト構成

```
.
├── src/
│   └── test20260825_02/
│       ├── __init__.py
│       └── main.py        # FastAPI アプリケーション本体
├── tests/
│   └── test_main.py       # pytest テストコード
├── pyproject.toml
└── README.md
```

## セットアップ

```bash
# 依存パッケージのインストール
uv sync
```

## サーバーの起動

```bash
uv run uvicorn test20260825_02.main:app --reload
```

サーバー起動後、以下の URL にアクセスできます:

- **天気予報エンドポイント**: http://localhost:8000/weather/tokyo
- **API ドキュメント (Swagger UI)**: http://localhost:8000/docs
- **API ドキュメント (ReDoc)**: http://localhost:8000/redoc

## API の使用例

```bash
curl http://localhost:8000/weather/tokyo
```

レスポンス例:

```json
{"forecast": "東京の天気: 晴れ、最高気温32℃、最低気温18℃"}
```

## テストの実行

```bash
uv run pytest tests/ -v
```
