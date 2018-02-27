import pandas as pd

df = pd.read_csv('Desktop/neko.txt.mecab',names=('a','b','c','d','e','f'))
tmp = list(df[df['d'].str.contains('動詞-自立','動詞-非自立', na=False)]['c'])  #動詞の原形をすべて抽出

print(tmp)
