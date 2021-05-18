# import re
# dict_email = {
#     r'[1-9]\d{4,7}@qq\.com$': 'qq邮箱',
#     r'[a-z1-9][a-z1-9_]{2,14}[a-z0-9]@sina\.com$': '新浪普通邮箱',
#     r'1[3456789]\d{9}@sina\.cn$': '新浪手机邮箱',
#     r'[a-zA-Z]\w{5,17}@163\.com$': '网易普通邮箱',
#     r'[a-zA-Z][a-zA-Z0-9_.]{4,19}@vip\.163\.com$': '网易VIP邮箱',
#     r'[a-zA-Z][a-zA-Z0-9_.]{4,19}@linshiyouxiang\.net$': '临时邮箱'
#     }
# def check(addr):
#     n = 1
#     for pattern, email in dict_email.items():
#         if re.match(pattern, addr):
#             print(f'{addr}为{email}')
#             break
#             return True
#         elif n == len(dict_email):
#             print(f'{addr}不是邮箱账号')
#             return False
#         else:
#             n += 1
# check('143379@qq.com')
# print(check('143379@qq.com'))
# check('143379@qq\.com')
# check('a823456@sina.com')
# check('a823456@sina.comg')
# check('15187632190@sina.cn')
# check('05187632190@sina.cn')
# check('A123456789@163.com')
# check('123456789A@163.com')
# check('a._0a2b3c@vip.163.com')
# check('fz0lunj2@linshiyouxiang.net')
#-*- coding:utf-8 -*-
import re

def checkmail(email):
    # str = r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$'
    str = r'[\w+\.]+@[a-zA-Z\d]+\.(com|cn|net)'
    if re.match(str,email):
        print('Email address is Right!')
        return True;
    else:
        print('Please reset your right Email address!')
        return False;
if __name__ == '__main__':
    res= checkmail("1@163.com");
    print(res)