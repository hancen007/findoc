
# 应用场景函数作为参数传递
def test(a,b):
    return a + b
result = test(11,22)
print(result)
test2 = lambda a,b:a +b
result2 = test2(11,22)
print(result2)


#想一想，下面的数据如何指定按age或name排序？
stus = [
    {"name":"zhangsan", "age":18},
    {"name":"lisi", "age":19},
    {"name":"wangwu", "age":17}
]

#按name排序
stus.sort(key=lambda x:x['name'])
print(stus)

#按age排序
stus.sort(key=lambda x:x['age'])
print(stus)
