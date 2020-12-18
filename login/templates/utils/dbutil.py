# coding=utf-8
import pymysql.cursors
from login.templates.utils import getconf
from login.templates.utils.getconf import get_conf

# 查
# def select(sql, dbname, host=getconf.get_conf("mysql", "host"), user=getconf.get_conf("mysql", "username"),
#            password=getconf.get_conf("mysql", "password")):
#     print('****当前SQL****------------------------------host：' + host)
#     print('****当前SQL****：' + sql)
#     try:
#         connection = pymysql.connect(host=host,
#                                      user=user,
#                                      password=password,
#                                      db=getconf.get_conf("mysql", dbname),
#                                      charset='utf8mb4',
#                                      cursorclass=pymysql.cursors.DictCursor)
#         cursor = connection.cursor()
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         return result
#     except Exception as e:
#         print('查询出错:%s' % e)
#     finally:
#         cursor.close()
#         connection.close()

def select(sql, db):
    '''audiobook、yyting_partdb库查询
    :param sql 数据库语句
    :param db 数据库名称
    :return list
    '''
    conn = pymysql.connect(host=get_conf('mysql', 'host'),
                           port=3306,
                           user=get_conf('mysql', 'username'),
                           password=get_conf('mysql', 'password'),
                           database=get_conf('mysql', db),
                           charset='utf8mb4')
    ##游标设置为字典类型
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        cur.execute(sql)
        res = cur.fetchall()
    except Exception as e:
        print(str(e))
    cur.close()
    conn.close()
    return res


# 改
def update(sql, dbname, host=getconf.get_conf("mysql", "host"), user=getconf.get_conf("mysql", "username"),
           password=getconf.get_conf("mysql", "password")):
    print('****当前SQL****：' + sql)
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 db=getconf.get_conf("mysql", dbname),
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()
