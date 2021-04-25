#coding=utf-8
#@time   :2021/4/22  14:46
#@Author :wangjuan
import requests
# 封装 post请求
def Send_Post(url,data,header=None):
    try:
        res = requests.post(url=url,data=data,headers=header,timeout=5)
        res.raise_for_status()
        print("======打印响应信息====",res.text)
    except Exception as e:
        print('异常信息是',e)
    else:
        return res
# 封装 get 请求
def Send_Get(url,params,header=None):
    if params is not None:
        try:
            res = requests.get(url=url,params=params,header=header,timeout=5)
            res.raise_for_status()
        except Exception as e:
            print('异常信息是',e)
        finally:
            return res
    else:
        try:
            res = requests.get(url=url,header=header,timeout=5)
            res.raise_for_status()
        except Exception as e:
            print('异常信息是',e)
        finally:
            return res