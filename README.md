# ポスト交換シミュレーターテンプレート
自由に改造してください(frokかcloneしてください)

## nodes module
仮想的なノード(ユーザ？)を作成します。
現在はクラスメソッドとしてデータ交換の発火を行っていますが、P2Pの仕組み的にはメソッドで完結させる方が望ましいと思われます。

また、クラスメソッドを作るという事はサーバを作っていると同義であると言えるので直接的に関与するクラスメソッドの作成はなるべく避けましょう。

TODO:
- 非同期処理化 

## posts medule
ポストデータを作成、管理します。基本的に後からのポストデータの作成はないこととしています。重要なものではないです。

## logs medule
logを作成したいときに専用のmoduleを作成してください。
また、出力先はlogファイル内が望ましいと考えています(自由でok)。

## __main__.py
主な処理を書いてください

## 開発環境
開発コンテナ内にて開発、Poetryにてライブラリとバージョン管理を想定しています。