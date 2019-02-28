class People:
    country = 'china'#类变量，公共的
    def __init__(self,name,sex):
        self.name = name#实例变量
        self.sex = sex#实例变量
    def say(self):
        print('name'+self.name)
        print('sex'+self.sex)
        print('country'+self.country)
    @property#加上property，把一个函数变为一个变量，这个变量的值的就是函数的返回值
    def get_name(self):
        return self.name
gufeng = People('gufeng','male')
gufeng.say()
print(gufeng.get_name)
gufeng.get_name()