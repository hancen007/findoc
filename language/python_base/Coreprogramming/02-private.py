class Test (object):
    def __init__(self):
        self.num = 100
    def setNum(self,newNum):
        self.__num = newNum

    def getNum(self):
        return self.__num
