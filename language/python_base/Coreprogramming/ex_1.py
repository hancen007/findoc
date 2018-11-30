# -*- coding: utf-8 -*-
# @File  : ex_1.py
# @Author: 岑苏岸
# @Date  : 2018/9/25
# @Desc  :


#闭包
def w1(func):
    def inner():
        print("验证内部")
        func()

    return inner

def f1():
    print("---f1---")

def f2():
    print("----f2----")

innerfunc = W1(f1)



def test_login():
    print("login")




def retry(func):
    def warp():
        for time in range(3):
            try:
                func()
            except:
                pass
    return warp


@retry
def test_login_retry():
    assert 1 = 1

test_login_retry()

"""
def retry(times=3,wait_time=10):
    def warp_func(func):
        def fild_retry(*args,**kwargs):
            for time in range(times):
                try:
                    func(*args,**kwargs)
                    return 
                except:
                    time.sleep(wait_time)
        return fild_retry
    return warp_func

"""


