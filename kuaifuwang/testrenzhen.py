#coding=utf-8
#@time   :2021/5/12  15:07
#@Author :wangjuan
import Utlis.Md5Tool as md5tool
import Utlis.HttpTools as httptool
infodata = {};
infodata['company_id'] = "72155998";
infodata['organization_name'] = "kftest的电子商务有限公司";
infodata['organization_num'] = '123456';
infodata['legal_person_tel'] = '17604618635';
infodata['legal_person_idCard'] = "342623199911177535"
infodata['attestation_type'] = "4";
infodata['legal_person_name'] = "王宏安"
infodata['address'] = "安徽省,无为县,十里墩乡";
infodata['legal_industry'] = '2030000'
teststr = "fyweao&@^#()@)#!><?F";
for key,value in infodata.items():
    print(key,value)
    teststr += value;
print(teststr)
key = md5tool.GetMd5Str(teststr)
url =  "http://www.kuaifuwang.com.cn/interface/index.php?controller=attestation&action=syncAuthentication&key="+key;
print("====key=====",key)
res = httptool.Send_Post(url=url,data=infodata)
print('====嘿嘿====',res.text)