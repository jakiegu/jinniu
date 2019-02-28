class Lw:
    money = 100000
    house = '10套'
    def kaiche(self):
        print('开车')
    def chouyan(self):
        print('抽烟')
    def hejiu(self):
        print('喝酒')
    def tangtou(self):
        print('烫头')
#小王继承老王
class Xw(Lw):
    def dayouxi(self):
        print('打游戏')
father = Lw()
son = Xw()
son.chouyan()
son.hejiu()
son.dayouxi()
father.hejiu()#father没有打游戏的方法

