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

class Use:
    __pinm = 0.0
    __jiag = 0.0
    __cpu = ""
    __neicun = 0.0
    __daij = 0.0

    def setpinm(self, pinm):
        if pinm < 0 or pinm > 40:
            print("这是电脑吗")
        else:
            self.__pinm = pinm

    def getpinm(self):
        return self.__pinm

    def setjiag(self, jiag):
        if jiag < 0 or jiag > 9999:
            print("什么电脑这么贵")
        else:
            self.__jiag=jiag
    def getjiag(self):
        return self.__jiag

    def cpu(self, cpu):
        print( "电脑cpu是",cpu)

    def setneic(self,neic):
        if neic <0 or neic>66666:
            print("有这么大的吗？")
        else:
            self.__neic=neic
    def getneic(self):
        return self.__neic

    def setdaij(self,daij):
        if daij <0 or daij >999:
            print("有这样的吗？")
        else:
            self.__daij=daij
    def getdaij(self):
        return self.__daij

    def eat(self,eatgame):
        print("上午在",eatgame)

    def sleep(self,dy):
        print("下午在",dy)

    def ame(self,lw):
        print("晚上在",lw)


    def showMe(self):
        print("电脑屏幕为", self.__pinm, "寸的,"
              , "电脑价格为", self.__jiag, "元,"
              ,"电脑的内存是",self.__neic,"t的"
              , "电脑已经待机了", self.__daij, "分钟"),

use = Use()
use.setpinm(20)
use.setjiag(7000)
use.cpu("晓龙")
use.setneic(1)
use.setdaij(5)

use.eat("玩游戏")
use.sleep("看电影")
use.ame("写论文")

use.showMe()
