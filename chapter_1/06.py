def ngram(text, n):
    list = []
    tsize = len(text)
    for i in range(tsize - n + 1):
        list.append(text[i:i + n])
    return list


a = "paraparaparadise"
b = "paragraph"

abi = set(ngram(a, 2))
bbi = set(ngram(b, 2))

print(abi | bbi)  #和集合
print(abi & bbi)  #積集合
print(abi - bbi)  #差集合
print("ok" if "se" in (abi or bbi) else "no")

