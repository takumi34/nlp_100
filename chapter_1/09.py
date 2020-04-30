import random


def typogly(s):
    if (len(s) <= 4):
        return s
    else:
        res = [s[0]] + random.sample(list(s[1:-1]), len(s[1:-1])) + [s[-1]]
        return "".join(res)


a = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

res = " ".join([typogly(i) for i in a.split()])
print(res)