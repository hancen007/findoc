from time import ctime,sleep

def timefun(func):
    print("---正在装饰---")
    def wrappedfun(*args,**kwargs):
        print("%s call at %s" %(func.__name__,ctime()))
        res = func(*args,**kwargs)
        return res
    return wrappedfun


@timefun
def foo():
    #print(a+b+c)
    return "REVIEW"
res = foo()

print(res)
