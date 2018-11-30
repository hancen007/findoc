# 装饰器
装饰器是程序开发中经常会用到的一个功能，用好了装饰器，开发效率如虎添翼，所以这也是Python面试中必问的问题，但对于好多初次接触这个知识的人来讲，这个功能有点绕，自学时直接绕过去了，然后面试问到了就挂了，因为装饰器是程序开发的基础知识，这个都不会，别跟人家说你会Python, 看了下面的文章，保证你学会装饰器。

1. 先明白这段代码

#### 第一波 ####

```
def foo():
    print('foo')

foo     #表示是函数
foo()   #表示执行foo函数
```
#### 第二波 ####
```
def foo():
    print('foo')

foo = lambda x: x + 1

foo()   # 执行下面的lambda表达式，而不再是原来的foo函数，因为foo这个名字被重新指向了另外一个匿名函数

```

2. 需求来了
初创公司有N个业务部门，1个基础平台部门，基础平台负责提供底层的功能，如：数据库操作、redis调用、监控API等功能。业务部门使用基础功能时，只需调用基础平台提供的功能即可。如下：

```
############### 基础平台提供的功能如下 ###############

def f1():
    print('f1')

def f2():
    print('f2')

def f3():
    print('f3')

def f4():
    print('f4')

############### 业务部门A 调用基础平台提供的功能 ###############

f1()
f2()
f3()
f4()

############### 业务部门B 调用基础平台提供的功能 ###############

f1()
f2()
f3()
f4()
```
目前公司有条不紊的进行着，但是，以前基础平台的开发人员在写代码时候没有关注验证相关的问题，即：基础平台的提供的功能可以被任何人使用。现在需要对基础平台的所有功能进行重构，为平台提供的所有功能添加验证机制，即：执行功能前，先进行验证。

老大把工作交给 B，他是这么做的：
跟每个业务部门交涉，每个业务部门自己写代码，调用基础平台的功能之前先验证。诶，这样一来基础平台就不需要做任何修改了。太棒了，有充足的时间泡妹子...

当天Low B 被开除了…

老大把工作交给 C，他是这么做的：
```
############### 基础平台提供的功能如下 ###############

def f1():
    # 验证1
    # 验证2
    # 验证3
    print('f1')

def f2():
    # 验证1
    # 验证2
    # 验证3
    print('f2')

def f3():
    # 验证1
    # 验证2
    # 验证3
    print('f3')

def f4():
    # 验证1
    # 验证2
    # 验证3
    print('f4')

############### 业务部门不变 ###############
### 业务部门A 调用基础平台提供的功能###

f1()
f2()
f3()
f4()

### 业务部门B 调用基础平台提供的功能 ###

f1()
f2()
f3()
f4()
```
过了一周 C 被开除了…

老大把工作交给 D，他是这么做的：
只对基础平台的代码进行重构，其他业务部门无需做任何修改

```
############### 基础平台提供的功能如下 ###############

def check_login():
    # 验证1
    # 验证2
    # 验证3
    pass


def f1():

    check_login()

    print('f1')

def f2():

    check_login()

    print('f2')

def f3():

    check_login()

    print('f3')

def f4():

    check_login()

    print('f4')

```

老大看了下 D 的实现，嘴角漏出了一丝的欣慰的笑，语重心长的跟D聊了个天：

老大说：
写代码要遵循开放封闭原则，虽然在这个原则是用的面向对象开发，但是也适用于函数式编程，简单来说，它规定已经实现的功能代码不允许被修改，但可以被扩展，即：

封闭：已实现的功能代码块
开放：对扩展开发
如果将开放封闭原则应用在上述需求中，那么就不允许在函数 f1 、f2、f3、f4的内部进行修改代码，老板就给了Low BBB一个实现方案:

```
def w1(func):
    def inner():
        # 验证1
        # 验证2
        # 验证3
        func()
    return inner

@w1
def f1():
    print('f1')
@w1
def f2():
    print('f2')
@w1
def f3():
    print('f3')
@w1
def f4():
    print('f4')
```

对于上述代码，也是仅仅对基础平台的代码进行修改，就可以实现在其他人调用函数 f1 f2 f3 f4 之前都进行【验证】操作，并且其他业务部门无需做任何操作。

Low BBB心惊胆战的问了下，这段代码的内部执行原理是什么呢？

老大正要生气，突然D的手机掉到地上，恰巧屏保就是D的女友照片，老大一看一紧一抖，喜笑颜开，决定和D交个好朋友。

详细的开始讲解了：

单独以f1为例：

```
def w1(func):
    def inner():
        # 验证1
        # 验证2
        # 验证3
        func()
    return inner

@w1
def f1():
    print('f1')
python解释器就会从上到下解释代码，步骤如下：

def w1(func): ==>将w1函数加载到内存
@w1
```

没错， 从表面上看解释器仅仅会解释这两句代码，因为函数在 没有被调用之前其内部代码不会被执行。

从表面上看解释器着实会执行这两句，但是 @w1 这一句代码里却有大文章， @函数名 是python的一种语法糖。

上例@w1内部会执行一下操作：
执行w1函数
执行w1函数 ，并将 @w1 下面的函数作为w1函数的参数，即：@w1 等价于 w1(f1) 所以，内部就会去执行：

```
def inner():
    #验证 1
    #验证 2
    #验证 3
    f1()     # func是参数，此时 func 等于 f1

```

return inner# 返回的 inner，inner代表的是函数，非执行函数 ,其实就是将原来的 f1 函数塞进另外一个函数中
w1的返回值
将执行完的w1函数返回值 赋值 给@w1下面的函数的函数名f1 即将w1的返回值再重新赋值给 f1，即：

```
新f1 = def inner():
            #验证 1
            #验证 2
            #验证 3
            原来f1()
        return inner

```

所以，以后业务部门想要执行 f1 函数时，就会执行 新f1 函数，在新f1 函数内部先执行验证，再执行原来的f1函数，然后将原来f1 函数的返回值返回给了业务调用者。

如此一来， 即执行了验证的功能，又执行了原来f1函数的内容，并将原f1函数返回值 返回给业务调用着

D 你明白了吗？要是没明白的话，我晚上去你家帮你解决吧！！！

3. 再议装饰器

```
#定义函数：完成包裹数据
def makeBold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

#定义函数：完成包裹数据
def makeItalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makeBold
def test1():
    return "hello world-1"

@makeItalic
def test2():
    return "hello world-2"

@makeBold
@makeItalic
def test3():
    return "hello world-3"

print(test1()))
print(test2()))
print(test3()))
运行结果:

<b>hello world-1</b>
<i>hello world-2</i>
<b><i>hello world-3</i></b>

```

4. 装饰器(decorator)功能
引入日志
函数执行时间统计
执行函数前预备处理
执行函数后清理功能
权限校验等场景
缓存
5. 装饰器示例

例1:无参数的函数

```
from time import ctime, sleep

def timefun(func):
    def wrappedfunc():
        print("%s called at %s"%(func.__name__, ctime()))
        func()
    return wrappedfunc

@timefun
def foo():
    print("I am foo")

foo()
sleep(2)
foo()

```

上面代码理解装饰器执行行为可理解成

```
foo = timefun(foo)
#foo先作为参数赋值给func后,foo接收指向timefun返回的wrappedfunc
foo()
#调用foo(),即等价调用wrappedfunc()
#内部函数wrappedfunc被引用，所以外部函数的func变量(自由变量)并没有释放
#func里保存的是原foo函数对象
```

例2:被装饰的函数有参数

```
from time import ctime, sleep

def timefun(func):
    def wrappedfunc(a, b):
        print("%s called at %s"%(func.__name__, ctime()))
        print(a, b)
        func(a, b)
    return wrappedfunc

@timefun
def foo(a, b):
    print(a+b)

foo(3,5)
sleep(2)
foo(2,4)

```

例3:被装饰的函数有不定长参数

```
from time import ctime, sleep

def timefun(func):
    def wrappedfunc(*args, **kwargs):
        print("%s called at %s"%(func.__name__, ctime()))
        func(*args, **kwargs)
    return wrappedfunc

@timefun
def foo(a, b, c):
    print(a+b+c)

foo(3,5,7)
sleep(2)
foo(2,4,9)

```

例4:装饰器中的return

```
from time import ctime, sleep

def timefun(func):
    def wrappedfunc():
        print("%s called at %s"%(func.__name__, ctime()))
        func()
    return wrappedfunc

@timefun
def foo():
    print("I am foo")

@timefun
def getInfo():
    return '----hahah---'

foo()
sleep(2)
foo()


print(getInfo())
执行结果:

foo called at Fri Nov  4 21:55:35 2016
I am foo
foo called at Fri Nov  4 21:55:37 2016
I am foo
getInfo called at Fri Nov  4 21:55:37 2016
None
如果修改装饰器为return func()，则运行结果：

foo called at Fri Nov  4 21:55:57 2016
I am foo
foo called at Fri Nov  4 21:55:59 2016
I am foo
getInfo called at Fri Nov  4 21:55:59 2016
----hahah---
```

总结：
一般情况下为了让装饰器更通用，可以有return

例5:装饰器带参数,在原有装饰器的基础上，设置外部变量

```
#decorator2.py

from time import ctime, sleep

def timefun_arg(pre="hello"):
    def timefun(func):
        def wrappedfunc():
            print("%s called at %s %s"%(func.__name__, ctime(), pre))
            return func()
        return wrappedfunc
    return timefun

@timefun_arg("itcast")
def foo():
    print("I am foo")

@timefun_arg("python")
def too():
    print("I am too")

foo()
sleep(2)
foo()

too()
sleep(2)
too()
可以理解为

foo()==timefun_arg("itcast")(foo)()

```
例6：类装饰器（扩展，非重点）
装饰器函数其实是这样一个接口约束，它必须接受一个callable对象作为参数，然后返回一个callable对象。在Python中一般callable对象都是函数，但也有例外。只要某个对象重写了 __call__() 方法，那么这个对象就是callable的。
```
class Test():
    def __call__(self):
        print('call me!')

t = Test()
t()  # call me
类装饰器demo


class Test(object):
    def __init__(self, func):
        print("---初始化---")
        print("func name is %s"%func.__name__)
        self.__func = func
    def __call__(self):
        print("---装饰器中的功能---")
        self.__func()

```

#说明：
#1. 当用Test来装作装饰器对test函数进行装饰的时候，首先会创建Test的实例对象
#    并且会把test这个函数名当做参数传递到__init__方法中
#    即在__init__方法中的func变量指向了test函数体
#
#2. test函数相当于指向了用Test创建出来的实例对象
#
#3. 当在使用test()进行调用时，就相当于让这个对象()，因此会调用这个对象的__call__方法
#
#4. 为了能够在__call__方法中调用原来test指向的函数体，所以在__init__方法中就需要一个实例属性来保存这个函数体的引用
#    所以才有了self.__func = func这句代码，从而在调用__call__方法中能够调用到test之前的函数体
@Test
def test():
    print("----test---")
test()
showpy()#如果把这句话注释，重新运行程序，依然会看到"--初始化--"
运行结果如下：

---初始化---
func name is test
---装饰器中的功能---
----test---



装饰器与出错重试机制
谈到稳定性，不得不说的就是“出错重试”机制了，在自动化测试中，由于环境一般都是测试环境，经常会有各种各种的抽风情况影响测试结果，这样就为测试的稳定性带来了挑战，毕竟谁也不想自己的脚本一天到晚的出各种未知问题，而往往这种环境的抽风（通常是前端页面的响应速度和后端接口的响应速度）带来的影响是暂时的，可能上一秒失败了，下一秒你再执行又好了，在这种情况下，如果你有一个出错重试机制，起码可以在这种暂时性的影响下让你的脚本安然无恙，下面我们具体的说一下做法。

什么是装饰器？
因为我们的做法依赖装饰器，所以在去做之前，先简单介绍一下装饰器。

装饰器，表现形式为，在方法（或者类）的上面加上@xxx这样的语句，假如我们已经实现了一个装饰器名叫retry，那么我们想用它就这么用：

@retry
def test_login():
    print("test")
    error = 1/0
如果retry实现了出错再次重试（稍后再说如何实现），那么这么使用的话，就会让test_login这个case在执行出错的时候再次执行。

很神奇，让我们来看看实现retry的代码：

def retry(func):
    def warp():
        for time in range(3):
            try:
                func()
            except:
                pass
    return warp

就结果而言，执行以下代码：

@retry
def test_login():
    print("test")
    error = 1/0

test_login()
和执行：

retry(test_login)()
是等价的，由此我们可以看出，装饰器其实本质上就是一个函数，这个函数接收其他函数（或者类）作为参数，通过对这个函数（或者类）的调用或者修改，完成不更改原始函数而修改该函数的功能。

在这里还有一个知识点，你有没有想过，在retry内部的函数warp()，是怎么拿到func这个参数来执行的？执行retry函数return的是warp这个函数，而warp并没有接受func这个传参啊。

这就是python里的闭包的概念，闭包就是指运行时自带上下文的函数，比如这里的warp这个函数，他运行的时候自带了上层函数retry传给他的func这个函数，所以才可以在运行时对func进行处理和输出。

了解了装饰器和闭包，那么下面就很容易做到对测试用例的出错重试机制了。

编写一个出错重试装饰器
现在，我们来尝试自己编写一个用于测试用例的出错重试装饰器，代码如下：

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
这个装饰器可以通过传入重试次数（times）和重试等待时间（wait_time），对待测用例实行重试机制。

pytest里的出错重试机制实现
在测试框架pytest里，已经实现了有关出错重试的策略，我们首先需要安装一个此类的插件，在cmd内执行以下命令安装：

pip install pytest-rerunfailures
如果你需要将此机制应用到所有的用例上，那么请在执行的时候使用如下命令（reruns是重试次数）：

pytest --reruns 5
来执行你的用例；

如果你期望加上出错重试的等待时间，请使用如下命令(reruns-delay是等待时间)：

pytest --reruns 5 --reruns-delay 1
来执行你的用例；

如果你只想对某几个测试用例应用重试策略，你可以使用装饰器：

@pytest.mark.flaky(reruns=5, reruns_delay=2)
例如：

@pytest.mark.flaky(reruns=5, reruns_delay=2)
def test_example():
    import random
    assert random.choice([True, False])
更详细的介绍请参阅官方文档 。

Allure里的测试用例分层
刚刚我们实现了用例的出错重试机制，但是这仅仅解决了脚本在不稳定环境下的稳定性；如果还想要脚本变得更加容易维护，除了传统的po模式使用例和元素分离之外，我们还可以引入测试用例分层机制。

为什么要采用分层机制？
传统的po模式，仅仅实现了用例和元素分离，这一定层面上保障了用例的可维护性，起码不必头疼于元素的变更会让用例到处失效；但是这还不够，例如，现在有三个case，他们都包含了以下步骤：登录、打开工作台、进入个人中心；那么如果不做分层，这三个用例会把这三个步骤都写一遍，如果某天页面的变动导致其中一个步骤需要更改，那么你不得不去每个用例里去更新那个步骤。

而如果，我们把用例当做是堆积木，登录、打开工作台、进入个人中心这三个步骤都只是个积木，那么我们写用例的时候，只需要在用到这个步骤时，把积木搭上去；如果某一天，其中一个积木的步骤有变动，那么只需要去更改这个积木的内容，而无需在每个使用了这个积木的用例里去改动。

这大大增强了用例的复用性和可维护性，这就是采用分层机制的原因，下面，我会就allure里的分层机制做介绍来讨论具体如何实现。

allure的装饰器@step
在allure里，我们可以通过装饰器@step完成分层机制，具体的，当你用@step装饰一个方法时，当你在用例里执行这个方法，会在报告里，表现出这个被装饰方法；而@step支持嵌套结构，这就意味着，你可以像搭积木一样去搭你的步骤，而他们都会一一在报告里被展示。

下面直接用allure的官方示例作做举例：

import allure
import pytest

from .steps import imported_step


@allure.step
def passing_step():
    pass


@allure.step
def step_with_nested_steps():
    nested_step()


@allure.step
def nested_step():
    nested_step_with_arguments(1, 'abc')


@allure.step
def nested_step_with_arguments(arg1, arg2):
    pass


def test_with_imported_step():
    passing_step()
    imported_step()


def test_with_nested_steps():
    passing_step()
    step_with_nested_steps()