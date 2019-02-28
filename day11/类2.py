class Car():
    def __init__(self,color,pl):#pl：排量
        self.color = color
        self.pl = pl
        pass
    def add_fun(self,fun):
        self.fun = fun
        print('颜色是%s'%self.color)
        print('排量是%s' % self.pl)
bmw = Car('红色','3.5L')
bmw.add_fun('水陆两膝')