# _*_ coding:utf-8 _*_

import os
import pymysql


def get_sql_files():  # 从文件夹中批量读取sql文件，返回sql文件
    sql_files = []
    # files = os.listdir(os.path.dirname(os.path.abspath(__file__)))
    files = os.listdir(r"C:\Users\示弱\Desktop\毕业设计等\sql")
    for file in files:
        if os.path.splitext(file)[1] == '.sql':
            sql_files.append(file)

    return sql_files


def execute_fromfile(filename, cursor):  # 封装一个读取sql文件中的sql语句，并执行语句的方法
    fd = open(filename, 'r', encoding='utf-8')  # 以只读的方式打开sql文件
    sqlfile = fd.read()  # 读取文件内容
    fd.close()
    sqlcommamds = sqlfile.split(';')  # 以;切割文件内容，获取单个sql语句

    for command in sqlcommamds:
        try:
            cursor.execute(command)
            # cur = cursor.execute(command)  # 执行每个sql语句
            # print('sql执行成功:', cur)
        except Exception as msg:
            print("错误信息： ", msg)

    print('sql执行完成')


def connect_mysql():  # 创建数据路连接，调用读sql文件和执行sql语句方法，达到批量执行sql文件的目的
    # 建立连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='dsq171007', db='bysj')
    print("连接数据库成功")
    # 获取游标对象
    cursor = conn.cursor()
    # 执行sql语句-查询
    # count = cursor.execute("select * from tebl_acct_bs_sgmt")
    # print(count)
    # 执行sql
    for file in get_sql_files():
        filename = r"C:\Users\示弱\Desktop\毕业设计等\sql\\" + file
        # print(filename)
        execute_fromfile(filename, cursor)

    # 关闭连接
    conn.close()


if __name__ == '__main__':
    connect_mysql()