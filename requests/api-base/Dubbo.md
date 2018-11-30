

# 如何科学的解释RPC

说起RPC，就不能不提到分布式，这个促使RPC诞生的领域。

假设你有一个计算器接口，Calculator，以及它的实现类CalculatorImpl，那么在系统还是单体应用时，你要调用Calculator的add方法来执行一个加运算，直接new一个CalculatorImpl，然后调用add方法就行了，这其实就是非常普通的本地函数调用，因为在同一个地址空间，或者说在同一块内存，所以通过方法栈和参数栈就可以实现。

![](https://upload-images.jianshu.io/upload_images/7143349-443a8cbcf6136ef5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/540)

现在，基于高性能和高可靠等因素的考虑，你决定将系统改造为分布式应用，将很多可以共享的功能都单独拎出来，比如上面说到的计算器，你单独把它放到一个服务里头，让别的服务去调用它。
![](https://upload-images.jianshu.io/upload_images/7143349-9b1fbd80b8db018b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

这下问题来了，服务A里头并没有CalculatorImpl这个类，那它要怎样调用服务B的CalculatorImpl的add方法呢？

有同学会说，可以模仿B/S架构的调用方式呀，在B服务暴露一个Restful接口，然后A服务通过调用这个Restful接口来间接调用CalculatorImpl的add方法。

很好，这已经很接近RPC了，不过如果是这样，那每次调用时，是不是都需要写一串发起http请求的代码呢？比如httpClient.sendRequest...之类的，能不能像本地调用一样，去发起远程调用，让使用者感知不到远程调用的过程呢，像这样：
```
@Reference
private Calculator calculator;

...

calculator.add(1,2);

...

```

这时候，有同学就会说，用代理模式呀！而且最好是结合Spring IoC一起使用，通过Spring注入calculator对象，注入时，如果扫描到对象加了@Reference注解，那么就给它生成一个代理对象，将这个代理对象放进容器中。而这个代理对象的内部，就是通过httpClient来实现RPC远程过程调用的。

可能上面这段描述比较抽象，不过这就是很多RPC框架要解决的问题和解决的思路，比如阿里的Dubbo。

总结一下，RPC要解决的两个问题：

解决分布式系统中，服务之间的调用问题。
远程调用时，要能够像本地调用一样方便，让调用者感知不到远程调用的逻辑。
如何实现一个RPC
实际情况下，RPC很少用到http协议来进行数据传输，毕竟我只是想传输一下数据而已，何必动用到一个文本传输的应用层协议呢，我为什么不直接使用二进制传输？比如直接用Java的Socket协议进行传输？

不管你用何种协议进行数据传输，一个完整的RPC过程，都可以用下面这张图来描述：

![](https://upload-images.jianshu.io/upload_images/7143349-9e00bb104b9e3867.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/263)
以左边的Client端为例，Application就是rpc的调用方，Client Stub就是我们上面说到的代理对象，也就是那个看起来像是Calculator的实现类，其实内部是通过rpc方式来进行远程调用的代理对象，至于Client Run-time Library，则是实现远程调用的工具包，比如jdk的Socket，最后通过底层网络实现实现数据的传输。

这个过程中最重要的就是序列化和反序列化了，因为数据传输的数据包必须是二进制的，你直接丢一个Java对象过去，人家可不认识，你必须把Java对象序列化为二进制格式，传给Server端，Server端接收到之后，再反序列化为Java对象。


RPC vs Restful
其实这两者并不是一个维度的概念，总得来说RPC涉及的维度更广。

如果硬要比较，那么可以从RPC风格的url和Restful风格的url上进行比较。

比如你提供一个查询订单的接口，用RPC风格，你可能会这样写：
```
/queryOrder?orderId=123
用Restful风格呢？

Get
/order?orderId=123

```
RPC是面向过程，Restful是面向资源，并且使用了Http动词。从这个维度上看，Restful风格的url在表述的精简性、可读性上都要更好。

RPC vs RMI
严格来说这两者也不是一个维度的。

RMI是Java提供的一种访问远程对象的协议，是已经实现好了的，可以直接用了。

而RPC呢？人家只是一种编程模型，并没有规定你具体要怎样实现，你甚至都可以在你的RPC框架里面使用RMI来实现数据的传输，比如Dubbo：Dubbo - rmi协议



dubbo是什么
dubbo是阿里巴巴开源的一套rpc方案，以为理念很契合微服务，这几年很火，用户里面不凡京东，当当，去哪儿等大公司。
rpc场景


dubbo架构
![dubbo](dubbo-architecture-roadmap.jpg)


官网也提供了一个很简单实用的demo来演示dubbo协议的使用，用起来的确很简单强大。

```
PYthon

#telnet 访问dubbo服务
#telnet 115.28.108.130 20880
import telnetlib
t = telnetlib.Telnet("115.28.108.130",20880)
t.write(bytes('invoke sayHello("hello world")\n','utf-8'))
r = t.read_until(bytes('ms.','utf-8'))
print(r.decode('utf-8'))
t.close()

```
