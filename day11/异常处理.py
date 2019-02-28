# s = 'a'
# print(int(s))
# import pymysql
# conn = pymysql.connect(host='118.24.3.40',user='jxz',password='123456',db='jxz')
# cur = conn.cursor()
# cur.execute('select * from a;')
# # 遇到一场就不走下面的print了
# print('aaa')
# def calc(a,b):
#     try:
#         return a/b
#     # except ZeroDivisionError as e:
#     #     res = '除数不能为0，%s'%e
#     # except TypeError as e:#多个异常直接后面写
#     #     res = '类型错误，只能是数字类型%s'%e
#     except Exception as e:
#         print(e)
#     # return res
# res = calc(10,1)
# print(res)
# res = calc('k',1) #报错信息为：TypeError
# print(res)
# res = calc(10,0) #报错信息为：ZeroDivisionError
# print(res)

money = input('enter:')
try:
    money = int(money)
except Exception as e:  #产生异常走这边
    print('输入金额错误！')
else:   #不产生异常走这里
    print(money+1)
finally:
    print('什么时候执行finally！')
