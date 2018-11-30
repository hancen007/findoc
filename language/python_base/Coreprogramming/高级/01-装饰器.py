

def decorate_1(func):
    print("----开始装饰------")


    def inner():
        print("----使用方法---{}".format(func()))

    return inner




k1 = decorate_1(10)

print(k1)

@decorate_1
def test_dec():
    print("----测试用的")

#k2 = K1(20)

test_dec()
#print(k2)