#coding=utf-8
#@time   :2021/6/16  13:30
#@Author :wangjuan
import yaml
def readUser(filename):
    f = open(filename,'r',encoding='utf-8')
    users = yaml.load(f,Loader=yaml.FullLoader)
    f.close()
    return users