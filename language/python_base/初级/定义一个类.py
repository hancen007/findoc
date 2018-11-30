class Cat:
    #属性
    def __init__(self):
        self.name = "yanyan"
        self.color = "black"
    def __str__(self):
        return self.name
    #方法
    def eat(self):
        print("猫在吃鱼....%s"%self.name)

    def __send_message(self):
        print("send message")

    def verfir_menoy(self,menoy):
        if menoy > 100:
            self.__send_message()

    def drink(self):
        print("猫正在喝kele.....")

class jiaficat(Cat):
    def itcolor(self):
        print('棕色的')

class backcat(Cat):
    def itcolor(self):
        print('黑色')
#多继承
class muticat(jiaficat,backcat):
    pass

class parcat(jiaficat,super):
    def itcolor(self):
        print('重写的棕色的')
        #调用父级的方法
        #jiaficat.itcolor(self)
        super.itcolor()


bcat = Cat()
print(bcat)
