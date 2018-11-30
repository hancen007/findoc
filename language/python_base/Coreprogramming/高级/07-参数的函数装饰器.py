from time import ctime,sleep

def timefun(func):
    print("---正在装饰---")
    def wrappedfun(a,b):
        print("%s call at %s" %(func.__name__,ctime()))
        func(a,b)
    return wrappedfun


@timefun
def foo(a,b):
    print(a+b)
foo(3,5)
