# 类的构成
## 类(Class) 由3个部分构成
- 类的名称:类名
- 类的属性:一组数据
- 类的方法:允许对进行操作的方法 (行为)


应用:烤地瓜
为了更好的理解面向对象编程，下面以“烤地瓜”为案例，进行分析

1. 分析“烤地瓜”的属性和方法
示例属性如下:
cookedLevel : 这是数字；0~3表示还是生的，超过3表示半生不熟，超过5表示已经烤好了，超过8表示已经烤成木炭了！我们的地瓜开始时时生的
cookedString : 这是字符串；描述地瓜的生熟程度
condiments : 这是地瓜的配料列表，比如番茄酱、芥末酱等
示例方法如下:
cook() : 把地瓜烤一段时间
addCondiments() : 给地瓜添加配料
__init__() : 设置默认的属性
__str__() : 让print的结果看起来更好一些
2. 定义类，并且定义__init__()方法
#定义`地瓜`类
```
class SweetPotato:
    '这是烤地瓜的类'

    #定义初始化方法
    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = "生的"
        self.condiments = []
```
3. 添加"烤地瓜"方法
    #烤地瓜方法
```
    def cook(self, time):
        self.cookedLevel += time
        if self.cookedLevel > 8:
            self.cookedString = "烤成灰了"
        elif self.cookedLevel > 5:
            self.cookedString = "烤好了"    
        elif self.cookedLevel > 3:
            self.cookedString = "半生不熟"
        else:
            self.cookedString = "生的"
```
