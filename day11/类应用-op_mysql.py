import pymysql
class Mysql():
    # 初始化时链接mysql
    def __init__(self,host,user,password,db,port=3306,charset='utf8'):
        self.conn = pymysql.connect(
            host=host,
            user=user,
            db=db,
            password=password,
            port=port,
            charset=charset
        )
        #建立mysql游标
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    #返回多条sql语句，因为fetchall返回的是list，如果多条的话不方便[{},{},{}]
    def excute_many(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    # 返回单条sql语句，使用fecchone
    def excute_one(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchone()

    # 关闭mysql连接
    # def close_mysql(self):
    #     self.cur.close()
    #     self.conn.close()

    #将连接作为析构函数存在，就不需要手动关闭连接了
    def __del__(self):
        self.cur.close()
        self.conn.close()
        print('sql连接已经关闭')
db = Mysql('192.168.1.250','root','1q2w3e4r','choujiang')
res = db.excute_many('select * from app_myuser limit 20;')
print(res)
res = db.excute_one('select * from app_myuser where username="zhaokai";')
print(res)
# db.close_mysql()