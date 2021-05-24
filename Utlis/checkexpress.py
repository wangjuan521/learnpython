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