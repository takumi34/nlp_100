import pandas as pd

df = pd.read_csv('Desktop/neko.txt.mecab',names=('a','b','c','d','e','f'))
tmp = list(df[df['d'].str.contains('名詞-サ変接続', na=False)]['a'])  #サ変接続の名詞をすべて抽出
tmp2 = []
for t in tmp:
    if  t.find('——') == -1 : #'——'が幾つか含まれていたので、これを除去
        tmp2.append(t)

print(tmp2)
