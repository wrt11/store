class User:
    __gd = 0.0
    __rj = 0.0
    __color = ""
    __cz = ""
    __yt = ""

    def setgd(self, gd):
        if gd < 0 or gd > 30:
            print("这是水杯吗")
        else:
            self.__gd = gd

    def getgd(self):
        return self.__gd

    def setrj(self, rj):
        if rj < 0 or rj > 1000:
            print("这是水杯吗？")
        else:
            self.__rj = rj

    def getrj(self):
        return self.__rj

    def setColor(self, color):
        if color == "":
            print("颜色非法，别瞎弄！")
        else:
            self.__color = color

    def getColor(self):
        return self.__color

    def setcz(self, cz):
        if cz == "":
            print("材料非法！")
        else:
            self.__cz = cz

    def getVolume(self):
        return self.__cz

    def yt(self,yt):
        print(self.__cz,"材料的杯子可以放",yt,"类型的液体")



        print("水杯高度为", self.__gd, "厘米,"
              , "容量为", self.__rj, "毫升,"
              , "材料是由", self.__cz, "组成的,"
              , "它的颜色是",self.__color,"的"),


user = User()
user.setgd(15)
user.setrj(700)
user.setColor("黑色")
user.setcz("玻璃")
user.yt("可乐")

