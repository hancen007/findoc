class Test (object):
    def __init__(self):
        self.num = 100
    def setNum(self,newNum):
        self.__num = newNum
    def getNum(self):
        return self.__num

    def __pr(self):
        print("私有变量")

    num = property(getNum,setNum)

t =Test()
t.num = 200
t.num = 300
t.__pr

#print(t.getNum())
print(t.num)
