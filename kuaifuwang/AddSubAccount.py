#coding=utf-8
#@time   :2021/4/23  10:37
#@Author :wangjuan
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import kuaifuwang.GetCookie as cookie
import Utlis.HttpTools as httptool
import Utlis.UrlTool as urltool
import string
import random
# 实例化对象，创建窗口
window = tk.Tk();
# 设置窗口的标题
window.title("71baomu快服网添加子账号");
# 获得屏幕的高度
screenh=window.winfo_screenheight();
# 获得屏幕的宽度
screenw=window.winfo_screenwidth();
# 窗口的宽度
wwidth = 600;
# 窗口的高度
wwheight = 400;
# 设置窗口的大小
window.geometry("%dx%d+%d+%d" %(wwidth,wwheight,(screenw-wwidth)/2,(screenh-wwheight)/2));
# 主账号变量，用于接收entry输入框输入的值
mainaccount = tk.StringVar();
# 接收输入框输入的子账号前缀的变量
subprefix = tk.StringVar();
# 设置选择邮箱格式的文本变量
subEmail = tk.StringVar();
# 设置添加子账号的数量变量文本
subaccountNum = tk.StringVar();
# 字体的属性,设置成全局变量
font=("黑体",13,'bold')
# 设置布局,包括标签，输入框，下拉框等的布局
def settingLayout():
    LabelLayout();
    EntryLayout();
    choiceBoxLayout();
    AddButton();
    # setTxtLayout();
# 界面所有标签的布局
def LabelLayout():
    # 主账号的标签
    MainAccLabel = tk.Label(window,text="请输入主账号",font=font);
    MainAccLabel.grid(row=0,column=0,ipady=10,sticky=E);

    # 要添加的子账号的前缀的标签
    subprefixLabel = tk.Label(window,text="请输入子账号的前缀",font=font);
    subprefixLabel.grid(row=1,column=0,sticky=E);

    # 子账号邮箱的格式标签
    subEmailLabel = tk.Label(window, text="请选择子账号的邮箱格式", font=font)
    subEmailLabel.grid(row=2, column=0,sticky =E,ipady=10);
    # 显示子账号数量的标签
    subNumsLabel = tk.Label(window, text="要添加子账号的数量", font=font)
    subNumsLabel.grid(row=3, column=0,sticky=E);
# 设置输入框的布局
def EntryLayout():
    # 主账号输入框，show=none显示成明文
    MainAccEntry = tk.Entry(window,show = None,textvariable = mainaccount,validate="key")\
                   .grid(row=0,column=1,sticky=W);
    # 子账号前缀输入框
    subprefixEntry = tk.Entry(window,textvariable = subprefix,validate="key")\
                   .grid(row=1,column=1,sticky=W);
# 选择下拉框布局
def choiceBoxLayout():
    subEmailBox = ttk.Combobox(window,textvariable = subEmail,width = 17);
    subEmailBox["values"] = ("@163.com","@126.com","@qq.com","@gmail.com",
                         "@sina.com","@linshiyouxiang.net");
    # 默认选择第一个
    subEmailBox.current(0);
    # 点击绑定事件
    subEmailBox.bind("<<ComboboxSelected>>",click)  # 绑定事件,(下拉列表框被选中时，绑定click()函数)
    subEmailBox.grid(row=2,column=1,sticky = W);
    # 添加子账号数量的下拉框
    subaccNumBox = Spinbox(window, from_=1, to=200, textvariable = subaccountNum,
                           validate="key",width =18)\
                   .grid(row=3,column=1,sticky = W)
# 邮箱格式下拉框点击事件
def click(*argvs):
    print('点击下拉框',subEmail.get());
# 按钮的布局
def AddButton():
    addbtn = tk.Button(window,text="添加",bg = "#1798FC",fg="white",width =6,
            command = addaccount)\
             .grid(row=5,column = 1,sticky = E,padx=15);
# 多行文本的布局
def setTxtLayout():
    showtext = tk.Text(window,height = 15,fg="red")
    showtext.grid(row =4,columnspan=2,sticky=W,padx=15,pady=10);
    showtext.insert(END,"jjjj\n");
# 添加子账号的事件
def addaccount():
    if mainaccount.get()=="":
        messagebox.showwarning("温馨提示","主账号不可为空")
    elif subprefix.get()=="":
        messagebox.showwarning("温馨提示", "子账号前缀不可为空")
    else:
        print("添加子账号")
        # 将主账号赋值给一个变量
        MainAccount = mainaccount.get();
        # 将子账号前缀赋值给一个变量
        subprefixstr = subprefix.get();
        # 获取子账号邮箱的后缀格式
        subEmailFormat = subEmail.get();
        print('邮箱的后缀格式是',subEmailFormat);
        # 获取cookie并赋值给变量字符串
        mycookie = cookie.getCookie();
        # 获取添加子账号的数量
        subaccountnum = int(subaccountNum.get());
        for i in range(subaccountnum):
            print("=======添加第%d位子账号===="%(i+1));
            subaccount = subprefixstr + "_" + "".join(random.sample(string.ascii_letters, 3)) + subEmailFormat;
            print("最终子账号是", subaccount);
            # 调用添加子账号的函数
            AddSubAccount(subaccount,MainAccount,mycookie);
# 请求获取添加子账号的链接
def requestGetUrl(subaccount,MainAccount,mycookie):
    header = {};
    header['Accept'] = "*/*";
    header['Accept-Encoding'] = "zh-CN,zh;q=0.9";
    header['Connection'] = "keep-alive";
    header['Cookie'] = mycookie;
    header['Host'] = 'www.71baomu.com';
    header['Referer'] = "http://www.71baomu.com/Cloud_Manage/?controller=user_regurl&action=index";
    header['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
     Chrome/75.0.3770.142 Safari/537.36";
    header['X-Requested-With'] = "XMLHttpRequest";
    mydata = {};
    mydata['controller'] = "user_regurl";
    mydata['action'] = 'getRegUrl';
    mydata['email'] = '';
    mydata['proxy'] = '';
    mydata['yx_from'] = '';
    mydata['sub_yx_from'] = '';
    mydata['active_email'] = '';
    mydata['sub_account_email'] = subaccount;
    mydata['account_email'] = MainAccount;
    # mydata['name'] = subAccount+"".join(random.sample(string.ascii_letters,3))+str(i+1);
    mydata['name'] = "";
    # mydata['name'] = sub_account+str(num);
    mydata['add_account_method'] = 'add_sub_account';
    mydata['old_account_email'] = '';
    mydata['mobile'] = '';
    mydata['domain_name'] = '';
    res = httptool.Send_Get(url=urltool.GetUrl,params=mydata,headers=header)
    print('===嘿嘿====',res.status_code,res.text);
    return res.text
def AddSubAccount(subaccount,MainAccount,mycookie):
    resurl = requestGetUrl(subaccount,MainAccount,mycookie)
    pattern = re.compile("&code=(.*)&t")
    # 获取code
    code = pattern.findall(resurl)[0]
    # 获取sign
    mypattern = re.compile("&c=(.*)");
    c = mypattern.findall(resurl)[0];
    mytimepattern = re.compile("&t=(.*)&c");
    # 获取timea
    mytime = mytimepattern.findall(resurl)[0];
    print(mytime)
    myheader = {};
    myheader['Accept'] = "*/*";
    myheader['Accept-Language'] = "zh-CN,zh;q=0.9";
    myheader['Origin'] = "http://www.71baomu.com";
    myheader['Content-Type'] = "application/x-www-form-urlencoded";
    myheader['Accept-Encoding'] = "gzip, deflate";
    myheader['Cookie'] = mycookie;
    myheader['Referer'] = resurl;
    myheader['X-Requested-With'] = "XMLHttpRequest";
    myheader['Connection'] = "keep-alive";
    myheader['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400"
    mydata = {};
    mymobile = '1' + str(random.randrange(3, 10)) + "".join(random.sample(string.digits, 9));
    mydata['mobile'] = mymobile;
    mydata['password'] = 'abcdefg1'
    mydata['master_account'] = MainAccount;
    mydata['sub_account'] = subaccount;
    mydata['csign'] = c;
    mydata['tsign'] = mytime
    mydata['ucode'] = code;
    res = httptool.Send_Post(url=urltool.AddaccountUrl,data=mydata,header=myheader)
    print("=======提交的参数是====", mydata)
    print("注册子账号的请求数据", res.text,res.status_code)
    showtext.insert(END,res.text+"\n")
if __name__ == '__main__':
    settingLayout();
    # 多行文本框用来多行展示添加子账号的信息
    showtext = tk.Text(window, height=15)
    showtext.grid(row=4, columnspan=2, sticky=W, padx=15, pady=10);
    # 主窗口循环显示
    window.mainloop()
