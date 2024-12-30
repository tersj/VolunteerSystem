import pymysql
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *  # 图形界面库
import tkinter.messagebox as messagebox  # 弹窗


class StartPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁子界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('校园志愿者招募平台')
        self.window.geometry('300x470')

        label = Label(self.window, text="校园志愿者招募平台", font=("Verdana", 20))
        label.pack(pady=100)  # pady=100 界面的长度

        Button(self.window, text="管理员登陆", font=tkFont.Font(size=16), command=lambda: AdminPage(self.window), width=30,
               height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="学生登陆", font=tkFont.Font(size=16), command=lambda: StudentPage(self.window), width=30,
               height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="注册系统", font=tkFont.Font(size=16), command=lambda: AboutPage(self.window),
               width=30,
               height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text='退出系统', height=2, font=tkFont.Font(size=16), width=30, command=self.window.destroy,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()

        self.window.mainloop()  # 主消息循环


# 管理员登陆页面
class AdminPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('管理员登陆页面')
        self.window.geometry('300x450')

        label = tk.Label(self.window, text='管理员登陆', bg='green', font=('Verdana', 20), width=30, height=2)
        label.pack()

        Label(self.window, text='管理员账号：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_userid = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.admin_userid.pack()

        Label(self.window, text='管理员密码：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_pass = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.admin_pass.pack()

        Button(self.window, text="登陆", width=8, font=tkFont.Font(size=12), command=self.login).pack(pady=40)
        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back).pack()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def login(self):
        print(str(self.admin_userid.get()))
        print(str(self.admin_pass.get()))
        admin_pass = None

        # 数据库操作 查询管理员表
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='mamutong030906') # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM user WHERE u_id = '%s'" % (self.admin_userid.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                u_id = row[0]
                admin_pass = row[1]
                # 打印结果
                print("u_id=%s,admin_pass=%s" % (u_id, admin_pass))
        except:
            print("Error: unable to fecth data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        db.close()  # 关闭数据库连接

        print("正在登陆管理员管理界面")
        print("self", self.admin_pass)
        print("local", admin_pass)

        if self.admin_pass.get() == admin_pass:
            AdminManage(self.window)  # 进入管理员操作界面
        else:
            messagebox.showinfo('警告！', '用户名或密码不正确！')

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口


# 学生登陆页面
class StudentPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('学生登陆')
        self.window.geometry('300x450')

        label = tk.Label(self.window, text='学生登陆', bg='pink', font=('Verdana', 20), width=30, height=2)
        label.pack()

        Label(self.window, text='学生账号：', font=tkFont.Font(size=14)).pack(pady=25)
        self.student_id = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.student_id.pack()

        Label(self.window, text='学生密码：', font=tkFont.Font(size=14)).pack(pady=25)
        self.student_pass = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.student_pass.pack()

        Button(self.window, text="登陆", width=8, font=tkFont.Font(size=12), command=self.login).pack(pady=40)
        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back).pack()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def login(self):
        print(str(self.student_id.get()))
        print(str(self.student_pass.get()))
        stu_pass = None

        # 数据库操作 查询管理员表
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='mamutong030906')  # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM user WHERE u_id = '%s'" % (self.student_id.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                stu_id = row[0]
                stu_pass = row[1]
                # 打印结果
                print("stu_id=%s,stu_pass=%s" % (stu_id, stu_pass))
        except:
            print("Error: unable to fecth data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        db.close()  # 关闭数据库连接

        print("正在登陆学生信息查看界面")
        print("self", self.student_pass.get())
        print("local", stu_pass)

        if self.student_pass.get() == stu_pass:
            ActivityView(self.window, self.student_id.get())  # 进入活动信息查看界面
        else:
            messagebox.showinfo('警告！', '用户名或密码不正确！')

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口


# 管理员修改活动信息界面
class AdminManage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = Tk()  # 初始框的声明
        self.window.title('管理员操作界面')

        self.frame_left_top = tk.Frame(width=300, height=250)
        self.frame_right_top = tk.Frame(width=200, height=250)
        self.frame_center = tk.Frame(width=700, height=500)
        self.frame_bottom = tk.Frame(width=700, height=50)

        # 定义下方中心列表区域
        self.columns = ("活动id", "活动名称", "需要人数", "活动要求", "活动地点id")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("活动id", width=50, anchor='center')  # 表示列,不显示
        self.tree.column("活动名称", width=100, anchor='center')
        self.tree.column("需要人数", width=100, anchor='center')
        self.tree.column("活动要求", width=200, anchor='center')
        self.tree.column("活动地点id", width=100, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.ac_id = []
        self.ac_name = []
        self.capacity = []
        self.requir = []
        self.l_id = []
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='mamutong030906')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM activity"  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.ac_id.append(row[0])
                self.ac_name.append(row[1])
                self.capacity.append(row[2])
                self.requir.append(row[3])
                self.l_id.append(row[4])
            # print(self.id)
            # print(self.name)
            # print(self.gender)
            # print(self.age)
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(min(len(self.ac_id), len(self.ac_name), len(self.capacity), len(self.requir), len(self.l_id))):  # 写入数据
            self.tree.insert('', i, values=(self.ac_id[i], self.ac_name[i], self.capacity[i], self.requir[i], self.l_id[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="活动信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()  # 声明活动id
        self.var_name = StringVar()  # 声明活动名称
        self.var_capacity = StringVar()  # 声明需要人数
        self.var_requir = StringVar()  # 声明活动要求
        self.var_lid = StringVar()  # 声明活动地点id

        # 活动id
        self.right_top_id_label = Label(self.frame_left_top, text="活动id：", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)  # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)
        # 活动名称
        self.right_top_name_label = Label(self.frame_left_top, text="活动名称：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 需要人数
        self.right_top_capacity_label = Label(self.frame_left_top, text="需要人数：", font=('Verdana', 15))
        self.right_top_capacity_entry = Entry(self.frame_left_top, textvariable=self.var_capacity,
                                            font=('Verdana', 15))
        self.right_top_capacity_label.grid(row=3, column=0)  # 位置设置
        self.right_top_capacity_entry.grid(row=3, column=1)
        # 活动要求
        self.right_top_requir_label = Label(self.frame_left_top, text="活动要求：", font=('Verdana', 15))
        self.right_top_requir_entry = Entry(self.frame_left_top, textvariable=self.var_requir,
                                            font=('Verdana', 15))
        self.right_top_requir_label.grid(row=4, column=0)  # 位置设置
        self.right_top_requir_entry.grid(row=4, column=1)
        # 活动地点id
        self.right_top_lid_label = Label(self.frame_left_top, text="活动地点id：", font=('Verdana', 15))
        self.right_top_lid_entry = Entry(self.frame_left_top, textvariable=self.var_lid,
                                            font=('Verdana', 15))
        self.right_top_lid_label.grid(row=5, column=0)  # 位置设置
        self.right_top_lid_entry.grid(row=5, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建活动信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中活动信息', width=20,
                                            command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中活动信息', width=20,
                                            command=self.del_row)
        self.right_top_button4 = ttk.Button(self.frame_right_top, text='查询活动申请列表', width=20,
                                            command=lambda: ApplicationManage(self.window))

        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)
        self.right_top_button4.grid(row=5, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=20)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口

    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.var_name.set(self.row_info[1])
        self.var_capacity.set(self.row_info[2])
        self.var_requir.set(self.row_info[3])
        self.var_lid.set(self.row_info[4])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id,
                                        font=('Verdana', 15))

        print('')

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def new_row(self):
        print('123')
        print(self.var_id.get())
        print(self.ac_id)
        if str(self.var_id.get()) in self.ac_id:
            messagebox.showinfo('警告！', '该学生已存在！')
        else:
            if self.var_id.get() != '' and self.var_name.get() != '' and self.var_capacity.get() != '' and self.var_requir.get() != '' and self.var_lid.get() != '':
                # 打开数据库连接
                db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='mamutong030906')
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "INSERT INTO activity(ac_id, ac_name, capacity, requir, l_id) \
				       VALUES ('%s', '%s', '%s', '%s', '%s')" % \
                      (self.var_id.get(), self.var_name.get(), self.var_capacity.get(), self.var_requir.get(), self.var_lid.get())  # SQL 插入语句
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()  # 关闭数据库连接

                self.ac_id.append(self.var_id.get())
                self.ac_name.append(self.var_name.get())
                self.capacity.append(self.var_capacity.get())
                self.requir.append(self.var_requir.get())
                self.l_id.append(self.var_lid.get())
                self.tree.insert('', len(self.ac_id) - 1, values=(
                    self.ac_id[len(self.ac_id) - 1], self.ac_name[len(self.ac_id) - 1], self.capacity[len(self.ac_id) - 1],
                    self.requir[len(self.ac_id) - 1], self.l_id[len(self.ac_id) - 1]))
                self.tree.update()
                messagebox.showinfo('提示！', '插入成功！')
            else:
                messagebox.showinfo('警告！', '请填写学生数据')

    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_id.get() == self.row_info[0]:  # 如果所填学号 与 所选学号一致
                # 打开数据库连接
                db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='mamutong030906')
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql_update = "UPDATE activity SET ac_name = '%s', capacity = '%s', requir = '%s', l_id = '%s' \
				 WHERE ac_id = '%s'" % (
                    self.var_name.get(), self.var_capacity.get(), self.var_requir.get(),  self.var_lid.get(), self.var_id.get())  # SQL 插入语句
                try:
                    cursor.execute(sql_update)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '更新成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
                db.close()  # 关闭数据库连接

                id_index = self.ac_id.index(self.row_info[0])
                self.ac_name[id_index] = self.var_name.get()
                self.capacity[id_index] = self.var_capacity.get()
                self.requir[id_index] = self.var_requir.get()
                self.l_id[id_index] = self.var_lid.get()

                self.tree.item(self.tree.selection()[0], values=(
                    self.var_id.get(), self.var_name.get(), self.var_capacity.get(),
                    self.var_requir.get(), self.var_lid.get()))  # 修改对于行信息
            else:
                messagebox.showinfo('警告！', '不能修改学生学号！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print(self.tree.selection()[0])  # 行号
            print(self.tree.get_children())  # 所有行
            # 打开数据库连接
            db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='mamutong030906')
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql_delete = "DELETE FROM activity WHERE ac_id = '%s'" % (self.row_info[0])  # SQL 插入语句
            try:
                cursor.execute(sql_delete)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            db.close()  # 关闭数据库连接

            id_index = self.ac_id.index(self.row_info[0])
            print(id_index)
            del self.ac_id[id_index]
            del self.ac_name[id_index]
            del self.capacity[id_index]
            del self.requir[id_index]
            del self.l_id[id_index]
            print(self.ac_id)
            self.tree.delete(self.tree.selection()[0])  # 删除所选行
            print(self.tree.get_children())


#管理员查询申请界面
class ApplicationManage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('申请列表')

        self.frame_top = tk.Frame(width=300, height=40)
        self.frame_center = tk.Frame(width=700, height=800)
        self.frame_bottom = tk.Frame(width=700, height=50)

        # 定义中心列表区域
        self.columns = ("申请活动id", "申请人id", "状态")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("申请活动id", width=150, anchor='center')  # 表示列,不显示
        self.tree.column("申请人id", width=150, anchor='center')
        self.tree.column("状态", width=100, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.ac_id = []
        self.u_id = []
        self.status = []

        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='mamutong030906')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM application"  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.ac_id.append(row[0])
                self.u_id.append(row[1])
                self.status.append(row[2])
        except:
            print("Error: unable to fetch data")
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(min(len(self.ac_id), len(self.u_id), len(self.status))):  # 写入数据
            self.tree.insert('', i,
                             values=(self.ac_id[i], self.u_id[i], self.status[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部提交申请区域
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.top_button = ttk.Button(self.frame_top, text='通过申请', width=20, command=self.submit)
        self.top_button.grid(row=2, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口

    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        self.row_info = self.tree.item(self.row, "values")
        print('选中申请',self.row_info[0],self.row_info[1])
        print('')


    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def submit(self):
        print('123')

        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='mamutong030906')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "UPDATE application set status='1' where ac_id='%s' and u_id='%s'" \
                % (self.row_info[0],self.row_info[1])
        try:
            cursor.execute(sql)  # 执行sql语句
            db.commit()  # 提交到数据库执行
            messagebox.showinfo('提示！', '通过申请！')
        except:
            db.rollback()  # 发生错误时回滚
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

# 用户活动查看信息界面
class ActivityView:
    def __init__(self, parent_window, student_id):
        parent_window.destroy()  # 销毁主界面
        self.u_id = student_id

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('活动信息')

        self.frame_top = tk.Frame(width=300, height=40)
        self.frame_center = tk.Frame(width=700, height=800)
        self.frame_bottom = tk.Frame(width=700, height=50)

        # 定义下方中心列表区域
        self.columns = ("活动名称", "需要人数", "活动要求", "活动地点","活动id")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("活动名称", width=100, anchor='center')
        self.tree.column("需要人数", width=50, anchor='center')
        self.tree.column("活动要求", width=100, anchor='center')
        self.tree.column("活动地点", width=100, anchor='center')
        self.tree.column("活动id", width=50, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.ac_id = []
        self.ac_name = []
        self.capacity = []
        self.requir = []
        self.l_name = []
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='mamutong030906')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM viewactivityinfo"  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.ac_name.append(row[0])
                self.capacity.append(row[1])
                self.requir.append(row[2])
                self.l_name.append(row[3])
                self.ac_id.append(row[4])
        except:
            print("Error: unable to fetch data")
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(min(len(self.ac_name), len(self.capacity), len(self.requir), len(self.l_name), len(self.ac_id))):  # 写入数据
            self.tree.insert('', i, values=(self.ac_name[i], self.capacity[i], self.requir[i], self.l_name[i], self.ac_id[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部提交申请区域
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.top_button = ttk.Button(self.frame_top, text='提交申请', width=20, command=self.submit)
        self.top_button.grid(row=2, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击

        self.var_uid = StringVar()  # 声明用户id

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口

    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        self.row_info = self.tree.item(self.row, "values")
        print('选中id',self.row_info[4])
        print('')


    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def submit(self):
        print('123')
        print('选中活动id:',self.row_info[4])
        print('学生id:',self.u_id)

        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='mamutong030906')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "INSERT INTO application(ac_id, u_id, status) \
                VALUES ('%s', '%s', '0')" % (self.row_info[4],self.u_id)
        try:
            cursor.execute(sql)  # 执行sql语句
            db.commit()  # 提交到数据库执行
            messagebox.showinfo('提示！', '插入成功！')
        except:
            db.rollback()  # 发生错误时回滚
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

class CreateUserPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('普通用户注册页面')

        Label(self.window, text='学生账号应为学号', font=('Verdana', 18)).pack(pady=5)

        Label(self.window, text='学号：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_id = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.admin_id.pack()

        Label(self.window, text='密码：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_pass = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.admin_pass.pack()

        Label(self.window, text='专业id：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_mid = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.admin_mid.pack()

        Label(self.window, text='姓名：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_name = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.admin_name.pack()

        Label(self.window, text='性别：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_sex = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.admin_sex.pack()

        Button(self.window, text="确定创建", width=8, font=tkFont.Font(size=12), command=self.find).pack(pady=40)
        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back).pack()

    def find(self):
        print(str(self.admin_id.get()))
        print(str(self.admin_pass.get()))

        # 数据库操作 查询用户表
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='mamutong030906') # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT u_id FROM user WHERE u_id = '%s'" % \
              (self.admin_id.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            print(results)
            if self.admin_id.get in results:
                print("Error: name already exists！")
                messagebox.showinfo('警告！', '用户id已存在！')
            else:
                self.change()
        except:
            print("Error: unable to fecth data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')

    def change(self):
        print(str(self.admin_id.get()))
        print(str(self.admin_pass.get()))

        # 数据库操作
        db = pymysql.connect(host='localhost', port=3306, db='student',user='root', password='mamutong030906') # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "INSERT INTO user(u_id, u_password) VALUES ('%s', '%s')" % \
              (self.admin_id.get(), self.admin_pass.get())  # SQL 查询语句
        sql1 = "INSERT INTO student(s_id, u_id, m_id, s_name, s_sex) VALUES ('%s', '%s', '%s', '%s', '%s')" % \
              (self.admin_id.get(), self.admin_id.get(), self.admin_mid.get(), self.admin_name.get(), self.admin_sex.get())  # SQL 查询语句
        try:
            cursor.execute(sql)  # 执行sql语句
            cursor.execute(sql1)  # 执行sql语句
            db.commit()  # 提交到数据库执行
            messagebox.showinfo('提示', '创建成功')
        except:
            db.rollback()  # 发生错误时回滚
            messagebox.showinfo('警告！', '数据库连接失败！')

        db.close()  # 关闭数据库连接

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口


class AboutPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明

        self.window.title('用户注册')
        self.window.geometry('300x420')

        label = tk.Label(self.window, text='注册系统', bg='cyan', font=('Verdana', 20), width=30, height=2)
        label.pack()

        Label(self.window, text='学生账号为学号', font=('Verdana', 18)).pack(pady=5)
        Label(self.window, text='初始密码为123456', font=('Verdana', 18)).pack(pady=5)

        Button(self.window, text="用户注册", width=10, font=tkFont.Font(size=16),
               command=lambda: CreateUserPage(self.window)).pack(pady=15)
        Button(self.window, text="管理员注册", width=10, font=tkFont.Font(size=16),
               command=lambda: Adminlogin(self.window)).pack(pady=15)
        Button(self.window, text="返回首页", width=10, font=tkFont.Font(size=16), command=self.back).pack(pady=15)

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口


# 管理员账号设置
class Adminlogin:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('请先登录任意管理员账号')
        self.window.geometry('300x500')  # 这里的乘是小x

        label = tk.Label(self.window, text='管理员登陆', bg='green', font=('Verdana', 20), width=30, height=2)
        label.pack()

        Label(self.window, text='管理员账号：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_userid = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.admin_userid.pack()

        Label(self.window, text='管理员密码：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_pass = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.admin_pass.pack()

        Button(self.window, text="创建账号", width=8, font=tkFont.Font(size=12), command=self.login_create).pack(pady=25)
        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back).pack(pady=25)

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def login_create(self):
        print(str(self.admin_userid.get()))
        print(str(self.admin_pass.get()))
        admin_pass = None

        # 数据库操作 查询用户表
        db = pymysql.connect(host='localhost', port=3306, db='student',user='root', password='mamutong030906')  # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM user WHERE u_id = '%s'" % (self.admin_userid.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                u_id = row[0]
                admin_pass = row[1]
                # 打印结果
                print("u_id=%s,admin_pass=%s" % (u_id, admin_pass))
        except:
            print("Error: unable to fecth data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        db.close()  # 关闭数据库连接

        print("正在登陆管理员创建界面")
        print("self", self.admin_pass)
        print("local", admin_pass)

        if self.admin_pass.get() == admin_pass:
            CreateAdminPage(self.window)
        else:
            messagebox.showinfo('警告！', '用户名或密码不正确！')


    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口


class CreateAdminPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('管理员账号注册')

        Label(self.window, text='管理员账号：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_id = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.admin_id.pack()

        Label(self.window, text='管理员编号：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_id1 = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.admin_id1.pack()

        Label(self.window, text='设置密码：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_pass = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.admin_pass.pack()

        Label(self.window, text='管理员性别：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_sex = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.admin_sex.pack()

        Button(self.window, text="确定创建", width=8, font=tkFont.Font(size=12), command=self.find).pack(pady=40)
        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back).pack()

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口

    def find(self):
        print(str(self.admin_id.get()))
        print(str(self.admin_id1.get()))
        print(str(self.admin_pass.get()))

        # 数据库操作 查询管理员表用户表
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='mamutong030906') # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT u_id FROM user WHERE u_id = '%s'" % \
              (self.admin_id.get())  # SQL 查询语句
        # sql1 = "SELECT a_id FROM administrator WHERE a_id = '%s'" % \
        #       (self.admin_id1.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            print(results)
            if self.admin_id.get in results:
                print("Error: name already exists！")
                messagebox.showinfo('警告！', '用户id已存在！')
            else:
                self.change()
        except:
            print("Error: unable to fecth data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        # try:
        #     # 执行SQL语句
        #     cursor.execute(sql1)
        #     # 获取所有记录列表
        #     results = cursor.fetchall()
        #     print(results)
        #     if self.admin_id1.get in results:
        #         print("Error: name already exists！")
        #         messagebox.showinfo('警告！', '管理员编号已存在！')
        #     else:
        #         self.change()
        # except:
        #     print("Error: unable to fecth data")
        #     messagebox.showinfo('警告！', '用户名或密码不正确！')

    def change(self):
        print(str(self.admin_id.get()))
        print(str(self.admin_id1.get()))
        print(str(self.admin_pass.get()))
        print(str(self.admin_sex.get()))

        # 数据库操作
        db = pymysql.connect(host='localhost', port=3306, db='student',user='root', password='mamutong030906') # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "INSERT INTO user(u_id, u_password) VALUES ('%s', '%s')" % \
              (self.admin_id.get(), self.admin_pass.get())  # SQL 查询语句
        sql1 = "INSERT INTO administrator(a_id, u_id, a_sex) VALUES ('%s', '%s', '%s')" % \
              (self.admin_id1.get(), self.admin_id.get(), self.admin_sex.get())  # SQL 查询语句
        try:
            cursor.execute(sql)  # 执行sql语句
            cursor.execute(sql1)  # 执行sql语句
            db.commit()  # 提交到数据库执行
            messagebox.showinfo('提示', '创建成功')
        except:
            db.rollback()  # 发生错误时回滚
            messagebox.showinfo('警告！', '数据库连接失败！')

        db.close()  # 关闭数据库连接


if __name__ == '__main__':
    try:
        # 打开数据库连接 连接测试
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='mamutong030906')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # 关闭数据库连接
        db.close()

        # 实例化Application
        window = tk.Tk()
        StartPage(window)
    except:
        messagebox.showinfo('错误！', '连接数据库失败！')
