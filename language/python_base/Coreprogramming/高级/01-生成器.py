L = [x*2 for x in range(5)]


def creatNum():
    a,b =0,1
    for i in range(5):
        yield b
        a,b = b,a+b
a = creatNum()
ret = a.__next__()
print(ret)
