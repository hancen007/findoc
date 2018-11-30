from time import ctime,sleep

def timefun_arg(pre):
    def timefun(func):
        def wrappedfun(*args,**kwargs):
            print("%s call at %s %s" %(func.__name__,ctime(),pre))
            res = func(*args,**kwargs)
            return res
        return wrappedfun
    return timefun

#装饰器带参数,在原有装饰器的基础上，设置外部变量
@timefun_arg('hello world')
def foo():
    return "foo"
res = foo()

print(res)
