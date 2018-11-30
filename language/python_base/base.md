# 语句和语法

- **#** 表示之后是python注释
- **\n** 行分隔符
- **\** 继续上一行
- **;** 两个语句连接在一行中
- **:** 将代码块的头和体分开
- python模块以文件的形式组织



## 字符串学用内建函数

- **大小写转换 lower()/upper**

```
>>> name = 'hancen'
>>> nLower = name.lower()
>>> nLower,name
('hancen', 'hancen')
>>> aUpper =name.upper()
>>> aUpper,name
('HANCEN', 'hancen')
>>>

```
- **去掉空格 lstrip()/rstrip()/strip**

- - **拼接和切片 join()/split(str='')**

```
>>> a = ['a','b','b']
>>> b='&'.join(a)
>>> b
'a&b&b'
>>> clist = b.split('&')
>>> clist
['a', 'b', 'b']
>>>
```


## 列表

- **pop** 顶部弹出
- **sort** 反序
- **reverse** 反转
