# 三目Zero
AlphaZeroのアルゴリズムで三目並べするAI作った。

![デモ画像](https://github.com/derodero24/3moku_zero/blob/master/demo.gif)

## コード
- game.py: ゲーム状態
- dual_network.py: デュアルネットワーク
- pv_mcts.py: モンテカルロ木探索
- self_play.py: セルフプレイ
- train_network.py: パラメータ更新
- evaluate_network.py: 新パラメータの評価
- evaluate_best_player.py: ベストプレーヤーの評価
- train_cycle.py: 学習サイクル
- human_play.py: ゲームUI（tkinter）
- human_play.py2: ゲームUI（kivy）
