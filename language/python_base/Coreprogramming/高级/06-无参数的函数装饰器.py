from time import ctime,sleep

def timefun(func):
    print("---正在装饰---")
    def wrappedfun():
        print("%s call at %s" %(func.__name__,ctime()))
        func()
    return wrappedfun


@timefun
def foo():
    print('I am foo')
foo()


#代码理解

foo = timefun(foo)
#foo先作为参数赋值给func后，foo接收
foo()
#调用foo(),即造价调用wrappedfun()
