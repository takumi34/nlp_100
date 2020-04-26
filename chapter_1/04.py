a = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

a = a.replace(',', '').replace('.', '')
b = a.split()
l = []
for i in range(len(b)):
    if i + 1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        l.append([b[i][0], i + 1])
    else:
        l.append([b[i][0:2], i + 1])
print(l)
