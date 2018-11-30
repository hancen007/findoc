def print_menu():
    print("="*30)
    print("xxx--system---")
    print("1.xxx")
    print("2.xxx")

def print_string():
    print("string")

print_menu()
print_string()


def sum_2_nums(a,b):
    result =  a + b
    print("%d+%d=%d"%(a,b,result))

num1 = int(input("请输入第1数字"))
num2 = int(input("请输入第2个数字"))

#调用函数

sum_2_nums(num1,num2)


#返回值带一值
def get_str():
    str = 22
    print("当前温度是：%d" %str)
    return str

result = get_str()


#一个函数返回多个return
def test():
    a = 11
    b = 22
    c = 33

    #第1种,用一个列表来封装3个变量的值
    d = [a,b,c]
    return d
    #第2种
    #return [a,b,c]
    #第3中
    #return (a,b,c)
    #return a,b,c

    #return b
    #return c
num = test()
print(num)
num = test()
print(num)
