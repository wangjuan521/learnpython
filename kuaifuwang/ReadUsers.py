#coding=utf-8
#@time   :2021/6/22  14:48
#@Author :wangjuan
import requests
import string
import random
import re
userdic = {'user':[],'pwd':[]}
userlist = [];
def readuser():
    for i in range(5):
        phone = "1"+str(random.randrange(3,10))+ "".join(random.sample(string.digits, 9));
        print(phone)
        # choiceid = random.choice(getID());
        # print('====选择的客服id是',choiceid)
        url = "http://www.71baomu.com/?controller=test_One";
        mydata = {};
        mydata['action'] = "phone_reg";
        mydata['phone'] = phone;
        #mydata['phone'] = 12012345678;
        mydata['inner_user_id'] = 17;
        res = requests.get(url=url,params=mydata)
        print(res.text)
        patternpwd = '\"password\":\"(.*?)\"'
        pwd = re.findall(patternpwd, res.text)[0]
        patternuser = '\"email\":\"(.*?)\"'
        user = re.findall(patternuser, res.text)[0]
        userlist.append([user,pwd])
    print(userlist)
    return userlist
if __name__ == '__main__':
    readuser()