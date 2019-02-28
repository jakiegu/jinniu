class Phone():
    def __del__(self):
        print('我是析构函数')
    def call(self,name):
        print('为%s打call，为%s打电话'%(name,name))
    def __init__(self):
        self.test = 'abc'
        print('我是构造函数')
iphonex = Phone()
print(iphonex.test)
iphonex.call('gufeng')


