from time import ctime,sleep
#被装饰的函数有不定⻓参数
def timefun(func):
    print("---正在装饰---")
    def wrappedfun(*args,**kwargs):
        print("%s call at %s" %(func.__name__,ctime()))
        func(*args,**kwargs)
    return wrappedfun


@timefun
def foo(a,b,c):
    print(a+b+c)
foo(3,5,7)
