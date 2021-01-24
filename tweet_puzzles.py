import json, sys, time


def main():
    # tweet.jsファイルの読み込み
    filename = "tweet.js"
    with open(filename, "r") as f:
        tweets = json.load(f)

    # 個々のツイートの処理
    puzzles = []
    for tw_obj in tweets:
        tw = tw_obj['tweet']

        # 日付を取得（フォーマットを変換）
        tw_date = time.strftime('%Y/%m/%d', time.strptime(
            tw['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))

        # パズル関係の情報があれば取得
        hashtags = []
        urls = []
        imgurls = []
        if 'hashtags' in tw['entities']:
            for thash in tw['entities']['hashtags']:
                hashtags.append(thash['text'])
        if 'urls' in tw['entities']:
            for turl in tw['entities']['urls']:
                urls.append(turl['expanded_url'])
        if 'media' in tw['entities']:
            for imgurl in tw['entities']['media']:
                imgurls.append(imgurl['media_url_https'])

        # 他の人のRTは除外
        retweeted = (len(tw['entities']['user_mentions']) > 0)
        if not retweeted:
            # ぱずぷれ/puzzlinkのURLのみ取得
            valid_urls = get_valid_urls(urls)
            for valid_url in valid_urls:
                valid_url['date'] = tw_date
                valid_url['contents'] = tw['full_text']
                puzzles.append(valid_url)


    # 集計結果表示
    puzzles.sort(key = lambda x: x['date'])
    print_puzzles(puzzles)



# ぱずぷれ/puzzlinkの有効なURLを抽出
# 
# @param list urls: URLのリスト
# @returns list 有効なURLのインデックス。なければ空リスト
def get_valid_urls(urls):
    url_patterns = [
        'http://pzv.jp/p.html',
        'https://pzv.jp/p.html',
        'http://puzz.link/p',
        'https://puzz.link/p',
    ]

    valid_urls = []
    for url in urls:
        split_url = url.split('?')    # クエリ部分とURL本体を分ける
        if split_url[0] in url_patterns:
            url_parts = split_url[1].split('/')
            url_parts[0] = url_parts[0].replace('_edit', '')   # 編集モードを無効化
            urlinfo = {}
            urlinfo['url'] = split_url[0] + '?' + '/'.join(url_parts)
            urlinfo['name'] = url_parts[0]
            urlinfo['yoko'] = url_parts[1]
            urlinfo['tate'] = url_parts[2]
            # スラロームだけ slalom/d/10/10 みたいになっている
            if urlinfo['name'] == 'slalom':
                urlinfo['yoko'] = url_parts[2]
                urlinfo['tate'] = url_parts[3]

            valid_urls.append(urlinfo)

    return valid_urls



# パズルのリストを出力する
def print_puzzles(puzzles):
    for p in puzzles:
        print("{0},{1},{2} x {3},{4}".format(
            p['date'], puzname[p['name']], p['tate'], p['yoko'], p['url']))

    # print("総パズル数: {0}".format(len(puzzles)))




# ========================= パズル名の対応表 ==============================
puzname = {
    'nurikabe': 'ぬりかべ',
    'box': 'ボックス',
    'creek': 'クリーク',
    'mochikoro': 'モチコロ',
    'tasquare': 'たすくえあ',
    'kurotto': 'クロット',
    'nuribou': 'ぬりぼう',
    'tawa': 'たわむれんが',
    'lookair': 'るっくえあ',
    'mochinyoro': 'モチにょろ',
    'tapa': 'Tapa',
    'cave': 'バッグ',
    'bag': 'バッグ',
    'nurimisaki': 'ぬりみさき',
    'snake': 'Snake',
    'nonogram': 'ののぐらむ',
    'interbd': 'International Borders',
    'aqre': 'Aqre',
    'tilepaint': 'タイルペイント',
    'norinori': 'のりのり',
    'nurimaze': 'ぬりめいず',
    'lits': 'LITS',
    'shimaguni': '島国',
    'stostone': 'ストストーン',
    'paintarea': 'ペイントエリア',
    'chocona': 'チョコナ',
    'aquarium': 'アクアプレース',
    'heyawake': 'へやわけ',
    'hitori': 'ひとりにしてくれ',
    'kurodoko': '黒どこ',
    'usoone': 'ウソワン',
    'yajikazu': 'やじさんかずさん',
    'kurochute': 'クロシュート',
    'ayeheya': '∀人ヨHEYA',
    'slither': 'スリザーリンク',
    'mashu': 'ましゅ',
    'masyu': 'ましゅ',
    'yajilin': 'ヤジリン',
    'slalom': 'スラローム',
    'nagare': '流れるループ',
    'moonsun': '月か太陽',
    'country': 'カントリーロード',
    'onsen': '温泉めぐり',
    'mejilink': 'メジリンク',
    'angleloop': '鋭直鈍ループ',
    'doubleback': 'Double Back',
    'scrin': 'スクリン',
    'yajilin-regions': 'ヘヤジリン',
    'geradeweg': 'グラーデヴェグ',
    'castle': 'Castle Wall',
    'maxi': 'Maxi Loop',
    'midloop': 'ミッドループ',
    'balance': 'Balance Loop',
    'simpleloop': 'Simple Loop',
    'detour': 'Detour',
    'haisu': 'Haisu',
    'tapaloop': 'Tapa-Like Loop',
    'reflect': 'リフレクトリンク',
    'pipelink': 'パイプリンク',
    'loopsp': '環状線スペシャル',
    'nagenawa': 'なげなわ',
    'kouchoku': '交差は直角に限る',
    'ringring': 'リングリング',
    'icebarn': 'アイスバーン',
    'pipelinkr': '帰ってきたパイプリンク',
    'barns': 'バーンズ',
    'icelom': 'アイスローム',
    'icelom2': 'アイスローム2',
    'numlin': 'ナンバーリンク',
    'wblink': 'シロクロリンク',
    'kusabi': 'クサビリンク',
    'arukone': 'アルコネ',
    'hashikake': '橋をかけろ',
    'hashi': '橋をかけろ',
    'firefly': 'ホタルビーム',
    'ichimaga': 'イチマガ',
    'ichimagam': '磁石イチマガ',
    'ichimagax': '一回曲がって交差もするの',
    'amibo': 'あみぼー',
    'herugolf': 'ヘルゴルフ',
    'kaero': 'お家に帰ろう',
    'yosenabe': 'よせなべ',
    'armyants': 'ぐんたいあり',
    'bonsan': 'ぼんさん',
    'heyabon': 'へやぼん',
    'rectslider': '四角スライダー',
    'sato': 'さとがえり',
    'satogaeri': 'さとがえり',
    'shikaku': '四角に切れ',
    'bdblock': 'ボーダーブロック',
    'fivecells': 'ファイブセルズ',
    'sashigane': 'さしがね',
    'nawabari': 'なわばり',
    'triplace': 'トリプレイス',
    'fourcells': 'フォーセルズ',
    'aho': 'アホになり切れ',
    'heteromino': 'ヘテロミノ',
    'dbchoco': 'ダブルチョコ',
    'compass': 'Compass',
    'araf': '相ダ部屋',
    'nikoji': 'NIKOJI',
    'tentaisho': '天体ショー',
    'kramma': '快刀乱麻',
    'kramman': '新・快刀乱麻',
    'shwolf': 'ヤギとオオカミ',
    'cbblock': 'コンビブロック',
    'loute': 'エルート',
    'tatamibari': 'タタミバリ',
    'fillmat': 'フィルマット',
    'usotatami': 'ウソタタミ',
    'yajitatami': 'ヤジタタミ',
    'kakuro': 'カックロ',
    'minarism': 'マイナリズム',
    'sukoro': '数コロ',
    'kakuru': 'カックル',
    'view': 'ヴィウ',
    'bosanowa': 'ボサノワ',
    'skyscrapers': 'ビルディングパズル',
    'kropki': 'Kropki',
    'easyasabc': 'ABCプレース',
    'doppelblock': 'Doppelblock',
    'sudoku': '数独',
    'fillomino': 'フィルオミノ',
    'symmarea': 'シンメトリーエリア',
    'ripple': '波及効果',
    'factors': '因子の部屋',
    'makaro': 'マカロ',
    'nanro': 'ナンロー',
    'cojun': 'コージュン',
    'renban': '連番窓口',
    'sukororoom': '数コロ部屋',
    'hanare': 'はなれ組',
    'kazunori': 'かずのりのへや',
    'meander': 'にょろにょろナンバー',
    'putteria': 'プッテリア',
    'toichika2': '遠い誓い2',
    'juosan': '縦横さん',
    'gokigen': 'ごきげんななめ',
    'tateyoko': 'タテボーヨコボー',
    'wagiri': 'ごきげんななめ・輪切',
    'walllogic': 'ウォールロジック',
    'curvedata': 'カーブデータ',
    'lightup': '美術館',
    'akari': '美術館',
    'goishi': '碁石ひろい',
    'shakashaka': 'シャカシャカ',
    'kinkonkan': 'キンコンカン',
    'hebi': 'へびいちご',
    'shugaku': '修学旅行の夜',
    'pencils': 'ペンシルズ',
    'tents': 'Tents',
    'mines': 'マインスイーパ',
    'hakoiri': 'はこいり○△□',
    'dosufuwa': 'ドッスンフワリ',
    'roma': 'ろーま',
    'toichika': '遠い誓い',
    'nondango': 'ノンダンゴ',
    'yinyang': 'しろまるくろまる',
    'starbattle': 'スターバトル',
}

if __name__ == "__main__":
    main()
