#夏目漱石『吾輩は猫である」を形態素解析し、その結果を保存する
#以後はこの解析データを使って問題を解く

from natto import MeCab
import os
import csv

fp = open("neko.txt","r", encoding="utf-8")　#ファイルは<http://www.cl.ecei.tohoku.ac.jp/nlp100/>のもの
doc = fp.read()

nm = MeCab()


nm = MeCab("-Ochasen") #茶筅形式に出力フォーマットを変更

list_keitaiso = [i.split() for i in nm.parse(doc).splitlines()]

fp2= open('neko.txt.mecab', 'ab') 
 
with open('neko.txt.mecab','a') as fp2: #<neko.text.mecab>に入れる
    writer = csv.writer((fp2), lineterminator="\n")
    for i in range(0,len(list_keitaiso)):
        writer.writerow(list_keitaiso[i])

fp.close
