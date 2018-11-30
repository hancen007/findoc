目前流行的数据交换格式有：XML,JSON(最流行)
## Json介绍
> 一种基于key/Value以一定规则的轻量级的数据交换格式

## Json处理
它的处理本质就是数据编码和解码
- 将特定语言的本地数据类型编码为标准的JSON格式的字符串
- 将标准的JSON格式的字符串解码为特定语言本地数据类型
-----
JSON处理库
Python中针对JSON的处理提供JSON库
```

import json

def json_dumps_demo():
    '''编码成json字符串'''
    my_dict = dict(
        name = 'alatest',
        age = '1',
    )
    my_array = []
    my_array.append(my_dict)

    print(json.dumps(my_dict))
    print(json.dumps(my_array))

def json_loads_demo():
    '''解码'''
    json_str = '{"name": "alatest",'\
                ' "age": "1"}'
    my_dict = json.loads(json_str)
    print('my name is%s,''I am %s years old'
        %(
            my_dict['name'],
            my_dict['age']
        )
        )

print(json_dumps_demo())
```
