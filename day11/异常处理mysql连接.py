import pymysql
def mysql(sql):
    try:
        conn = pymysql.connect(**mysql_info)
    except Exception as e:
        res = '数据库连接失败，请检查链接信息%s '%e
        print(res)
        return  res
    # 在这里可以不写else，因为上面的语句return后直接跳出一场捕获了了
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        cur.execute(sql)
    except Exception as e:
        res = 'sql语法不符合要求，请检查%s'%e
        print(res)
    else:
        res = cur.fetchall()
    finally:
        cur.close()
        conn.close()
    return res