a = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
a = a.replace(',','').replace('.','')
b = a.split()
l = []
for i in range(len(b)):
    l.append(len(b[i]))
print(l)