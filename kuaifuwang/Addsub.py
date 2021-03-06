#coding=utf-8
#@time   :2021/4/29  10:01
#@Author :wangjuan
'''
这是快服网后台添加子账号的接口，可批量添加子账号
'''
import tkinter as tk
from tkinter import *
import Base.LoginBasePage as loginpage
from tkinter import ttk
import tkinter.messagebox as mbox
import kuaifuwang.GetCookie as cookie
import Utlis.HttpTools as httptool
import Utlis.UrlTool as urltool
import string
import random
import Utlis.checkexpress as expresstool
import re
# 字体的属性,设置成全局变量
font=("黑体",13,'bold')

class addsubaccount():
    def __init__(self, master):
        self.master = master
        self.addface1 = tk.Frame(self.master, )
        self.addface1.pack()
        # 控制输入框的输入只能输入数字
        self.inputCMD=self.addface1.register(self.inputnum)
        # 控制输入框的输入只能输入字母
        self.subInputCMD = self.addface1.register(self.subinput)
        # 主账号变量，用于接收entry输入框输入的值
        self.mainaccount = tk.StringVar();
        # 接收输入框输入的子账号前缀的变量
        self.subprefix = tk.StringVar();
        # 设置选择邮箱格式的文本变量
        self.subEmail = tk.StringVar();
        # 设置添加子账号的数量变量文本
        self.subaccountNum = tk.StringVar();
        # 用于接收输入框输入的子账号密码
        self.subpwdtext = tk.StringVar();
        # 标签的布局
        self.LabelLayout();
        # 输入框的布局
        self.EntryLayout();
        # 下拉框的布局
        self.choiceBoxLayout();
        # 按钮的布局
        self.AddButton();
        # 多行文本框用来多行展示添加子账号的信息
        self.showtext = tk.Text(self.addface1, height=15)
        self.showtext.grid(row=5, columnspan=2, sticky=W, padx=15);
    # 监听只能输入数字
    def inputnum(self,content):
        if content.isdigit() or content == "":
            return True
        else:
            return False
    def subinput(self,content):
        return all(ord(c) < 128 for c in content)
    def LabelLayout(self):
        # 主账号的标签
        MainAccLabel = tk.Label(self.addface1, text="请输入主账号邮箱", font=font);
        MainAccLabel.grid(row=0, column=0, ipady=7, sticky=E);
        # 要添加的子账号的前缀的标签
        subprefixLabel = tk.Label(self.addface1, text="请输入子账号的前缀", font=font);
        subprefixLabel.grid(row=1, column=0, sticky=E);
        # 子账号邮箱的格式标签
        subEmailLabel = tk.Label(self.addface1, text="请选择子账号的邮箱格式", font=font)
        subEmailLabel.grid(row=2, column=0, sticky=E, ipady=7);
        # 显示子账号数量的标签
        subNumsLabel = tk.Label(self.addface1, text="要添加子账号的数量", font=font)
        subNumsLabel.grid(row=3, column=0, sticky=E);
    #   子账号的密码标签
        subaccpwdLabel = tk.Label(self.addface1, text="请设置子账号的密码", font=font)
        subaccpwdLabel.grid(row=4, column=0, sticky=E,pady=7);
    # 设置输入框的布局
    def EntryLayout(self):
        # 主账号输入框，show=none显示成明文
        MainAccEntry = tk.Entry(self.addface1,show = None,textvariable = self.mainaccount,validate="key")
        MainAccEntry.grid(row=0,column=1,sticky=W);
        # 子账号前缀输入框
        subprefixEntry = tk.Entry(self.addface1,textvariable = self.subprefix,validate="key",validatecommand=(self.subInputCMD, '%P'))
        subprefixEntry.grid(row=1,column=1,sticky=W);
    #   子账号密码输入框
        self.subpwdEntry = tk.Entry(self.addface1,textvariable = self.subpwdtext,validate="key")
        self.subpwdEntry.grid(row=4,column=1,sticky=W);
    # 选择下拉框布局
    def choiceBoxLayout(self):
        subEmailBox = ttk.Combobox(self.addface1, textvariable=self.subEmail, width=17);
        subEmailBox["values"] = ("@163.com", "@126.com", "@qq.com", "@gmail.com",
                                 "@sina.com", "@linshiyouxiang.net","@139.com");
        # 默认选择第一个
        subEmailBox.current(0);
        # 点击绑定事件
        subEmailBox.bind("<<ComboboxSelected>>",self.click)  # 绑定事件,(下拉列表框被选中时，绑定click()函数)
        subEmailBox.grid(row=2, column=1, sticky=W);
        # 添加子账号数量的下拉框
        subaccNumBox = Spinbox(self.addface1, from_=5, to=200, textvariable=self.subaccountNum,
                               validate="key", validatecommand=(self.inputCMD,'%P'),width=18) \
            .grid(row=3, column=1, sticky=W)
    # 邮箱格式下拉框点击事件
    def click(self,*argvs):
        print('点击下拉框',self.subEmail.get());

    # 按钮的布局
    def AddButton(self):
        addbtn = tk.Button(self.addface1, text="添加", bg="#1798FC", fg="white", width=6,
                           command=self.addaccount)
        addbtn.grid(row=6, column=1, sticky=E, padx=15,pady=5);
        btn_back = tk.Button(self.addface1, text='返回主界面', bg="#1798FC", fg="white",
                             command=self.back)
        btn_back.grid(row=6, column=1, sticky=E, padx=80);
    # 添加子账号的事件
    def addaccount(self):
        subEmailFormatList = ["@163.com", "@126.com", "@qq.com", "@gmail.com",
                                 "@sina.com", "@linshiyouxiang.net","@139.com"];
        if self.mainaccount.get() == "" or self.mainaccount.get().isspace():
            mbox.showerror("温馨提示","主账号邮箱不可为空")
            # self.messagebox.showwarning("温馨提示", "主账号不可为空")
        elif self.subprefix.get() == "" or self.subprefix.get().isspace():
            mbox.showerror("温馨提示", "子账号前缀不可为空")
        elif self.subaccountNum.get()=="" or self.subaccountNum.get().isspace():
            mbox.showerror("温馨提示", "要模拟的子账号数量不可为空")
        elif self.subEmail.get()=="" or self.subEmail.get().isspace():
            mbox.showwarning("温馨提示","子账号的邮箱后缀不可为空")
        elif self.subpwdtext.get()=="" or self.subpwdtext.get().isspace():
            mbox.showwarning("温馨提示", "子账号的密码不可为空")
        elif self.subEmail.get() not in subEmailFormatList:
            mbox.showwarning(title="温馨提示",message="子账号的后缀格式不正确")
        else:
            # 将主账号赋值给一个变量
            MainAccount = self.mainaccount.get();
            if expresstool.checkmail(MainAccount) == False:
                mbox.showerror("温馨提示","请输入正确的邮箱账号")
            else:
                # 将子账号前缀赋值给一个变量
                subprefixstr = self.subprefix.get();
                # 获取子账号邮箱的后缀格式
                subEmailFormat = self.subEmail.get();
                # 要设置的子账号的密码
                subpwd = self.subpwdtext.get()
                print('邮箱的后缀格式是', subEmailFormat);
                # 获取cookie并赋值给变量字符串
                mycookie = cookie.getCookie();
                # 获取添加子账号的数量
                subaccountnum = int(self.subaccountNum.get());
                for i in range(subaccountnum):
                    print("=======添加第%d位子账号====" % (i + 1));
                    subaccount = subprefixstr + "".join(random.sample(string.digits+string.ascii_letters,6)) + subEmailFormat;
                    print("最终子账号是", subaccount);
                    # 调用添加子账号的函数
                    self.AddSubAccount(subaccount, MainAccount, mycookie,subpwd);
    # 请求获取添加子账号的链接
    def requestGetUrl(self,subaccount, MainAccount, mycookie):
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
        mydata['name'] = self.subprefix.get()+"".join(random.sample(string.ascii_letters,3));
        mydata['add_account_method'] = 'add_sub_account';
        mydata['old_account_email'] = '';
        mydata['mobile'] = '';
        mydata['domain_name'] = '';
        res = httptool.Send_Get(url=urltool.GetUrl, params=mydata, headers=header)
        return res.text
    # 添加子账号的接口
    def AddSubAccount(self,subaccount, MainAccount, mycookie,subpwd):
        resurl = self.requestGetUrl(subaccount, MainAccount, mycookie)
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
        mydata['password'] = subpwd;
        mydata['master_account'] = MainAccount;
        mydata['sub_account'] = subaccount;
        mydata['csign'] = c;
        mydata['tsign'] = mytime
        mydata['ucode'] = code;
        res = httptool.Send_Post(url=urltool.AddaccountUrl, data=mydata, header=myheader)
        print("=======提交的参数是====", mydata)
        print("注册子账号的请求数据", res.text, res.status_code)
        self.showtext.insert(END, res.text + "\n")
        patternstatus = '\"status\":\"(.*?)\"'
        statusstr = re.findall(patternstatus, res.text)[0]
        print("我要把你打印出来",statusstr,res.json(),type(res.json()))
        if statusstr == "success":
            self.showtext.insert(END,"=====恭喜您，子账号"+subaccount+"添加成功====="+"\n")
        else:
            patternmsg = '\"msg\":\"(.*)\"'
            msg = re.findall(patternmsg,res.text)[0]
            # 将 unicode 转中文
            msgstr = msg.encode().decode("unicode_escape");
            self.showtext.insert(END,"======子账号"+subaccount+"添加失败，"+"失败原因是："+msgstr+"======"+"\n")
            # 返回主界面
    def back(self):
        self.addface1.destroy()
        loginpage.initfacepage(self.master);
