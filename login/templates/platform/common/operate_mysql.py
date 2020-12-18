import pymysql
from login.templates.utils.getconf import get_conf


def select(sql, db):
    '''audiobook、yyting_partdb库查询
    :param sql 数据库语句
    :param db 数据库名称
    :return list
    '''
    conn = pymysql.connect(host=get_conf('mysql', 'host'), user=get_conf('mysql', 'username'),
                           password=get_conf('mysql', 'password'), database=get_conf('mysql', db), charset='utf8mb4')
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        cur.execute(sql)
        res = cur.fetchall()
    except:
        cur.rollback()
    cur.close()
    conn.close()
    return res


def select_platform(sql):
    '''platform库查询
    :param sql 数据库语句
    :param db 数据库名称
    :return list
    '''
    conn = pymysql.connect(host=get_conf('mysql_platform', 'host'), user=get_conf('mysql_platform', 'username'),
                           password=get_conf('mysql_platform', 'password'), database='platform', charset='utf8mb4')
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        cur.execute(sql)
        res = cur.fetchall()
    except:
        cur.rollback()
    cur.close()
    conn.close()
    return res
def select_billing(sql):
    '''billing库查询
    :param sql 数据库语句
    :param db 数据库名称
    :return list
    '''
    conn = pymysql.connect(host=get_conf('mysql_billing', 'host'), user=get_conf('mysql_billing', 'username'),
                           password=get_conf('mysql_billing', 'password'), database='billing', charset='utf8mb4')
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        cur.execute(sql)
        res = cur.fetchall()
    except:
        cur.rollback()
    cur.close()
    conn.close()
    return res
def select_readbook(sql):
    '''readbook库查询
    :param sql 数据库语句
    :param db 数据库名称
    :return list
    '''
    conn = pymysql.connect(host=get_conf('mysql_readbook', 'host'), user=get_conf('mysql_readbook', 'username'),
                           password=get_conf('mysql_readbook', 'password'), database='readbook', charset='utf8mb4')
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        cur.execute(sql)
        res = cur.fetchall()
    except:
        cur.rollback()
    cur.close()
    conn.close()
    return res
def select_yystory(sql):
    '''yystory库查询
    :param sql 数据库语句
    :param db 数据库名称
    :return list
    '''
    conn = pymysql.connect(host=get_conf('mysql_yystory', 'host'), user=get_conf('mysql_yystory', 'username'),
                           password=get_conf('mysql_yystory', 'password'), database='yystory', charset='utf8mb4')
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        cur.execute(sql)
        res = cur.fetchall()
    except:
        cur.rollback()
    cur.close()
    conn.close()
    return res
# def billing_delete(sql, db):
#     '''billing,readbook,platform库删除操作
#     :param sql 数据库语句
#     :param db 数据库名称
#     :return list
#     '''
#     conn = pymysql.connect(host=get_conf('mysql_platform', 'host'), user=get_conf('mysql_platform', 'username'),
#                            password=get_conf('mysql_platform', 'password'), database=db, charset='utf8mb4')
#     #使用cursor()方法获取操作游标
#     cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
#     try:
#         #执行sql语句
#         cur.execute(sql)
#         #提交修改
#         conn.commit()
#     except:
#         # 发生错误时回滚
#         cur.rollback()
#     # 关闭连接
#     conn.close()
#     cur.close()
