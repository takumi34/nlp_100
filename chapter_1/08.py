def cipher(s):
    res = []
    for i in s:
        if (i.islower()):
            res.append(chr(219 - ord(i)))
        else:
            res.append(i)
    return ''.join(res)


text = "chika chika"
a = cipher(text)
print(a)
b = cipher(a)
print(b)
