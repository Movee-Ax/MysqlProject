import tkinter as tk
import tkinter.messagebox

top = tk.Tk()
top.title("系统登录！！")  # 创建窗口名
top.geometry("500x500")  # 设置像素
l1 = tk.Label(top, text="用户名：", font=("黑体", 10))
l1.place(x="50", y="10")
l2 = tk.Label(top, text="密码：", font=("黑体", 10))
l2.place(x="50", y="40")
result = tk.StringVar()
text1 = tk.Entry(top, textvariable=result)
text1.place(x="120", y="10")
result2 = tk.StringVar()
text2 = tk.Entry(top, textvariable=result2)
text2.place(x="120", y="40")


# 声明函数


def okqqq():
    name_no = "张三"
    password_no = "1234567"
    name = text1.get()
    password = text2.get()
    if name == name_no:
        if password == password_no:
            tkinter.messagebox.askokcancel(title='yes', message='用户名和密码正确！')
            result.set(""), result2.set("")
        else:
            tkinter.messagebox.askokcancel(title='密码错误', message='密码错误，请重新输入！')
            result.set(""), result2.set("")
    else:
        # if password == 1234567:
        if password == password_no:
            tkinter.messagebox.askokcancel(title='用户名错误', message='用户名错误，请重新输入！')
            result.set(""), result2.set("")
        else:
            tkinter.messagebox.askokcancel(title='用户名和密码错误', message='用户名和密码错误，请重新输入！')
            result.set(""), result2.set("")


btn = tk.Button(top, text="登陆！！", font=("黑体", 10), command=okqqq)
btn.place(x=190, y=70)
top.mainloop()