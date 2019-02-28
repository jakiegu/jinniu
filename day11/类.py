'''
People:类，类不能直接用，必须要实例化
'''
class People:
    eye = 2 #属性
    mouth = 1   #属性
    shengao = 180   #属性
    money = 1000000 #属性
    # def __init__(self): #构造函数，类在初始化做的一些操作
    #     print('生下来就会哭')
    def __init__(self,name): #构造函数，定义了参数，就必须要传参数
        self.name = name#通过这个语句，将变量变为全局
        print('实例化这个人的名字是%s'%name)

    def cry(self):  #方法
        print('哭...')

    def makemoney(self):    #方法
        print('self的内存地址',id(self))
        print('%s挣了20w'%self.name)


gufeng = People('gufeng')#实例化
# print('gufeng的内存地址',id(gufeng))
# gufeng.makemoney()#调用类下面的方法
# zhangsan = People('zhangsan')#实例化
# print('zhangsan的内存地址',id(zhangsan))
# zhangsan.makemoney()
People.makemoney(gufeng)

