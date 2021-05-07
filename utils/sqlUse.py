import pymysql


def get_list(sql, args):
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='mj031017',
        db='drugstore',
        charset='utf8'
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    result_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return result_list


def get_one(sql, args):
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='mj031017',
        db='drugstore',
        charset='utf8'
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    result_list = cursor.fetchone()
    cursor.close()
    conn.close()
    return result_list


def modify(sql, args):
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='mj031017',
        db='drugstore',
        charset='utf8'
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    conn.commit()
    cursor.close()
    conn.close()