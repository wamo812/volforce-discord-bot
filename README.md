# volforce-discord-bot
ﾇｫをDiscordに投稿するだけのプログラム

## デモ
<img width="724" alt="スクリーンショット 2021-05-19 1 34 15" src="https://user-images.githubusercontent.com/47220340/118690967-8e05da80-b843-11eb-9eea-ca644e4e5d21.png">

## 動作環境
- mac OS X 10.14.6
- Python 3.7.3

## 機能

- ﾇｫをお好きなDiscordチャンネルに投稿してくれる

## セットアップ
### ログイン情報の設定
環境変数にログイン用のメールアドレスとパスワードを設定
下記内容を`bash_profile`やら`zsh_profile`やらに追記  
（適宜自分のものに置き換えてください）
```
$ export SDVX_MAIL=hogehoge@fugamail.com
$ export SDVX_PASSWORD=pokopoko
```
(追記後、sourceコマンドで追記したファイルを読み直すのをお忘れなく)

設定できたことを念の為確認
```
$ echo $SDVX_MAIL
hogehoge@fugamail.com
$ echo $SDVX_PASSWORD
pokopoko
```

### webhookのURLとﾇｫ取得対象のIDを`values.py`に設定
参考：[webhookURLの取得方法（公式リファレンス）](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
```
#送信先
WEBHOOK_URL = 'https://discord.com/api/webhooks/hogehoge/fugafuga'

#ﾇｫ取得対象IDリスト
ID_LIST = [
    'SV-XXXX-YYYY',
    'SV-ZZZZ-0000'
]
```

## 実行手順

```
$ python iemuchi.py
```
※モジュールないよって言われたらpipしてください(私は`pipenv`使ってます)  
※`chromedriver`のバージョンの関係で動かない場合は拾ってきてください  
※mac以外動かないかも

## ライセンス
よくわかってないので設定してないですすみません...勝手に使っても怒らないです

## 作者
TM

## 要望
こういう機能欲しい！みたいな要望思いつきましたらぜひ言ってください

## TODO
- [ ] コンテナイメージ化したい