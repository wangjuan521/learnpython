#coding=utf-8
#@time   :2021/4/28  13:10
#@Author :wangjuan
import tkinter as tk
from GUI.Guidemo2 import face1
class basedesk():
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.title('Base page')
        self.root.geometry('200x200')
        initface(self.root);
class initface():
    def __init__(self, master):
        self.master = master
        self.master.config(bg='green')
        # 基准界面initface
        self.initface = tk.Frame(self.master, )
        self.initface.pack()
        self.initface.config(bg='yellow')
        btn = tk.Button(self.initface, text='change', command=self.change)
        btn.grid(row=0,column=0);
        btn1 = tk.Button(self.initface, text='change', command=self.change)
        btn1.grid(row=1,column=0);
    def change(self, ):
        self.initface.destroy()
        face1(self.master)

if __name__ == '__main__':
    root = tk.Tk()
    basedesk(root)
    root.mainloop()
