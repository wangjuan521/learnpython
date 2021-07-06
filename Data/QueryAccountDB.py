#coding=utf-8
#@time   :2021/4/30  11:23
#@Author :wangjuan
# 从数据库查询账号是否存在
import mysql.connector
from config import ReadConfig
def connetdb(databasename):
    # 读取 config文件
    readconfig = ReadConfig.readconfig("../config/config.ini")
    db = mysql.connector.connect(
        host = readconfig[0],
        user = readconfig[1],
        passwd = readconfig[2],
        database= databasename
    )
    return db
# 查询表
def querytable(dataName,sql):
    # 连接数据库，传个数据库名称
    mydb = connetdb(dataName);
    circle = 0;
    # 数据库操作符
    mydatabase = mydb.cursor();
    # 执行 sql 语句
    mydatabase.execute(sql);
    result = mydatabase.fetchall();
    myid = result[0][0];
    return myid
if __name__ == '__main__':
    sql = "SELECT id FROM cloud_worker WHERE id6d = 10102164;"
    # 查询数据的表，传数据库名称和，sql语句
    querytable('53cloud',sql)



