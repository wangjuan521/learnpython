#coding=utf-8
#@time   :2021/5/26  14:14
#@Author :wangjuan
import logging
import os
def MakeLog(log_content):
    # 定义日志文件
    # logFile = logging.FileHandler(dirname('testlog1.txt','Log'),'a',encoding='utf-8')
    logFile = logging.FileHandler(dirname("Log","mylog.txt"), 'a', encoding='utf-8')
    # 设置log格式
    fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s');
    logFile.setFormatter(fmt)
    logger1 = logging.Logger('logTest',level=logging.DEBUG)
    logger1.addHandler(logFile)
    logger1.info(log_content)
    logFile.close();
def dirname(filepath,filename):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),filepath,filename)

if __name__ == '__main__':
    MakeLog("====生成log文件====")
