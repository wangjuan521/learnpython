#coding=utf-8
#@time   :2021/4/30  11:23
#@Author :wangjuan
# 从数据库查询账号是否存在
import mysql.connector
def connetdb():
    db = mysql.connector.connect(
        host="122.226.84.37",
        user="root",
        passwd="meidi",
        database="facilitator"
    )
    return db
# 查询表
def querytable(id6d):
    mydb = connetdb();
    circle = 0;
    # 数据库操作符
    mydatabase = mydb.cursor();
    mysql = "SELECT *from account WHERE id6d = "+id6d+";"
    mydatabase.execute(mysql);
    result = mydatabase.fetchall();
    print(result)
    row=mydatabase.rowcount
    return row
if __name__ == '__main__':
    querytable("10102164")



