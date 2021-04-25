#coding=utf-8
#@time   :2021/4/25  14:40
#@Author :wangjuan
from tkinter import *
import webbrowser
from tkinter import messagebox

class Application(Frame):
    """一个经典的GUI程序的写法"""

    def __init__(self, master=None):
        super().__init__(master)  # super代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """创建组件"""
        self.w1 = Text(root, width=60, height=18, bg='gray')
        self.w1.pack()

        self.w1.insert(1.0, '悟空')  # 1.0:第一行，第零列
        self.w1.insert(2.0, '孙悟空，又呼“行者”，\n'
                            '出身东胜神洲傲来国花果山水帘洞，\n'
                            '金水为真空之性，悟得此空，\n'
                            '还须行得此空，而金水攒矣。')
        Button(self, text='重复插入文本', command=self.newText).pack(side='left')
        Button(self, text='返回文本', command=self.allText).pack(side='left')
        Button(self, text='添加图片', command=self.newPhoto).pack(side='left')
        Button(self, text='添加组件', command=self.newSpare).pack(side='left')
        Button(self, text='通过 tag 精确控制文本 ', command=self.testTag
               ).pack(side='left')

    def newText(self):
        self.w1.insert(INSERT, '西游记')
        # INSERT表示再光标处插入
        self.w1.insert(END, '插入')
        # END表示在最后插入
        self.w1.insert(1.4, '大圣归来')

    def allText(self):
        """
        Indexes(索引)是用来指向Text组件中文本的位置，
        Text的组件索引也是对应实际字符之间的位置
        核心：行号以1开始，列号以0开始
        """
        print(self.w1.get(1.1, 1.5))
        print('所有的文本内容：\n' + self.w1.get(1.0, END))

    def newPhoto(self):
        global photo
        self.photo = PhotoImage(file='photo/222.gif')
        self.w1.image_create(END, image=self.photo)

    def newSpare(self):
        b1 = Button(self.w1, text='python')
        self.w1.window_create(INSERT, window=b1)
        '''在Text创建组件的命令'''

    def testTag(self):
        self.w1.delete(1.0, END)
        self.w1.insert(INSERT, '悟空长的高万丈，头如泰山，\n'
                               '腰如峻岭，眼如闪电，\n'
                               '口似血盆，牙如剑戟；\n'
                               '手中那棒，上抵三十三天，\n'
                               '下至十八层地狱。\n'
                               '百度，百度一下你就知道')
        self.w1.tag_add('悟空', 1.0, 1.2)
        self.w1.tag_config('悟空', background='yellow', foreground='red')
        self.w1.tag_add('百度', 6.0, 6.2)
        self.w1.tag_config('百度', underline=True)
        self.w1.tag_bind('百度', "<Button-1>", self.webshow)

    def webshow(self, event):
        webbrowser.open('www.baidu.com')


if __name__ == "__main__":
    root = Tk()
    root.geometry('400x300+200+200')
    app = Application(master=root)
    root.mainloop()