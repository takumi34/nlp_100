def ngram(text, n):
    list = []
    tsize = len(text)
    for i in range(tsize - n + 1):
        list.append(text[i:i + n])
    return list

a = "I am an NLPer"
print(ngram(a, 2))  #文字bi-gram
print(ngram(a.split(' '), 2))  #単語bi-gram
