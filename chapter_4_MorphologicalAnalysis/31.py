#本問題はPandasの利用を想定していないようだが、Pandasを使った方が楽だと思い、利用する

import pandas as pd

df = pd.read_csv('Desktop/neko.txt.mecab',names=('a','b','c','d','e','f'))
tmp = list(df[df['d'].str.contains('動詞-自立','動詞-非自立', na=False)]['a'])　#動詞の表層形をすべて抽出
print(tmp)
