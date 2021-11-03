import time
class Cuook:
    __name = ""
    __age = 0
    def setname(self, name):
            self.__name =name

    def getname(self):
            return self.__name

    def setage(self,age):
        self.__age=age
    def getage(self):
        return self.__age

    def eat(self):
        print("厨师",self.getname(),"在做饭")

class zicuook(Cuook):
    def caook(self):
            print("厨师", self.getname(), "正在炒菜")

class cook(zicuook, Cuook):

        def cookm(self):
            print(self.getage(),"岁","厨师", self.getname(), "正在蒸饭,炒菜")

cuook=cook()
cuook.setname(11)
cuook.setage(19)
cuook.cookm()

class Phone(object):
    def __init__(self, brand):
        self.__brand = brand

    def call(self, number):
        print("正在用", self.__brand, "给", number, "打电话")

    def introduce(self):
        print('品牌为：', self.__brand, '的手机很好用')


class Cellphone(Phone):
    def newcall(self, number):
        print("语音拨号中")
        for i in range(5):
            print('.', end='')
            time.sleep(1)

        print('正在给', number, '打电话')

p = Phone('nubia')
c = Cellphone('大哥大')

c.call('123456789')
c.introduce()
c.newcall('987654321')

