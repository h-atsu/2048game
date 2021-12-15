## 採点実行方法
- solver.pyのSolverクラスsolveメソッドとして盤面の状態を表す4*4の二次元配列を受け取り，"r", "l", "u", "d"のいずれかの文字列を返す関数を作成する．  
- 作成したアルゴリズムの性能評価を実際に問題インスタンスを複数実行してその平均値で評価．(下記コマンド)  
`pyhton3 scoring.py`

## Visualizer 実行方法(ローカル)
- ローカルのchromeのサポートバージョンのchromedriverをインストールしてパスを通す (https://chromedriver.chromium.org/downloads)
- 以下のコマンドを実行  
`python3 visualizer.py`

## Visualizer 実行方法(colab)
- 以下のコマンドを実行
`!apt-get update`  
`!pip install selenium`  
`!apt install chromium-chromedriver`  
`import sys`  
`sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')`  


## 解法
- 乱択 1000点前後
- 一手先得点貪欲 3000点前後

## 参考資料
- 中江 康公，米田 貴，『「2048」のアルゴリズム』，2018 年度情報処理学会関西支部 支部大会 (2018)
- https://play2048.co/
