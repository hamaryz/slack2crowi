# slack2crowi
SlackのメッセージをWikiツールであるCrowi上に登録するツール  
  
無料版のSlackの場合、メッセージ数が1万件を超えるとメッセージが削除されてしまうため、  
Wiki上に保存するためのツールを作りました。
「投稿日、投稿者名、投稿内容」が登録されます。

# how to use
1. コードをローカルにクローンする
```
git clone https://github.com/hamaryz/slack2crowi.git 
cd slack2growi
```

2. APIキーなどを登録する(setup.pyを利用)
```
python setup.py
input slack token: xxxxxxxx              # SlackのAPIキーを入力
input crowi token: xxxxxxxx              # CrowiのAPIキーを入力する
input crowi URL(including http or https): htts://example.com   # CrowiのURLを入力する
```

3. Slackのチャネル名を指定して実行する
```
python slack2crowi.py -n [Slack Channel Name]
```

# Output
/\[Slack Channel Name\]のパスにSlackのメッセージが登録されます
