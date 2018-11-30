## Python基本语法

### 1. 输出

```
print ("python")
```

### 2. 分支与循环

``` If   For  ```
```
a = 13
b = 15

if  a > b:
    print ("a 大于 b")
else:
    print ("这是提示")

```

### 3. 数组与字典

数组用方括号（[]）表示，里面的每一项用逗号（，）隔开。

```
>>> lists = [1,2,3,'a',5]
>>> lists
>>>  [2, 3, 'a', 5]
>>> lists[0]
1
>>> lists[4]
>>> 5
>>> lists[4]='b'
>>> lists[4]
>>> 'b'
>>> lists.append('c')
>>> lists
>>>  [2, 3, 'a', 'b', 'c']
```

------

Python允许在数组里面任意地放置数字或字符串。需要注意的是，数组下标是从 0 开始的，所以，lists[0]会输出数组中的第一项。append()函数可以向数组末尾追加新的项。

```
>>> dicts = {"username":"zhangsan",'password':123456}
>>> dicts.keys()
>>> ['username', 'password']
>>> dicts.values()
>>> ['zhangsan', 123456]
>>> dicts.items()
>>> [('username', 'zhangsan'), ('password', 123456)]
>>> for k,v in dicts.items():
>>> dicts("dicts keys is %r " %k)
>>> nt("dicts values is %r " %v)
>>> dicts keys is 'username'
>>> dicts values is 'zhangsan'
>>> dicts keys is 'password'
>>> dicts values is 123456
```

------

Python 规定一个字典中的 key 必须独一无二，value 可以相同。s()函数返回字典 key 的列表，values()函数返回字典 value 的列表， items()函数将所有的字典项以列表回，这些列表中的每一项都包含 key 和 value，但是项在返回时并不会按照它们在字典中的存放顺序。如果想按存放的顺序输出，则可以通过下面的方法。

### 4. 函数、类和方法

#### 1 函数

在 Python 中通过 def 关键字来定义函数。下面来定义一个函数。

```
def add (a,b):
    return a + b
add (2,5)
```

------

创建一个 add()函数，此函数接收两个参数 a、b，通过 print()打印 a+b 的结果。调用 add()函数，并且传两个参数3、5 给 add()函数。通常add()函数不会直接打印结果，而是将处理结果通过 return 关键字返回。

> Pyhon Shell

```
>>> def add(a, b):
>>>   return a + b
>>> add(3, 5)
>>> 8
```

------

我们在调用 add()函数的时候不想传参，这时可以为 add()函数设置默认参数。

> pyhon Shell

```
>>> def add(a=1, b=2):
>>>   return a + b
>>> add()
>>> 3
>>> add(3,5)
>>> 8
```

------

如果调用时不传参，那么add()函数就使用默认参数进行计算；如果传参则计算参数的值。
