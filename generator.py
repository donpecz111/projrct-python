def generator():
    x = 0
    while True:
        y = yield x
        if y  is None:
            x = x + 1
        else:
            x = y

g= generator()
print(next(g))
print('cos innego')
print(next(g))
print(next(g))
print('cos innego')
print(next(g))
print(g.send(12))
print(next(g))