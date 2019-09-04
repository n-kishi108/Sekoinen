# 支給された額に対して最も特をする組み合わせを推薦するプログラムSekoinen

## 背景
会社から食費を支給されたことはありませんか？領収証がないと精算してもらえない場合、できる限り損をしないように頑張ろうとするのが大阪人というものです。では、その組み合わせをどうやって見つけますか？いちいち計算しますか？いいえ。プログラムにお任せしましょう！

## ファイル構成

```
.
├── README.md
└── src
    ├── Sekoinen.py
    └── SekoinenDe.py
```

## Sekoinenについて
Sekoinenは指定金額に収まる範囲で最大の金額となる組み合わせを見つけてくれるプログラムです。

## SekoinenDeについて
SekoinenDeは指定金額内で最大の組み合わせと、指定金額を超えた最小の組み合わせを比較し、より差分の少ない組み合わせを推薦してくれるプログラムです。

## 使い方
`python3`のプログラムを実行するコマンドで実行してください。

領収証の値を要求されるので、一つずつ入力します。

0が入力されたら今度は支給額を聞いてきます。

それを答えれば結果を返してくれます。