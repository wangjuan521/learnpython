#coding=utf-8
#@time   :2021/4/22  14:46
#@Author :wangjuan
import requests
# 封装 post请求
def Send_Post(url,data,header=None):
    try:
        res = requests.post(url=url,data=data,headers=header)
        res.raise_for_status()
        print("======打印响应信息====",res.text)
    except Exception as e:
        print('异常信息是',e)
    finally:
        print('走这个方法了吗？')
        return res
# 封装 get 请求
def Send_Get(url,params,headers=None):
    if params is not None:
        try:
            res = requests.get(url=url,params=params,headers=headers)
            res.raise_for_status()
        except Exception as e:
            print('异常信息是',e)
        finally:
            return res
    else:
        try:
            res = requests.get(url=url,headers=headers)
            res.raise_for_status()
        except Exception as e:
            print('异常信息是',e)
        finally:
            return res