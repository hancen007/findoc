## 属性property

1. 私有属性添加getter和setter方法

```
class Test (object):
    def __init__(self):
        self.__num = 100
    def setNum(self,newNum):
        self.__num = newNum
    def getNum(self):
        return self.__num


t =Test()
print(t.getNum())
```

2. 使用property升级getter和setter方法

```
class Test (object):
    def __init__(self):
        self.__num = 100
    def setNum(self,newNum):
        self.__num = newNum
    def getNum(self):
        return self.__num

    num = property(getNum,setNum)

t =Test()
t.num = 200

print(t.num)
```



3. 使用property取代getter和setter方法
@property成为属性函数，可以对属性赋值时做必要的检查，并保证代码的清晰短小，主要有2个作用

将方法转换为只读
重新实现一个属性的设置和读取方法,可做边界判定

```
class Test (object):
    def __init__(self):
        self.__num = 100
    @property
    def num(self):
        print("-----getter----")
        return self.__num

    @num.setter
    def num(self,newNum):
        self.__num = newNum

t =Test()
t.num = 20
print(t.num)

```
