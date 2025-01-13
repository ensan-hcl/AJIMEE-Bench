# AJIMEE-Bench (A Japanese Input Method Evaluation and Examination Benchmark)

このレポジトリはAJIMEE-Bench(味見ベンチ)の評価データを配置しています。

## ディレクトリ

### `JWTD_v2/v1`

[日本語Wikipedia入力誤りデータセット (v2)](https://nlp.ist.i.kyoto-u.ac.jp/?日本語Wikipedia入力誤りデータセット)をベースに構築したデータです。

**ライセンスは元データに準拠し、CC-BY-SA 3.0に従います**。

以下はデータサンプルです。

* `index`は元データにおける行番号を示します
* `context_text`は（ある場合）左文脈を示します
* `input`はカタカナ表記された入力を示します
* `expected_output`は許容可能な変換候補を列挙します
* `original_text`は元データにおける文章全体にあたります
* `splitted_input_for_limited_input_length`は入力長の制約がある手法で評価するために入力を区切った場合の分割位置を示すデータです。入力が十分に長い場合準備されています

```json
{
  "index": "1890",
  "context_text": "",
  "input": "カケイヲタスケルタメ、リョウシュノイエニホウコウシ",
  "expected_output": [
    "家計を助けるため、領主の家に奉公し",
    "家計を助ける為、領主の家に奉公し"
  ],
  "original_text": "家計を助けるため、領主の家に奉公している。",
  "splitted_input_for_limited_input_length": []
}
```

このデータは以下の手順で構築しています。

* 日本語Wikipedia入力誤りデータセット (v2)のテストデータから`kanji-conversion_a`タイプの誤りを含む項目を200件サンプリングしました。これは全体の約20%にあたります。
* ついで、200件のうち100件を左文脈付きかな漢字変換、100件を条件のないかな漢字変換用のデータとしました。
* それぞれのデータにおいて、データの一部分を切り出し、これを変換対象のテキストとします。変換対象のテキストの読み推定を行い、これを入力とします。
* 入力（読み）及び区切りの妥当性を人手でチェック・修正し、変換候補が一意に定まらない場合は許容解を列挙しました。

## 評価方法

Python向けの評価の実装を`utils.py`にまとめています。適宜ご利用ください。

また、評価コードのテストが`test_utils.py`です。

両ファイルともにライセンスはCC0 1.0 Universalです。