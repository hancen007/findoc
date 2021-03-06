# 生成器

## 1. 什么是生成器

通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

## 2. 创建生成器方法1

要创建一个生成器，有很多种方法。第一种方法很简单，只要把一个列表生成式的 [ ] 改成 ( )

```
In [15]: L = [ x*2 for x in range(5)]

In [16]: L
Out[16]: [0, 2, 4, 6, 8]

In [17]: G = ( x*2 for x in range(5))

In [18]: G
Out[18]: <generator object <genexpr> at 0x7f626c132db0>

In [19]:
```

创建 L 和 G 的区别仅在于最外层的 [ ] 和 ( ) ， L 是一个列表，而 G 是一个生成器。我们可以直接打印出L的每一个元素，但我们怎么打印出G的每一个元素呢？如果要一个一个打印出来，可以通过 next() 函数获得生成器的下一个返回值：

```
In [19]: next(G)
Out[19]: 0

In [20]: next(G)
Out[20]: 2

In [21]: next(G)
Out[21]: 4

In [22]: next(G)
Out[22]: 6

In [23]: next(G)
Out[23]: 8

In [24]: next(G)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-24-380e167d6934> in <module>()
----> 1 next(G)

StopIteration: 

In [25]:
```

```
In [26]: G = ( x*2 for x in range(5))

In [27]: for x in G:
   ....:     print(x)
   ....:     
0
2
4
6
8

In [28]:
```

生成器保存的是算法，每次调用 next(G) ，就计算出 G 的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出 StopIteration 的异常。当然，这种不断调用 next() 实在是太变态了，正确的方法是使用 for 循环，因为生成器也是可迭代对象。所以，我们创建了一个生成器后，基本上永远不会调用 next() ，而是通过 for 循环来迭代它，并且不需要关心 StopIteration 异常。

## 3. 创建生成器方法2

generator非常强大。如果推算的算法比较复杂，用类似列表生成式的 for 循环无法实现的时候，还可以用函数来实现。

比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：

1, 1, 2, 3, 5, 8, 13, 21, 34, ...

斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：

```
In [28]: def fib(times):
   ....:     n = 0
   ....:     a,b = 0,1
   ....:     while n<times:
   ....:         print(b)
   ....:         a,b = b,a+b
   ....:         n+=1
   ....:     return 'done'
   ....: 

In [29]: fib(5)
1
1
2
3
5
Out[29]: 'done'
```

仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。

也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：

```
In [30]: def fib(times):
   ....:     n = 0
   ....:     a,b = 0,1
   ....:     while n<times:
   ....:         yield b
   ....:         a,b = b,a+b
   ....:         n+=1
   ....:     return 'done'
   ....: 

In [31]: F = fib(5)

In [32]: next(F)
Out[32]: 1

In [33]: next(F)
Out[33]: 1

In [34]: next(F)
Out[34]: 2

In [35]: next(F)
Out[35]: 3

In [36]: next(F)
Out[36]: 5

In [37]: next(F)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-37-8c2b02b4361a> in <module>()
----> 1 next(F)

StopIteration: done
```

在上面fib 的例子，我们在循环过程中不断调用 yield ，就会不断中断。当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。同样的，把函数改成generator后，我们基本上从来不会用 next() 来获取下一个返回值，而是直接使用 for 循环来迭代：

```
In [38]: for n in fib(5):
   ....:     print(n)
   ....:     
1
1
2
3
5

In [39]:
```

但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：

```
In [39]: g = fib(5)

In [40]: while True:
   ....:     try:
   ....:         x = next(g)
   ....:         print("value:%d"%x)      
   ....:     except StopIteration as e:
   ....:         print("生成器返回值:%s"%e.value)
   ....:         break
   ....:     
value:1
value:1
value:2
value:3
value:5
生成器返回值:done

In [41]:
```

## 4. send

例子：执行到yield时，gen函数作用暂时保存，返回i的值;temp接收下次c.send("python")，send发送过来的值，c.next()等价c.send(None)

```
In [10]: def gen():
   ....:     i = 0
   ....:     while i<5:
   ....:         temp = yield i
   ....:         print(temp)
   ....:         i+=1
   ....:
```

#### 使用next函数

```
In [11]: f = gen()

In [12]: next(f)
Out[12]: 0

In [13]: next(f)
None
Out[13]: 1

In [14]: next(f)
None
Out[14]: 2

In [15]: next(f)
None
Out[15]: 3

In [16]: next(f)
None
Out[16]: 4

In [17]: next(f)
None
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-17-468f0afdf1b9> in <module>()
----> 1 next(f)

StopIteration:
```

#### 使用`__next__()`方法

```
In [18]: f = gen()

In [19]: f.__next__()
Out[19]: 0

In [20]: f.__next__()
None
Out[20]: 1

In [21]: f.__next__()
None
Out[21]: 2

In [22]: f.__next__()
None
Out[22]: 3

In [23]: f.__next__()
None
Out[23]: 4

In [24]: f.__next__()
None
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-24-39ec527346a9> in <module>()
----> 1 f.__next__()

StopIteration:
```

#### 使用send

```
In [43]: f = gen()

In [44]: f.__next__()
Out[44]: 0

In [45]: f.send('haha')
haha
Out[45]: 1

In [46]: f.__next__()
None
Out[46]: 2

In [47]: f.send('haha')
haha
Out[47]: 3

In [48]:
```

## 总结

生成器是这样一个函数，它记住上一次返回时在函数体中的位置。对生成器函数的第二次（或第 n 次）调用跳转至该函数中间，而上次调用的所有局部变量都保持不变。

生成器不仅“记住”了它数据状态；生成器还“记住”了它在流控制构造（在命令式编程中，这种构造不只是数据值）中的位置。

生成器的特点：

1. 节约内存
2. 迭代到下一次的调用时，所使用的参数都是第一次所保留下的，即是说，在整个所有函数调用的参数都是第一次所调用时保留的，而不是新创建的