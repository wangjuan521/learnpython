#coding=utf-8
#@time   :2021/6/22  13:15
#@Author :wangjuan
import configparser   #导入配置模块
def readconfig(filename):
    savedata = [];
    # 创建 configparser 对象
    cf = configparser.ConfigParser()
    # 读取文件内容
    filename = cf.read(filename,encoding="utf-8")
    # 获取所有的 senctions以列表的形式返回
    sec = cf.sections();
    # # 得到某 sections下的所有的option
    # opt = cf.options('Database')
    # print(opt)
    # 得到 section下的所有键值对
    value = cf.items('Database')
    host = cf.get("Database","host")
    user = cf.get("Database","user")
    passwd = cf.get("Database","passwd")
    savedata.append(host)
    savedata.append(user)
    savedata.append(passwd)
    return savedata;
if __name__ == '__main__':
    readconfig();
