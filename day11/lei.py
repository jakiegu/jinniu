import pymysql
def con_db():
    conn = pymysql.connect(host='118.24.3.40',user='jxz',
                           password='123456',db='jxz')
    cur = conn.cursor()
    return conn,cur