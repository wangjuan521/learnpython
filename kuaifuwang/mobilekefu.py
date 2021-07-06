#coding=utf-8
#@time   :2021/6/4  10:01
#@Author :wangjuan
'''
手机端掌上客服登录接口
'''
import requests
import threading
def requestnewsaas(Arg):
    myurl = "https://newsaas.71baomu.com/saas"
    mydata = {}
    mydata['action'] = "SdkGuestLgn"
    mydata['app_key'] = "A0640E45E1DE40E490E99F572EE6A6BF"
    mydata['type'] = 0;
    # mydata['arg'] = "10013099";
    mydata['arg'] = Arg;
    while(1):
        try :
            res = requests.post(url=myurl,data=mydata)
            res.raise_for_status()
        except requests.RequestException as e:
            print('异常信息是',e)
        finally:
            print(res.json())
if __name__ == '__main__':
    Arg = "10013099";
    for i in range(50):
        try:
            t1 = threading.Thread(target=requestnewsaas, args=(Arg,), name="Thread-" + str(i))
            t1.start()
        except Exception as e:
            print('=======线程报错原因======', e)
        else:
            pass

        # requestnewsaas()
