<div id="top"></div>

## 使用技術一覧
<p style="display: inline">
<img src="https://img.shields.io/badge/-Python-3776AB.svg?logo=python&style=plastic">
<img src="https://img.shields.io/badge/-Flask-000000.svg?logo=flask&style=plastic">
</p>

## 使用した教材
Udamy
├── 初心者でも安心！Python + Flask によるビジネスに役立つWebアプリ開発入門（Bootstrap 5）
├──はじめてのPythonプログラミング入門
<!-- 成果物 -->
## 成果物について

Flaskを利用しての会社ホームページの作成

## 環境

| 言語・フレームワーク  | バージョン |
| --------------------- | ---------- |
| Python                | 3.10.14    |
| Flask                 | 2.0.3      |
| SQLite                | 3.45.3     |
| Bootstrap             | 5.0.2      |

その他Anacondaとvscodeを使用しました。

<p align="right">(<a href="#top">トップへ</a>)</p>

## ディレクトリ構成

<!-- Treeコマンドを使ってディレクトリ構成を記載 -->

❯ Flaskapp
├── app.py
├── init_db.py 
**company_blog**
  ├── **__pycache__**
  │   ├──__init__.cpython-310.pyc
  │   └──models.cpython-310.pyc
  ├── **error_pages**
  |   ├── __pycache__
  │   │   ├──__init__.cpython-310.pyc
  │   │   └──models.cpython-310.pyc
  |   ├──__init__.py
  |   └──handlers.py
  ├── **main**
  |   ├── __pycache__
  │   │   ├──__init__.cpython-310.pyc
  │   │   ├──forms.cpython-310.pyc
  │   │   ├──image_handler.cpython-310.pyc
  │   │   └──views.cpython-310.pyc
  │   ├──__init__.py
  │   ├── forms.py
  │   ├── views.py
  │   └── image_handler.py
  ├── **static**
  │   ├──
  │   └──
  ├── **templates**
  |   ├── error_pages
  │   │   ├──403.html
  │   │   └──404.html
  |   ├── users
  │   │   ├──account.html
  │   │   ├──login.html
  │   │   ├──register.html
  │   │   └──user_maintenance.html
  │   ├──formhelpers.html
  │   ├── base.html
  │   ├── blog_category.html
  │   ├── blog_maintenance.html
  │   ├── blog_post.html
  │   ├── category_maintenance.html
  │   ├── create_post.html
  │   ├── index.html
  │   ├── info.html
  │   ├── inquiry_maintenance.html
  │   ├── inquiry.html
  │   ├──__init__.py
  │   ├── forms.py
  │   ├── views.py
  │   └── image_handler.py
  └── **users**
      ├── __pycache__
      │   ├──__init__.cpython-310.pyc
      │   ├──forms.cpython-310.pyc
      │   └──views.cpython-310.pyc
      ├──__init__.py
      ├── forms.py
      └── views.py

<p align="right">(<a href="#top">トップへ</a>)</p>

## 動作確認
・コマンドプロンプトにてpython init_db.pyを行いdb作成
・python app.pyを行いhttp://127.0.0.1:5000/にアクセス
・一般ユーザーとして確認。http://127.0.0.1:5000/loginでdbに入れたユーザーでログイン可能。投稿フォームはこちらで確認。
