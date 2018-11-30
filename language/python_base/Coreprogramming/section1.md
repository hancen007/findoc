# python是动态语言
1. 动态语言的定义
动态编程语言 是 高级程序设计语言 的一个类别，在计算机科学领域已被广泛应用。它是一类 在运行时可以改变其结构的语言 ：例如新的函数、对象、甚至代码可以被引进，已有的函数可以被删除或是其他结构上的变化。动态语言目前非常具有活力。例如JavaScript便是一个动态语言，除此之外如 PHP 、 Ruby 、 Python 等也都属于动态语言，而 C 、 C++ 等语言则不属于动态语言。----来自 维基百科

2. 运行的过程中给对象绑定(添加)属性

```
>>> class Person(object):
    def __init__(self, name = None, age = None):
        self.name = name
        self.age = age


>>> P = Person("小明", "24")
>>>


Person.sex = None #给类Person添加一个属性
>>> P1 = Person("小丽", "25")
>>> print(P1.sex) #如果P1这个实例对象中没有sex属性的话，那么就会访问它的类属性
None #可以看到没有出现异常
>>>

```
3. 运行的过程中给类绑定(添加)方法

```
我们直接给Person绑定sex这个属性，重新实例化P1后，P1就有sex这个属性了！ 那么function呢？怎么绑定？

>>> class Person(object):
    def __init__(self, name = None, age = None):
        self.name = name
        self.age = age
    def eat(self):
        print("eat food")


>>> def run(self, speed):
    print("%s在移动, 速度是 %d km/h"%(self.name, speed))


>>> P = Person("老王", 24)
>>> P.eat()
eat food
>>>
>>> P.run()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    P.run()
AttributeError: Person instance has no attribute 'run'
>>>
>>>
>>> import types
>>> P.run = types.MethodType(run, P)
>>> P.run(180)
老王在移动,速度是 180 km/h
```
