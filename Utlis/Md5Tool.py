#coding=utf-8
#@time   :2021/5/6  13:19
#@Author :wangjuan
import hashlib  # 导入 hashlib模块，完成MD5加密操作
def GetMd5Str(str):
    # 创建 MD5对象，Md5是固定的，不能反鲜，关系一一对应
    h1 = hashlib.md5();
    # 加密某个字符串，则必须以 utf-8的形式encode
    h1.update(str.encode(encoding='utf-8'))
    print('MD5加密前为 ：' + str)
    # 用 hexdigest 拿到加密字符串
    md5str = h1.hexdigest();
    print('MD5加密后：'+md5str)
    return md5str
if __name__ == '__main__':
    GetMd5Str('');
