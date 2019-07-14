# graph_tool

残
・クラス化
・JSON化
・引数対応


* requirements.txtを読み込んで依存関係ライブラリをインストールする(pipまたはpip3は各自でinstallしてください)
```
pip3 install -r requirements.txt
```

* pipenvも使ってみた

```
pip3 install pipenv
```

```
pipenv install
```
※requirements.txtを見て、Pipfile, Pipfile.lockを作成してくれるみたい


* 逆に

```
pipenv lock -r > requires.txt
```
でrequirements.txtファイルを作成しておき、

```
pip3 istall -r requires.txt
```
でインストールするのでも良い
