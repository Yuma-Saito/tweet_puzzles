
# Twitterデータからパズル情報を取得するスクリプト

2021/01/24 Subaru Saito

---

## なにこれ

Twitterのデータから出題パズルデータのみを抜き出してテキスト形式で出力するスクリプトです。<br>
テキスト形式で出したあとはJavaScript使ってHTML化するなり解析するなりなんなりしてください。<br>
今のところは「ぱずぷれ」「puzzlink」のURLを含むもののみを抽出します。<br>
「penpa-edit」とか他のpuzzlinkフォークには未対応です。<br>
<br>
現在のバージョンでは、日付とパズル名、サイズ、URLを日付が古い順に取得してきます。<br>
将来的には画像内容とかpenpa-edit対応とかもしたい。<br>

### 注意

Twitter APIの仕様変更により`tweet.js`のデータフォーマットが知らぬ間に変わる可能性があり、<br>
そうなると使えなくなる可能性が高いです。そこはご了承ください。<br>
著者環境では2020/10/25時点でのTwitterデータで動作を確認しております。<br>


---
## 使い方

### 準備

1. python3をインストールしてください
  - Windows : [ここらへんを参考に](https://www.python.jp/install/windows/install.html)
  - macOS   : [ココらへんを参考に](https://qiita.com/ms-rock/items/72b8f1abc661c539bb09)
  - Ubuntu  : `sudo apt install python3`

2. Twitterデータをダウンロードします。
  - [Twitterデータのダウンロード方法](https://help.twitter.com/ja/managing-your-account/how-to-download-your-twitter-archive)

3. 何日か待つとメールでzip形式のデータをもらえます。

4. zipを解答します。

5. `data/tweet.js` に全ツイートデータがはいっています。
  - `tweet.js`の最初の一行を以下のように編集して正式なJSONフォーマットに直します。
  - （愚痴：なんでこれ最初からJSON形式にしてくれないんですかね）

6. ここにある`tweet_puzzles.py`をダウンロードして、`tweet.js`と同じフォルダに置きます。

7. ターミナルを開いて`tweet_filter.py`を置いたディレクトリに行きます。

これで準備完了です。


### 使い方

今の所オプションはないです。
そのうちオプションをいろいろつけれるようにしたいですねえ。

- `python3 tweet_puzzles.py > puzzle.txt`



---
## バージョン

- v1.0: とりあえず抽出できるところまで。UIとか一切関係なし。
