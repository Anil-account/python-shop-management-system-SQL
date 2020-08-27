from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from final_assignment.database_app.data import *
from tkinter import messagebox
from final_assignment.set_get.retrive import *
import datetime


class Main_frame:  # Creating Frame
    def __init__(self, root):
        self.root = root
        self.root.title('Home Page')
        self.root.geometry('1540x790+0+0')
        self.root.iconbitmap('icon.ico')

        image = Image.open("image.png")  # Inserting Background Image
        self.photo = image.resize((1540, 799), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.photo)
        lbl = Label(root, image=self.photo, bg='black')
        lbl.image_ref = self.photo
        lbl.grid(row=0, column=0)

        self.data = ImageTk.PhotoImage(Image.open('data.png'))  # Inserting Image for Product
        lbl1 = Label(image=self.data)
        lbl1.img = self.data

        product_btn = Button(root, image=self.data, command=self.entry)
        product_btn.place(x=300, y=350)

        self.customer = ImageTk.PhotoImage(Image.open('customer.png'))
        lab2 = Label(image=self.customer)
        lab2.photo = self.customer

        customer_btn = Button(root, image=self.customer, command=self.signup)
        customer_btn.place(x=700, y=350)

        self.shop = ImageTk.PhotoImage(Image.open('shop.png'))
        lab3 = Label(image=self.shop)
        lab3.photo = self.shop

        shop_btn = Button(root, image=self.shop, command=self.shopping)
        shop_btn.place(x=1100, y=350)

        Label(root, text='Sign Up', font=('arial', 16, 'bold'), width=10, bg='gray64').place(x=700, y=485)
        Label(root, text='Data', font=('arial', 16, 'bold'), width=10, bg='gray64').place(x=300, y=485)
        Label(root, text='Shop', font=('arial', 16, 'bold'), width=10, bg='gray64').place(x=1100, y=485)

        btn_quit = Button(root, text='Exit Page', font=('arial', 15, 'bold'), width=10, bg='sky blue3', bd=4,
                          command=self.quit)
        btn_quit.place(x=1375, y=10, height=50, width=150)

    def quit(self):
        message = messagebox.askyesno('Exit Application', 'Do you want to quit Application', icon='warning')
        if message:
            root.destroy()

    def entry(self):
        wn = Toplevel()
        Login(wn)
        self.root.withdraw()

    def signup(self):
        wn = Toplevel()
        CustomerDetails(wn)
        self.root.withdraw()

    def shopping(self):
        wn = Toplevel()
        Shop(wn)
        self.root.withdraw()


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title('LOGIN')
        self.root.geometry('400x196+600+200')
        self.root.resizable(0, 0)
        self.root.iconbitmap('icon.ico')

        self.id = StringVar()
        self.password = StringVar()

        heading = Label(self.root, text='Product Entry Page', bg='yellow', font=('arial', 17, 'bold'))
        heading.pack(side=TOP, fill=X)

        main_frame = Frame(self.root, bg='pink')
        main_frame.place(x=0, y=35, height=100, width=400)

        btn_frame = Frame(self.root, bg='cyan', relief=RIDGE, bd=10)
        btn_frame.place(x=0, y=135, height=60, width=400)
        # widget frame

        lbl_id = Label(main_frame, text='User Name', bg='pink', font=('arial', 15, 'bold'), width=10)
        lbl_id.grid(row=0, column=0, padx=10, pady=10)

        self.ent_id = Entry(main_frame, textvariable=self.id, font=('arial', 12, 'bold'), relief=GROOVE, bd=5)
        self.ent_id.grid(row=0, column=1, padx=10, pady=10)

        lbl_pass = Label(main_frame, text='Password', bg='pink', font=('arial', 15, 'bold'), width=10)
        lbl_pass.grid(row=1, column=0, padx=10, pady=10)

        self.ent_pass = Entry(main_frame, textvariable=self.password, font=('arial', 12, 'bold'), relief=GROOVE, bd=5,
                              show='*')
        self.ent_pass.grid(row=1, column=1, padx=10, pady=10)

        add_btn = Button(btn_frame, text='LOGIN', font=('arial', 10, 'bold'), command=self.add, width=35, bg='cyan', )
        add_btn.pack(pady=5)

    def add(self):
        if str(self.password.get()) == str('admin') and str(self.id.get()) == str('admin'):
            messagebox.showinfo('welcome', 'Good to see you Back')
            self.product()

        else:
            messagebox.showwarning('Error', 'Either Password or ID is incorrect')
            self.main_frame()

    def product(self):
        wn = Toplevel()
        Second_frame(wn)
        self.root.withdraw()

    def main_frame(self):
        wn = Toplevel()
        Main_frame(wn)
        self.root.withdraw()


class Second_frame:
    def __init__(self, root):
        self.root = root
        root.title('Product Details')
        root.geometry('1540x790+0+0')
        root.iconbitmap('icon.ico')

        image = Image.open('entry.jpg')
        image = image.resize((1540, 799), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        lbl_image = Label(root, image=photo)
        lbl_image.my_image = photo
        lbl_image.pack()

        self.connection = Database()

        self.name = StringVar()
        self.code = StringVar()
        self.id = StringVar()
        self.cost = StringVar()
        self.content = StringVar()
        self.stock = StringVar()

        data_frame = Frame(root, bg='orange4')
        data_frame.place(x=20, y=20, height=740, width=505)

        table_frame = Frame(root)
        table_frame.place(x=600, y=90, height=650, width=900)

        product = Label(data_frame, text='Products Data Entry', font=('arial', 35, 'bold'), bg='orange4',
                        fg='dark slate gray1')
        product.grid(row=0, columnspan=4, padx=10, pady=10, )

        product_name = Label(data_frame, text='Name of Product', font=('arial', 14, 'bold'), bg='orange4', fg='snow')
        product_name.grid(row=1, column=0, padx=10, pady=20)

        product_entry = Entry(data_frame, textvariable=self.name, font=('arial', 14, 'bold'), relief=GROOVE, bd=5)
        product_entry.grid(row=1, column=1)

        product_code = Label(data_frame, text='Product ID', font=('arial', 14, 'bold'), bg='orange4', fg='snow')
        product_code.grid(row=2, column=0, padx=10, pady=20)

        prod_entry = Entry(data_frame, textvariable=self.code, font=('arial', 14, 'bold'), relief=GROOVE, bd=5)
        prod_entry.grid(row=2, column=1)

        product_con = Label(data_frame, text='Content Code', font=('arial', 14, 'bold'), bg='orange4', fg='snow')
        product_con.grid(row=3, column=0, padx=10, pady=20)

        con_entry = Entry(data_frame, textvariable=self.content, font=('arial', 14, 'bold'), relief=GROOVE, bd=5)
        con_entry.grid(row=3, column=1)

        product_price = Label(data_frame, text='Cost', font=('arial', 14, 'bold'), bg='orange4', fg='snow')
        product_price.grid(row=4, column=0, padx=10, pady=20)

        price_entry = Entry(data_frame, textvariable=self.cost, font=('arial', 14, 'bold'), relief=GROOVE, bd=5)
        price_entry.grid(row=4, column=1, )

        discount_code = Label(data_frame, text='Discount Code', font=('arial', 14, 'bold'), bg='orange4', fg='snow')
        discount_code.grid(row=5, column=0, padx=10, pady=20)

        id_entry = Entry(data_frame, textvariable=self.id, font=('arial', 14, 'bold'), relief=GROOVE, bd=5)
        id_entry.grid(row=5, column=1)

        product_des = Label(data_frame, text='Description', font=('arial', 14, 'bold'), bg='orange4', fg='snow')
        product_des.grid(row=6, column=0, padx=10, pady=20, sticky=N)

        self.des = Text(data_frame, height=6, width=28, relief=GROOVE, bd=5)
        self.des.grid(row=6, column=1, pady=20)

        product_stock = Label(data_frame, text='Stock Left', font=('arial', 14, 'bold'), bg='orange4', fg='snow')
        product_stock.grid(row=7, column=0, padx=10, pady=20)

        stock_entry = Entry(data_frame, textvariable=self.stock, font=('arial', 14, 'bold'), relief=GROOVE, bd=5)
        stock_entry.grid(row=7, column=1)

        button_frame = Frame(root, bg='orange4', relief=RIDGE, bd=4)
        button_frame.place(x=25, y=690, height=70, width=490)

        Button(button_frame, text='CLEAR', width=10, bg='wheat1', bd=4, command=self.clear).pack(side=LEFT, padx=15,
                                                                                                 pady=5)

        btn_add = Button(button_frame, text='ADD', width=10, bg='wheat1', bd=4, command=self.add)
        btn_add.pack(side=LEFT, padx=15, pady=5)

        btn_update = Button(button_frame, text='UPDATE', width=10, bg='wheat1', bd=4, command=self.update)
        btn_update.pack(side=LEFT, padx=15, pady=5)

        btn_delete = Button(button_frame, text='DELETE', width=10, bg='wheat1', bd=4, command=self.delete)
        btn_delete.pack(side=LEFT, padx=15, pady=5)

        discount_content = Button(self.root, text='Discount and Content', font=('arial', 15, 'bold'), width=20,
                                  bg='wheat1', bd=4, command=self.dis_con)
        discount_content.place(x=1050, y=20, height=50)

        btn_quit = Button(root, text='Home Page', font=('arial', 15, 'bold'), width=10, bg='wheat1', bd=4,
                          command=self.quit)
        btn_quit.place(x=1350, y=20, height=50)

        btn_customer = Button(root, text='Customer Details', font=('arial', 15, 'bold'), width=15, bg='wheat1', bd=4,
                              command=self.customer)
        btn_customer.place(x=810, y=20, height=50)

        btn_order = Button(root, text='Customer Order', font=('arial', 15, 'bold'), width=15, bg='wheat1', bd=4,
                           command=self.order)
        btn_order.place(x=560, y=20, height=50)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.product_table = ttk.Treeview(table_frame, columns=(
            'productid', 'productname', 'cost', 'describe', 'stock', 'discount', 'content', 'discountoffer',
            'actualcont'),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.product_table.xview)
        scroll_y.config(command=self.product_table.yview)
        self.product_table.heading('productid', text='Product ID')
        self.product_table.heading('productname', text='Product Name')
        self.product_table.heading('cost', text='Cost')
        self.product_table.heading('describe', text='Description')
        self.product_table.heading('stock', text='Stock')
        self.product_table.heading('discount', text='Discount Code')
        self.product_table.heading('content', text='Content Code')
        self.product_table.heading('discountoffer', text='Discount%')
        self.product_table.heading('actualcont', text='Content')
        self.product_table['show'] = 'headings'

        self.product_table.column('productid', width=100)
        self.product_table.column('productname', width=100)
        self.product_table.column('content', width=100)
        self.product_table.column('discount', width=100)
        self.product_table.column('cost', width=100)
        self.product_table.column('describe', width=300)
        self.product_table.column('stock', width=100)
        self.product_table.column('discountoffer', width=100)
        self.product_table.column('actualcont', width=100)
        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def dis_con(self):
        wn = Toplevel()
        DiscountContent(wn)
        self.root.withdraw()

    def customer(self):
        wn = Toplevel()
        CustomerTable(wn)
        self.root.withdraw()

    def order(self):
        wn = Toplevel()
        CustomerOrder(wn)
        self.root.withdraw()

    def quit(self):
        if self.name.get() != '' or self.code.get() != '' or self.id.get() != '' or self.cost.get() != '' or self.content.get() != '' or self.des.get(
                '1.0', END) != '' or self.stock.get() != '':
            message = messagebox.askyesno('Wait', 'Are you sure, You want to quit?')
            if message:
                wn = Toplevel()
                Main_frame(wn)
                self.root.withdraw()

    def clear(self):
        list = [self.cost, self.name,self.code,self.content,self.id,self.des,self.stock]
        CustomerDetails.solution(list)

    def show(self):
        query = "select product_code,product_name,cost,description,stock,discount_code,content_code," \
                "discount.discountoffer,content.content_name from product,discount,content where " \
                "discount.dis_id=product.discount_code and product.content_code=content.content_id; "
        rows = self.connection.select(query)
        if len(rows) != 0:
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('', END, values=row)

    def add(self):
        if self.name.get() == '' or self.code.get() == '' or self.id.get() == '' or self.cost.get() == '' or self.content.get() == '' or self.des.get(
                '1.0', END) == '' or self.stock.get() == '':
            messagebox.showinfo('Data Inserting', 'Please fill all the entries')
        else:
            #                               name, discount_code, content_code, cost, product_code, describe, stock):
            pro_ref = ProductData(self.name.get(), self.id.get(), self.content.get(), self.cost.get(), self.code.get(),
                                  self.des.get('1.0', END), self.stock.get())
            query = "insert into product(product_code,product_name,cost,description,stock,discount_code, " \
                    "content_code) values(%s,%s,%s,%s,%s,%s,%s) "
            values = (
                int(pro_ref.get_product_code()), pro_ref.get_name(), int(pro_ref.get_cost()), pro_ref.get_describe(),
                int(pro_ref.get_stock()), int(pro_ref.get_discount_code()), int(pro_ref.get_content_code()))
            self.connection.add(query, values)
            messagebox.showinfo('Data Inserted', 'Data has been inserted')
            self.clear()
            self.show()

    def delete(self):
        message = messagebox.askyesno('Processing', 'Are you sure? ')
        if message:
            if self.code.get() == '':
                messagebox.showinfo('Data deleting', 'Please fill the entries \n product id')
            else:
                pro_ref = ProductData(self.name.get(), self.id.get(), self.content.get(), self.cost.get(),
                                      self.code.get(),
                                      self.des.get('1.0', END), self.stock.get())
                query = "delete from product where product_code=%s"
                values = (pro_ref.get_product_code(),)
                self.connection.delete(query, values)
                messagebox.showinfo('Deleting Data', 'Data has been deleted')
                self.show()

    def update(self):
        message = messagebox.askyesno('Processing', 'Are you sure? ')
        if message:
            if self.name.get() == '' or self.id.get() == '' or self.cost.get() == '' or self.content.get() == '' or self.des.get(
                    '1.0', END) == '' or self.stock.get() == '':
                messagebox.showinfo('Data Updating', 'Please fill all the entries ')
            else:
                pro_ref = ProductData(self.name.get(), self.id.get(), self.content.get(), self.cost.get(),
                                      self.code.get(),
                                      self.des.get('1.0', END), self.stock.get())
                query = "update product set product_name = %s, cost = %s, stock = %s, discount_code = %s, " \
                        "content_code=%s, description=%s where product_code=%s "
                values = (pro_ref.get_name(), pro_ref.get_cost(), pro_ref.get_stock(), pro_ref.get_discount_code(),
                          pro_ref.get_content_code(), pro_ref.get_describe(), pro_ref.get_product_code())
                self.connection.update(query, values)
                messagebox.showinfo('Data updating', 'Data has been updated')
                self.show()

    def get_data(self, ev):
        extract_data = self.product_table.focus()
        contents = self.product_table.item(extract_data)
        row = contents['values']
        self.name.set(row[1])
        self.code.set(row[0])
        self.content.set(row[6])
        self.cost.set(row[2])
        self.id.set(row[5])
        self.des.delete('1.0', END)
        self.des.insert(END, row[3])
        self.stock.set(row[4])


class CustomerDetails:
    def __init__(self, root):
        self.root = root
        root.title('Customer Details')
        root.geometry('1540x790+0+0')
        root.iconbitmap('icon.ico')

        image = Image.open('background.png')
        image = image.resize((1540, 799), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        lbl = Label(root, image=photo)
        lbl.image = photo
        lbl.pack()

        self.first = StringVar()
        self.last = StringVar()
        self.age = StringVar()
        self.id = StringVar()
        self.email = StringVar()
        self.phone = StringVar()

        self.connection = Database()

        entry_frame = Frame(root, bg='lavender')
        entry_frame.place(x=20, y=50, height=660, width=500)

        Label(entry_frame, text='Create an Account', bg='lavender', fg='green2', font=('arial', 20, 'bold'),
              width=26).grid(row=0, column=0, columnspan=5, pady=10)

        first = Label(entry_frame, text='First Name', bg='lavender', font=('arial', 15, 'bold'))
        first.grid(row=1, column=0, padx=5, pady=10)

        name_ent = Entry(entry_frame, textvariable=self.first, bd=3, font=('arial', 14, 'bold'), relief=GROOVE)
        name_ent.grid(row=1, column=1, padx=10, pady=20)

        last = Label(entry_frame, text='Last Name', bg='lavender', font=('arial', 15, 'bold'))
        last.grid(row=2, column=0, padx=5, pady=10)

        last_ent = Entry(entry_frame, textvariable=self.last, bd=3, font=('arial', 14, 'bold'), relief=GROOVE)
        last_ent.grid(row=2, column=1, padx=10, pady=10)

        user_id = Label(entry_frame, text='Customer ID', bg='lavender', font=('arial', 15, 'bold'))
        user_id.grid(row=3, column=0, padx=5, pady=10)

        user_ent = Entry(entry_frame, textvariable=self.id, bd=3, font=('arial', 14, 'bold'), relief=GROOVE)
        user_ent.grid(row=3, column=1, padx=10, pady=10)

        age = Label(entry_frame, text='Age', bg='lavender', font=('arial', 15, 'bold'))
        age.grid(row=4, column=0, padx=5, pady=10)

        age_ent = Entry(entry_frame, textvariable=self.age, bd=3, font=('arial', 14, 'bold'), relief=GROOVE)
        age_ent.grid(row=4, column=1, padx=10, pady=10)

        home_address = Label(entry_frame, text='Home Address', bg='lavender', font=('arial', 15, 'bold'))
        home_address.grid(row=5, column=0, padx=5, pady=10)

        self.home = Text(entry_frame, bd=3, relief=GROOVE, height=3, width=25, font=('arial', 12, ''))
        self.home.grid(row=5, column=1, padx=5, pady=10)

        email = Label(entry_frame, text='Email', bg='lavender', font=('arial', 15, 'bold'))
        email.grid(row=6, column=0, padx=5, pady=10)

        email_ent = Entry(entry_frame, textvariable=self.email, bd=3, font=('arial', 14, 'bold'), relief=GROOVE)
        email_ent.grid(row=6, column=1, padx=10, pady=10)

        delivery_address = Label(entry_frame, text='Delivery Address', bg='lavender', font=('arial', 15, 'bold'))
        delivery_address.grid(row=7, column=0, padx=5, pady=10)

        self.deliver = Text(entry_frame, bd=3, relief=GROOVE, height=3, width=25, font=('arial', 12, ''))
        self.deliver.grid(row=7, column=1, padx=5, pady=10)

        phone = Label(entry_frame, text='Phone', bg='lavender', font=('arial', 15, 'bold'))
        phone.grid(row=8, column=0, padx=5, pady=10)

        phone_ent = Entry(entry_frame, textvariable=self.phone, bd=3, font=('arial', 14, 'bold'), relief=GROOVE)
        phone_ent.grid(row=8, column=1, padx=10, pady=10)

        back = Button(self.root, text='Homepage', font=('arial', 17, 'bold'), bg='ghost white', command=self.quit)
        back.place(x=1370, y=20)

        add = Button(self.root, text='Sign Up', font=('arial', 17, 'bold'), bg='ghost white', command=self.add)
        add.place(x=1200, y=700)

        update = Button(self.root, text='Update Account', font=('arial', 17, 'bold'), bg='ghost white', width=20,
                        command=self.update)
        update.place(x=850, y=700)

        clear = Button(self.root, text='Clear', font=('arial', 17, 'bold'), bg='ghost white', width=15,
                       command=self.clear)
        clear.place(x=550, y=700)

    def quit(self):
        if self.first.get() != '' or self.last.get() != '' or self.id.get() != '' or self.home.get('1.0', END) != '' or \
                self.email.get() != '' or self.deliver.get('1.0',
                                                           END) != '' or self.phone.get() != '' or self.age.get() != '':
            message = messagebox.askyesno('Wait!!', 'Are you sure, You want to quit')
            if message:
                wn = Toplevel()
                Main_frame(wn)
                self.root.withdraw()

    def add(self):
        if self.first.get() == '' or self.last.get() == '' or self.id.get() == '' or self.home.get('1.0', END) == '' or \
                self.email.get() == '' or self.deliver.get('1.0',
                                                           END) == '' or self.phone.get() == '' or self.age.get() == '':
            messagebox.showwarning('Data missing', 'Please fill all entries')
        else:
            #                               id, first, last, address, phone, delivery, age, email
            customer_ref = Customer(self.id.get(), self.first.get(), self.last.get(), self.home.get('1.0', END),
                                    self.phone.get(), self.deliver.get('1.0', END), self.age.get(), self.email.get())
            query = 'insert into customer values (%s,%s,%s,%s,%s,%s,%s,%s)'
            values = (customer_ref.get_id(), customer_ref.get_first_name(), customer_ref.get_last_name(),
                      customer_ref.get_address(), customer_ref.get_phone(), customer_ref.get_delivery(),
                      customer_ref.get_age(), customer_ref.get_mail())
            self.connection.add(query, values)
            messagebox.showinfo('Creating account',
                                'Your account has been created. \n Your ID and E-mail acts as your account '
                                'IDENTITY.\n ID = ' + self.id.get() + " " + "E-mail = " + self.email.get())

    def update(self):
        message = messagebox.askyesno('Wait', 'Are you sure, You want to update all data except your ID',
                                      icon='warning')
        if message:
            if self.id.get() == '':
                messagebox.showwarning('Data missing', 'Please fill all Data to Update your information')
            else:
                customer_ref = Customer(self.id.get(), self.first.get(), self.last.get(), self.home.get('1.0', END),
                                        self.phone.get(), self.deliver.get('1.0', END), self.age.get(),
                                        self.email.get())
                query = 'update customer set first_name=%s, last_name=%s, address=%s, phone=%s, delivery_address=%s, ' \
                        'age=%s, email=%s where cus_Id=%s '
                values = (customer_ref.get_first_name(), customer_ref.get_last_name(), customer_ref.get_address(),
                          customer_ref.get_phone(), customer_ref.get_delivery(), customer_ref.get_age(),
                          customer_ref.get_mail(), customer_ref.get_id())
                self.connection.update(query, values)
                messagebox.showinfo('Data Updating', 'Your data has been updated')
                self.clear()

    def clear(self):
        list = [self.first, self.last, self.id, self.email, self.age, self.phone, self.home, self.deliver]
        CustomerDetails.solution(list)

    @classmethod
    def solution(cls, list):
        for i in range(len(list)):
            if type(list[i]) == Text:
                list[i].delete('1.0', END)
            else:
                list[i].set('')
        return list


class CustomerTable:
    def __init__(self, root):
        self.root = root
        root.title('Customer Table')
        root.geometry('1540x790+0+0')
        root.iconbitmap('icon.ico')

        image = Image.open('blur.png')
        image = image.resize((1540, 799), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        lbl_image = Label(root, image=photo)
        lbl_image.my_image = photo
        lbl_image.pack()

        self.connection = Database()

        table_frame = Frame(root, bd=3, relief=GROOVE)
        table_frame.place(x=300, y=300, height=450, width=900)

        lable_frame = Frame(root, relief=GROOVE, bg='light sky blue1', bd=4)
        lable_frame.place(x=300, y=12, width=900, height=50)

        small_frame = Frame(root, relief=GROOVE, bg='light sky blue1', bd=4)
        small_frame.place(x=300, y=60, width=900, height=220)

        Label(small_frame, text='Search By Customer ID', font=('arial', 15, 'bold'), bg='light sky blue1', ).place(x=40,
                                                                                                                   y=30)

        self.value = StringVar()

        search_ent = Entry(small_frame, bd=3, textvariable=self.value, font=('arial', 12, 'bold'), width=20)
        search_ent.place(x=270, y=30)

        Button(small_frame, text='Search', font=('arial', 10, 'bold'), bg='light sky blue1', width=10,
               command=self.search_value).place(x=480,
                                                y=30)

        # ===========================================================================

        Label(small_frame, text='Sort By', font=('arial', 15, 'bold'), bg='light sky blue1', ).place(x=40, y=90)

        self.combo_sort = ttk.Combobox(small_frame, font=('arial', 11, 'bold'),
                                       state='readonly')
        self.combo_sort['values'] = ('Phone No', 'Customer ID', 'Age')
        self.combo_sort.place(x=150, y=90)

        Button(small_frame, text='Sort', font=('arial', 10, 'bold'), bg='light sky blue1', width=10,
               command=self.sort_values).place(x=350, y=90)

        Label(lable_frame, text='Customers Details', font=('arial', 40, 'bold'), bg='light sky blue1',
              fg='purple1').pack()

        Button(small_frame, text='Reset', font=('arial', 10, 'bold'), bg='light sky blue1', width=10,
               command=self.show).place(x=170, y=150)

        Button(root, text='Product Page', font=('arial', 15, 'bold'), bg='pale violet red1', width=11,
               command=self.back).place(x=1380, y=20)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.customer_table = ttk.Treeview(table_frame, columns=(
            'id', 'first', 'last', 'address', 'phone', 'delivery', 'age', 'mail'),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.customer_table.xview)
        scroll_y.config(command=self.customer_table.yview)
        self.customer_table.heading('id', text='Customer ID')
        self.customer_table.heading('first', text='First Name')
        self.customer_table.heading('last', text='Last Name')
        self.customer_table.heading('address', text='Home Address')
        self.customer_table.heading('phone', text='Phone')
        self.customer_table.heading('delivery', text='Delivery Address')
        self.customer_table.heading('age', text='Age')
        self.customer_table.heading('mail', text='E-mail')
        self.customer_table['show'] = 'headings'

        self.customer_table.column('id', width=100)
        self.customer_table.column('first', width=150)
        self.customer_table.column('last', width=150)
        self.customer_table.column('address', width=300)
        self.customer_table.column('phone', width=200)
        self.customer_table.column('delivery', width=300)
        self.customer_table.column('age', width=50)
        self.customer_table.column('mail', width=200)
        self.customer_table.pack(fill=BOTH, expand=1)
        self.show()

    def show(self):
        query = "select * from customer"
        rows = self.connection.select(query)
        if len(rows) != 0:
            self.customer_table.delete(*self.customer_table.get_children())
            for row in rows:
                self.customer_table.insert('', END, values=row)

    def search_value(self):
        query = "select * from customer"
        rows = self.connection.select(query)
        index = 0
        values = CustomerTable.search(self.value.get(), rows, index)
        if len(values) == 0:
            messagebox.showinfo("error", 'please enter correct data')
        else:
            self.customer_table.delete(*self.customer_table.get_children())
            for row in values:
                self.customer_table.insert('', END, values=row)

    def sort_values(self):
        if self.combo_sort.get() == 'Phone No':
            query = "select * from customer"
            rows = self.connection.select(query)
            index = 4
            values = CustomerTable.sort(rows, index)
            if len(values) == 0:
                messagebox.showinfo("error", 'please enter correct data')
            else:
                self.customer_table.delete(*self.customer_table.get_children())
                for row in values:
                    self.customer_table.insert('', END, values=row)
        elif self.combo_sort.get() == 'Customer ID':
            query = "select * from customer"
            index = 0
            rows = self.connection.select(query)
            values = CustomerTable.sort(rows, index)
            if len(values) == 0:
                messagebox.showinfo("error", 'please enter correct data')
            else:
                self.customer_table.delete(*self.customer_table.get_children())
                for row in values:
                    self.customer_table.insert('', END, values=row)
        else:
            query = "select * from customer"
            rows = self.connection.select(query)
            index = 6
            values = CustomerTable.sort(rows, index)
            if len(values) == 0:
                messagebox.showinfo("error", 'please enter correct data')
            else:
                self.customer_table.delete(*self.customer_table.get_children())
                for row in values:
                    self.customer_table.insert('', END, values=row)

    @classmethod
    def search(cls, item, list, index):
        row = []
        for i in range(len(list)):
            for j in range(len(list[i])):
                if str(item) == str(list[i][index]):
                    row.append(list[i])
                    break
        return row

    @classmethod
    def sort(cls, rows, index):
        result = True
        while result:
            result = False
            for i in range(len(rows) - 1):
                if rows[i][index] > rows[i + 1][index]:
                    rows[i], rows[i + 1] = rows[i + 1], rows[i]
                    result = True
        return rows

    def back(self):
        wn = Toplevel()
        Second_frame(wn)
        self.root.withdraw()


class DiscountContent:
    def __init__(self, root):
        self.root = root
        root.title('Discount and Content')
        root.geometry('1540x790+0+0')
        root.iconbitmap('icon.ico')

        self.connection = Database()

        image = Image.open("content.png")  # Inserting Background Image
        self.photo = image.resize((1540, 799), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.photo)
        lbl = Label(root, image=self.photo, bg='black')
        lbl.image_ref = self.photo
        lbl.grid(row=0, column=0)

        dis_con_frame = Frame(root, bg='brown2')
        dis_con_frame.place(x=30, y=200, height=300, width=550)

        label_frame = Frame(root, bg='brown2')
        label_frame.place(x=30, y=110, height=90, width=550)

        self.discount_id = StringVar()
        self.discount = StringVar()
        self.content_id = StringVar()
        self.content = StringVar()

        label = Label(label_frame, text='Discount and Content', bg='brown2', fg='Dark Slate Gray1',
                      font=('arial', 30, 'bold'), )
        label.pack(pady=10)

        discount_id = Label(dis_con_frame, text='Discount ID', fg='green2', font=('Arial', 20, 'bold'),
                            bg='brown2', )
        discount_id.grid(row=1, column=0, pady=20, sticky=W)

        discount_id_ent = Entry(dis_con_frame, textvariable=self.discount_id, bd=3, font=('arial', 15, 'bold'),
                                relief=GROOVE, )
        discount_id_ent.grid(row=1, column=1, padx=15, pady=20, sticky=W)

        discount_percent = Label(dis_con_frame, text='Discount', fg='green2', font=('Arial', 20, 'bold'),
                                 bg='brown2')
        discount_percent.grid(row=2, column=0, sticky=W)

        discount_ent = Entry(dis_con_frame, bd=3, textvariable=self.discount, font=('arial', 15, 'bold'),
                             relief=GROOVE, )
        discount_ent.grid(row=2, column=1, padx=15, pady=20, sticky=W)

        content_id = Label(dis_con_frame, text='Content ID', fg='green2', font=('Arial', 20, 'bold'), bg='brown2')
        content_id.grid(row=3, column=0, sticky=W)

        content_id_ent = Entry(dis_con_frame, bd=3, textvariable=self.content_id, font=('arial', 15, 'bold'),
                               relief=GROOVE, )
        content_id_ent.grid(row=3, column=1, padx=15, pady=20, sticky=W)

        content = Label(dis_con_frame, text='Content', fg='green2', font=('Arial', 20, 'bold'), bg='brown2', )
        content.grid(row=4, column=0, sticky=W)

        content_ent = Entry(dis_con_frame, bd=3, textvariable=self.content, font=('arial', 15, 'bold'),
                            relief=GROOVE, )
        content_ent.grid(row=4, column=1, padx=15, pady=20, sticky=W)

        back = Button(root, text='Product Page', font=('arial', 15, 'bold'), bg='indian red1', command=self.product)
        back.place(x=1350, y=20)

        table_discount_frame = Frame(root, bd=4)
        table_discount_frame.place(x=600, y=200, width=300, height=400)

        table_content_frame = Frame(root, bd=4)
        table_content_frame.place(x=1000, y=200, width=300, height=400)

        # for discount table

        scroll_y = Scrollbar(table_discount_frame, orient=VERTICAL)

        self.discount_data = ttk.Treeview(table_discount_frame, columns=('DiscountID', 'Discount'),
                                          yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.discount_data.yview)

        self.discount_data.heading('DiscountID', text='Discount ID')
        self.discount_data.heading('Discount', text='Discount')
        self.discount_data['show'] = 'headings'

        self.discount_data.column('DiscountID', width=50)
        self.discount_data.column('Discount', width=100)
        self.discount_data.pack(fill=BOTH, expand=1)
        self.discount_data.bind("<ButtonRelease-1>", self.get_discount_data)
        self.show_discount()

        #  for content table
        scroll_y = Scrollbar(table_content_frame, orient=VERTICAL)

        self.content_data = ttk.Treeview(table_content_frame, columns=('ContentID', 'Content'),
                                         yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.content_data.yview)

        self.content_data.heading('ContentID', text='Content ID')
        self.content_data.heading('Content', text='Content')
        self.content_data['show'] = 'headings'

        self.content_data.column('ContentID', width=50)
        self.content_data.column('Content', width=100)
        self.content_data.pack(fill=BOTH, expand=1)
        self.content_data.bind("<ButtonRelease-1>", self.get_content_data)
        self.show_content()

        clear_but = Button(root, text='Clear', bg='brown2', bd=3, font=('arial', '12', 'bold'), width=10,
                           command=self.clear)
        clear_but.place(x=50, y=520)

        add_dis_but = Button(root, text='Add Discount', bg='brown2', bd=3, font=('arial', '12', 'bold'), width=12,
                             command=self.add_discount)
        add_dis_but.place(x=190, y=520)

        add_con_but = Button(root, text='Add Content', bg='brown2', bd=3, font=('arial', '12', 'bold'), width=12,
                             command=self.add_content)
        add_con_but.place(x=350, y=520)

        delete_dis_but = Button(root, text='Delete Discount', bg='brown2', bd=3, font=('arial', '12', 'bold'),
                                width=13,
                                command=self.delete_discount)
        delete_dis_but.place(x=600, y=610)

        update_dis_but = Button(root, text='Update Discount', bg='brown2', bd=3, font=('arial', '12', 'bold'),
                                width=13,
                                command=self.update_discount)
        update_dis_but.place(x=750, y=610)

        delete_con_but = Button(root, text='Delete Content', bg='brown2', bd=3, font=('arial', '12', 'bold'),
                                width=13,
                                command=self.delete_content)
        delete_con_but.place(x=1000, y=610)

        update_con_but = Button(root, text='Update Content', bg='brown2', bd=3, font=('arial', '12', 'bold'),
                                width=13,
                                command=self.update_content)
        update_con_but.place(x=1150, y=610)

    def show_discount(self):
        query = 'select * from discount'
        values = self.connection.select(query)

        if len(values) != 0:
            self.discount_data.delete(*self.discount_data.get_children())
            for item in values:
                self.discount_data.insert('', END, values=item)

    def show_content(self):
        query = 'select * from content'
        values = self.connection.select(query)

        if len(values) != 0:
            self.content_data.delete(*self.content_data.get_children())
            for item in values:
                self.content_data.insert('', END, values=item)

    def clear(self):
        list = [self.discount,self.content_id,self.content_id,self.content]
        CustomerDetails.solution(list)

    def get_discount_data(self, ev):
        extract_data = self.discount_data.focus()
        entries = self.discount_data.item(extract_data)
        row = entries['values']
        self.discount_id.set(row[0])
        self.discount.set(row[1])

    def get_content_data(self, ev):
        extract_data = self.content_data.focus()
        entries = self.content_data.item(extract_data)
        row = entries['values']
        self.content_id.set(row[0])
        self.content.set(row[1])

    def add_content(self):
        if self.content_id.get() == '' or self.content.get() == '':
            messagebox.showinfo('Adding data', 'No values to Add')
        else:
            query = "insert into content (content_id, content_name ) values(%s,%s);"
            data_ref = Offer(self.discount_id.get(), self.discount.get(), self.content_id.get(), self.content.get())
            values = (int(data_ref.get_content_id()), data_ref.get_content(),)
            self.connection.add(query, values)
            messagebox.showinfo('Content data', 'Content data has been inserted successfully')
            self.show_content()
            self.clear()

    def add_discount(self):
        if self.discount_id.get() == '' or self.discount.get() == '':
            messagebox.showinfo('Adding Discount', 'No data to Add')
        else:
            query = "insert into discount values(%s,%s);"
            data_ref = Offer(self.discount_id.get(), self.discount.get(), self.content_id.get(), self.content.get())
            values = (int(data_ref.get_discount_id()), int(data_ref.get_discount()),)
            self.connection.add(query, values)
            messagebox.showinfo('Discount data', 'Discount data has been inserted successfully')
            self.show_discount()
            self.clear()

    def delete_discount(self):
        if self.discount_id.get() == '' or self.discount.get() == '':
            messagebox.showinfo('Deleting data', 'No data to Delete')
        query = "Delete from discount where dis_id=%s"
        data_ref = Offer(self.discount_id.get(), self.discount.get(), self.content_id.get(), self.content.get())
        values = (int(data_ref.get_discount_id()),)
        self.connection.delete(query, values)
        messagebox.showinfo('Delete Discount data', 'Discount data has been deleted successfully')
        self.show_discount()
        self.clear()

    def delete_content(self):
        if self.content_id.get() == '' or self.content.get() == '':
            messagebox.showinfo('Deleting data', 'No values to Delete')
        else:
            query = "Delete from content where content_id=%s"
            data_ref = Offer(self.discount_id.get(), self.discount.get(), self.content_id.get(), self.content.get())
            values = (int(data_ref.get_content_id()),)
            self.connection.delete(query, values)
            messagebox.showinfo('Delete Content data', 'Content data has been deleted successfully')
            self.show_content()
            self.clear()

    def update_discount(self):
        if self.discount_id.get() == '' or self.discount.get() == '':
            messagebox.showinfo('Updating data', 'No values to Update')
        else:
            query = "update discount set discountoffer=%s where dis_id=%s"
            data_ref = Offer(self.discount_id.get(), self.discount.get(), self.content_id.get(), self.content.get())
            values = (int(data_ref.get_discount()), int(data_ref.get_discount_id()))
            self.connection.update(query, values)
            messagebox.showinfo('Updating Discount data', 'Discount data has been updated successfully')
            self.show_discount()
            self.clear()

    def update_content(self):
        if self.content_id.get() == '' or self.content.get() == '':
            messagebox.showinfo('Updating data', 'No values to Update')
        else:
            query = "update content set content_name=%s where content_id=%s"
            data_ref = Offer(self.discount_id.get(), self.discount.get(), self.content_id.get(), self.content.get())
            values = (data_ref.get_content(), int(data_ref.get_content_id()))
            self.connection.update(query, values)
            messagebox.showinfo('Updating Content data', 'Content data has been updated successfully')
            self.show_content()
            self.clear()

    def product(self):
        wn = Toplevel()
        Second_frame(wn)
        self.root.withdraw()


class CustomerOrder:
    def __init__(self, root):
        self.root = root
        root.title('Customer Order')
        root.geometry('1540x790+0+0')
        root.iconbitmap('icon.ico')

        image = Image.open('order.jpg')
        image = image.resize((1540, 799), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        lbl_image = Label(root, image=photo)
        lbl_image.my_image = photo
        lbl_image.pack()

        self.connection = Database()

        table_frame = Frame(root, bd=3, relief=GROOVE)
        table_frame.place(x=300, y=300, height=450, width=900)

        lable_frame = Frame(root, relief=GROOVE, bg='light sky blue1', bd=4)
        lable_frame.place(x=300, y=12, width=900, height=50)

        small_frame = Frame(root, relief=GROOVE, bg='light sky blue1', bd=4)
        small_frame.place(x=300, y=60, width=900, height=220)

        Label(small_frame, text='Search By Customer ID', font=('arial', 15, 'bold'), bg='light sky blue1', ).place(x=40,
                                                                                                                   y=30)

        self.value = StringVar()
        self.customer_id = StringVar()
        self.update_var = StringVar()

        search_ent = Entry(small_frame, bd=3, textvariable=self.value, font=('arial', 12, 'bold'), width=20)
        search_ent.place(x=290, y=30)

        Button(small_frame, text='Search', font=('arial', 10, 'bold'), bg='light sky blue1', width=10,
               command=self.search_value).place(x=510,
                                                y=30)

        Label(small_frame, text='Sort By', font=('arial', 15, 'bold'), bg='light sky blue1', ).place(x=90, y=90)

        Label(small_frame, text='Update Status', font=('arial', 15, 'bold'), bg='light sky blue1', ).place(x=60, y=140)

        update_ent = Entry(small_frame, bd=3, textvariable=self.update_var, font=('arial', 12, 'bold'), width=20)
        update_ent.place(x=290, y=140)

        Button(small_frame, text='Update', font=('arial', 10, 'bold'), bg='light sky blue1', width=10,
               command=self.update
               ).place(x=510, y=140)

        self.combo_sort = ttk.Combobox(small_frame, font=('arial', 11, 'bold'),
                                       state='readonly')
        self.combo_sort['values'] = ('Customer ID', 'Cost', 'Discount', 'Quantity')
        self.combo_sort.place(x=290, y=90)

        Button(small_frame, text='Sort', font=('arial', 10, 'bold'), bg='light sky blue1', width=10,
               command=self.sort_values).place(x=510, y=90)

        Label(lable_frame, text='Customers Orders', font=('arial', 40, 'bold'), bg='light sky blue1',
              fg='purple1').pack()

        Button(small_frame, text='Reset', font=('arial', 10, 'bold'), bg='light sky blue1', width=10,
               command=self.show).place(x=780, y=20)

        Button(root, text='Product Page', font=('arial', 15, 'bold'), bg='pale violet red1', width=11,
               command=self.product).place(x=1380, y=20)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.customer_table = ttk.Treeview(table_frame, columns=(
            'ordid', 'cusid', 'first', 'last', 'productname', 'quantity', 'cost', 'discount', 'address', 'status'),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.customer_table.xview)
        scroll_y.config(command=self.customer_table.yview)
        self.customer_table.heading('ordid', text='Order ID')
        self.customer_table.heading('cusid', text='Customer ID')
        self.customer_table.heading('first', text='First Name')
        self.customer_table.heading('last', text='Last Name')
        self.customer_table.heading('productname', text='Product Name')
        self.customer_table.heading('quantity', text='Quantity')
        self.customer_table.heading('cost', text='Cost')
        self.customer_table.heading('discount', text='Discount %')
        self.customer_table.heading('address', text='Delivery Address')
        self.customer_table.heading('status', text='Status')
        self.customer_table['show'] = 'headings'

        self.customer_table.column('ordid', width=100)
        self.customer_table.column('cusid', width=100)
        self.customer_table.column('first', width=100)
        self.customer_table.column('last', width=100)
        self.customer_table.column('productname', width=200)
        self.customer_table.column('quantity', width=100)
        self.customer_table.column('cost', width=100)
        self.customer_table.column('discount', width=100)
        self.customer_table.column('address', width=300)
        self.customer_table.column('status', width=100)
        self.customer_table.pack(fill=BOTH, expand=1)
        self.customer_table.bind('<ButtonRelease-1>', self.get_value)
        self.show()

    def get_value(self, ev):
        extract_data = self.customer_table.focus()
        content = self.customer_table.item(extract_data)
        row = content['values']
        self.customer_id.set(row[1])

    def update(self):
        if self.update_var.get() == '':
            messagebox.showinfo('Updating', 'No data to update')
        else:
            query = 'update customer_product set Status=%s where customer_Id=%s'
            values = (self.update_var.get(), self.customer_id.get())
            self.connection.update(query, values)
            messagebox.showinfo('Data Updating', 'Delivery status has been updated')
            self.show()

    def show(self):
        query = "select order_id,customer.cus_Id,customer.first_name,customer.last_name,product.product_name," \
                "customer_product.Quantity,product.cost,discount.discountoffer,customer.delivery_address," \
                "customer_product.Status FROM customer_product,product,customer,discount where customer.cus_Id = " \
                "customer_product.customer_Id and customer_product.product_code=product.product_code and " \
                "product.discount_code=discount.dis_id; "
        rows = self.connection.select(query)
        if len(rows) != 0:
            self.customer_table.delete(*self.customer_table.get_children())
            for row in rows:
                self.customer_table.insert('', END, values=row)

    def search_value(self):
        query = "select order_id,customer.cus_Id,customer.first_name,customer.last_name,product.product_name," \
                "customer_product.Quantity,product.cost,discount.discountoffer,customer.delivery_address," \
                "customer_product.Status FROM customer_product,product,customer,discount where customer.cus_Id = " \
                "customer_product.customer_Id and customer_product.product_code=product.product_code and " \
                "product.discount_code=discount.dis_id; "
        rows = self.connection.select(query)
        index = 1
        values = CustomerTable.search(self.value.get(), rows, index)
        self.customer_table.delete(*self.customer_table.get_children())
        for row in values:
            self.customer_table.insert('', END, values=row)

    def sort_values(self):
        if self.combo_sort.get() == 'Customer ID':
            query = "select order_id,customer.cus_Id,customer.first_name,customer.last_name,product.product_name," \
                    "customer_product.Quantity,product.cost,discount.discountoffer,customer.delivery_address," \
                    "customer_product.Status FROM customer_product,product,customer,discount where customer.cus_Id = " \
                    "customer_product.customer_Id and customer_product.product_code=product.product_code and " \
                    "product.discount_code=discount.dis_id; "
            rows = self.connection.select(query)
            index = 1
            values = CustomerTable.sort(rows, index)
            self.customer_table.delete(*self.customer_table.get_children())
            for row in values:
                self.customer_table.insert('', END, values=row)
        elif self.combo_sort.get() == 'Discount':
            query = "select order_id,customer.cus_Id,customer.first_name,customer.last_name,product.product_name," \
                    "customer_product.Quantity,product.cost,discount.discountoffer,customer.delivery_address," \
                    "customer_product.Status FROM customer_product,product,customer,discount where customer.cus_Id = " \
                    "customer_product.customer_Id and customer_product.product_code=product.product_code and " \
                    "product.discount_code=discount.dis_id; "
            index = 7
            rows = self.connection.select(query)
            values = CustomerTable.sort(rows, index)
            self.customer_table.delete(*self.customer_table.get_children())
            for row in values:
                self.customer_table.insert('', END, values=row)

        elif self.combo_sort.get() == 'Cost':
            query = "select order_id,customer.cus_Id,customer.first_name,customer.last_name,product.product_name," \
                    "customer_product.Quantity,product.cost,discount.discountoffer,customer.delivery_address," \
                    "customer_product.Status FROM customer_product,product,customer,discount where customer.cus_Id = " \
                    "customer_product.customer_Id and customer_product.product_code=product.product_code and " \
                    "product.discount_code=discount.dis_id; "
            index = 6
            rows = self.connection.select(query)
            values = CustomerTable.sort(rows, index)
            self.customer_table.delete(*self.customer_table.get_children())
            for row in values:
                self.customer_table.insert('', END, values=row)
        else:
            query = "select order_id,customer.cus_Id,customer.first_name,customer.last_name,product.product_name," \
                    "customer_product.Quantity,product.cost,discount.discountoffer,customer.delivery_address," \
                    "customer_product.Status FROM customer_product,product,customer,discount where customer.cus_Id = " \
                    "customer_product.customer_Id and customer_product.product_code=product.product_code and " \
                    "product.discount_code=discount.dis_id; "
            rows = self.connection.select(query)
            index = 6
            values = CustomerTable.sort(rows, index)
            self.customer_table.delete(*self.customer_table.get_children())
            for row in values:
                self.customer_table.insert('', END, values=row)

    def product(self):
        wm = Toplevel()
        Second_frame(wm)
        self.root.withdraw()


class Shop:
    def __init__(self, root):
        self.root = root
        root.title('Shop')
        root.geometry('1540x790+0+0')
        root.iconbitmap('icon.ico')

        image = Image.open('ShopOnline.jpg')
        image = image.resize((1540, 799), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        lbl_image = Label(root, image=photo)
        lbl_image.my_image = photo
        lbl_image.pack()

        self.connection = Database()

        table_frame = Frame(root)
        table_frame.place(x=600, y=90, height=600, width=800)

        data_frame = Frame(root, bd=3, bg='snow', relief=GROOVE)
        data_frame.place(x=30, y=150, height=500, width=400)

        customer_id = Label(data_frame, text='Customer ID', font=('arial', 14, 'bold'), width=10, bg='snow')
        customer_id.place(x=20, y=20)

        customer_mail = Label(data_frame, text='E-Mail', font=('arial', 14, 'bold'), width=10, bg='snow')
        customer_mail.place(x=20, y=80)

        customer_quantity = Label(data_frame, text='Quantity', font=('arial', 14, 'bold'), width=10, bg='snow')
        customer_quantity.place(x=20, y=140)

        search = Label(data_frame, text='Search Cost', font=('arial', 14, 'bold'), width=10, bg='snow')
        search.place(x=20, y=220)

        sort = Label(data_frame, text='Sort By', font=('arial', 14, 'bold'), width=10, bg='snow')
        sort.place(x=20, y=320)

        self.combo = ttk.Combobox(data_frame, font=('arial', 10, 'bold'),
                                  state='readonly')
        self.combo['values'] = ['Discount', 'Stock', 'Cost']
        self.combo.place(x=200, y=320)

        self.id = StringVar()
        self.mail = StringVar()
        self.quantity = StringVar()
        self.max_quantity = StringVar()
        self.product_code = StringVar()
        self.date = datetime.date.today()
        self.search_value = StringVar()

        id_ent = Entry(data_frame, font=('arial', 14, 'bold'), textvariable=self.id, width=15, bd=3)
        id_ent.place(x=200, y=20)

        mail_ent = Entry(data_frame, font=('arial', 14, 'bold'), textvariable=self.mail, width=15, bd=3)
        mail_ent.place(x=200, y=80)

        quantity_ent = Entry(data_frame, font=('arial', 14, 'bold'), textvariable=self.quantity, width=15, bd=3)
        quantity_ent.place(x=200, y=140)

        search_ent = Entry(data_frame, font=('arial', 14, 'bold'), textvariable=self.search_value, width=15, bd=3)
        search_ent.place(x=200, y=220)

        Button(data_frame, text='Search', font=('arial', 12, 'bold'), width=10, bg='snow',
               command=self.search_item, ).place(x=220, y=260)
        Button(data_frame, text='Sort', font=('arial', 12, 'bold'), width=10, bg='snow',
               command=self.sort_values, ).place(x=220, y=350)
        Button(data_frame, text='Track Order', font=('arial', 12, 'bold'), width=10, bg='Spring green',
               command=self.track_order).place(x=220,
                                               y=450)
        Button(data_frame, text='Refresh Data', font=('arial', 12, 'bold'), width=10, bg='snow',
               command=self.show).place(x=40, y=450)

        Button(root, text='Home Page', font=('arial', 14, 'bold'), width=10, bg='snow', command=self.home).place(x=1350,
                                                                                                                 y=20)
        Button(root, text='Buy', font=('arial', 14, 'bold'), width=10, bg='Spring green', command=self.buy).place(x=600,
                                                                                                                  y=700)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.shop_table = ttk.Treeview(table_frame, columns=(
            'productid', 'productname', 'cost', 'describe', 'stock', 'discount', 'content', 'discountoffer',
            'actualcont'),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.shop_table.xview)
        scroll_y.config(command=self.shop_table.yview)
        self.shop_table.heading('productid', text='Product ID')
        self.shop_table.heading('productname', text='Product Name')
        self.shop_table.heading('cost', text='Cost')
        self.shop_table.heading('describe', text='Description')
        self.shop_table.heading('stock', text='Stock')
        self.shop_table.heading('discount', text='Discount Code')
        self.shop_table.heading('content', text='Content Code')
        self.shop_table.heading('discountoffer', text='Discount%')
        self.shop_table.heading('actualcont', text='Content')
        self.shop_table['show'] = 'headings'

        self.shop_table.column('productid', width=100)
        self.shop_table.column('productname', width=100)
        self.shop_table.column('content', width=100)
        self.shop_table.column('discount', width=100)
        self.shop_table.column('cost', width=100)
        self.shop_table.column('describe', width=300)
        self.shop_table.column('stock', width=100)
        self.shop_table.column('discountoffer', width=100)
        self.shop_table.column('actualcont', width=100)
        self.shop_table.pack(fill=BOTH, expand=1)
        self.shop_table.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def show(self):
        query = "select product_code,product_name,cost,description,stock,discount_code,content_code," \
                "discount.discountoffer,content.content_name from product,discount,content where " \
                "discount.dis_id=product.discount_code and product.content_code=content.content_id; "
        rows = self.connection.select(query)
        if len(rows) != 0:
            self.shop_table.delete(*self.shop_table.get_children())
            for row in rows:
                self.shop_table.insert('', END, values=row)

    def get_data(self, ev):
        extract_data = self.shop_table.focus()
        contents = self.shop_table.item(extract_data)
        row = contents['values']
        self.product_code.set(row[0])
        self.max_quantity.set(row[4])

    def buy(self):
        if self.id.get() == '' or self.mail.get() == '' or self.quantity.get() == '':
            messagebox.showwarning("Customer data", "Please fill entries")
        elif self.quantity.get() > self.max_quantity.get():
            messagebox.showwarning("Stock", "Quantity is not enough. \n Buy less stock.")
        else:
            message = messagebox.askyesno("Ordering", "Are you sure you want to buy")
            if message:
                query = "select email from customer where cus_Id=%s"
                value = (self.id.get(),)
                row = (self.connection.selectvalue(query, value))
                print(self.mail.get(), row)
                if self.mail.get() == (row[0][0]):
                    query = "insert into customer_product (product_code, customer_Id, Quantity, order_date,Status) values(%s,%s,%s,%s,%s);"
                    shop_ref = Buy(self.id.get(), self.mail.get(), self.quantity.get(), self.product_code.get(),
                                   self.date)
                    values = (
                        shop_ref.get_product_code(), shop_ref.get_id(), shop_ref.get_quantity(), shop_ref.get_date(),
                        'Not Shipped',)
                    self.connection.add(query, values)
                    query1 = "update product set stock=%s where product_code=%s"
                    quantity = (int(self.max_quantity.get()) - int(self.quantity.get()))
                    value1 = (quantity, int(self.product_code.get()))
                    self.connection.update(query1, value1)
                    messagebox.showinfo('Ordering', "Item has been ordered")
                    self.show()

                else:
                    messagebox.showinfo('Wait', 'Need verified ID and Email')

    def search_item(self):
        query = "select product_code,product_name,cost,description,stock,discount_code,content_code," \
                "discount.discountoffer,content.content_name from product,discount,content where " \
                "discount.dis_id=product.discount_code and product.content_code=content.content_id; "
        rows = self.connection.select(query)
        item = 2
        values = CustomerTable.search(self.search_value.get(), rows, item)
        if len(values) == 0:
            messagebox.showinfo("error", 'Invalid cost')
        else:
            self.shop_table.delete(*self.shop_table.get_children())
            for row in values:
                self.shop_table.insert('', END, values=row)

    def sort_values(self):
        if self.combo.get() == 'Discount':
            query = "select product_code,product_name,cost,description,stock,discount_code,content_code," \
                    "discount.discountoffer,content.content_name from product,discount,content where " \
                    "discount.dis_id=product.discount_code and product.content_code=content.content_id; "
            rows = self.connection.select(query)
            index = 7
            values = CustomerTable.sort(rows, index)
            self.shop_table.delete(*self.shop_table.get_children())
            for row in values:
                self.shop_table.insert('', END, values=row)
        elif self.combo.get() == 'Cost':
            query = "select product_code,product_name,cost,description,stock,discount_code,content_code," \
                    "discount.discountoffer,content.content_name from product,discount,content where " \
                    "discount.dis_id=product.discount_code and product.content_code=content.content_id; "
            index = 2
            rows = self.connection.select(query)
            values = CustomerTable.sort(rows, index)
            self.shop_table.delete(*self.shop_table.get_children())
            for row in values:
                self.shop_table.insert('', END, values=row)

        else:
            query = "select product_code,product_name,cost,description,stock,discount_code,content_code," \
                    "discount.discountoffer,content.content_name from product,discount,content where " \
                    "discount.dis_id=product.discount_code and product.content_code=content.content_id; "
            index = 4
            rows = self.connection.select(query)
            values = CustomerTable.sort(rows, index)
            self.shop_table.delete(*self.shop_table.get_children())
            for row in values:
                self.shop_table.insert('', END, values=row)

    def track_order(self):
        if self.id.get() == '':
            messagebox.showinfo('Error', 'Need Verified ID and mail')
        else:
            query = "select email from customer where cus_Id=%s"
            value = (self.id.get(),)
            row = (self.connection.selectvalue(query, value))
            if self.mail.get() == (row[0][0]):
                self.order()
            else:
                messagebox.showinfo('Order', 'Need verified ID and Email')

    def order(self):
        wn = Toplevel()
        Order(wn, self.id.get())
        self.root.withdraw()

    def home(self):
        wn = Toplevel()
        Main_frame(wn)
        self.root.withdraw()


class Order:
    def __init__(self, root, id):
        self.customer_id = id
        self.root = root
        root.title('Order List')
        root.geometry('1540x790+0+0')
        root.iconbitmap('icon.ico')

        image = Image.open('ShopOnline.jpg')
        image = image.resize((1540, 799), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        lbl_image = Label(root, image=photo)
        lbl_image.my_image = photo
        lbl_image.pack()

        self.connection = Database()

        table_frame = Frame(root)
        table_frame.place(x=200, y=90, height=300, width=1100)

        data_frame = Frame(root, bd=3, bg='snow', relief=GROOVE)
        data_frame.place(x=520, y=400, height=200, width=550)

        self.address = Text(data_frame, height=6, width=28, relief=GROOVE, bd=5)
        self.address.place(x=200, y=20)

        self.id = StringVar()

        address = Label(data_frame, text='Update Address', font=('arial', 14, 'bold'), width=12, bg='snow')
        address.place(x=20, y=60)

        Button(data_frame, text='Update', font=('arial', 14, 'bold'), width=12, bg='snow', command=self.update).place(
            x=230, y=140)
        Button(root, text='Shop', font=('arial', 14, 'bold'), width=12, bg='snow', command=self.shop).place(x=1340,
                                                                                                            y=20)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.shop_table = ttk.Treeview(table_frame, columns=(
            'customerid', 'name', 'last', 'code', 'date', 'quantity', 'productname', 'address', 'status', 'cost',
            'discount'),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.shop_table.xview)
        scroll_y.config(command=self.shop_table.yview)
        self.shop_table.heading('customerid', text='Customer ID')
        self.shop_table.heading('name', text='First Name')
        self.shop_table.heading('last', text='Last Name')
        self.shop_table.heading('code', text='Product Code')
        self.shop_table.heading('date', text='Ordered Date')
        self.shop_table.heading('quantity', text='Quantity')
        self.shop_table.heading('productname', text='Product Name')
        self.shop_table.heading('address', text='Delivery Address')
        self.shop_table.heading('status', text='Status')
        self.shop_table.heading('cost', text='Cost')
        self.shop_table.heading('discount', text='Discount %')
        self.shop_table['show'] = 'headings'

        self.shop_table.column('customerid', width=100)
        self.shop_table.column('name', width=100)
        self.shop_table.column('last', width=100)
        self.shop_table.column('code', width=100)
        self.shop_table.column('date', width=100)
        self.shop_table.column('quantity', width=100)
        self.shop_table.column('productname', width=200)
        self.shop_table.column('address', width=300)
        self.shop_table.column('status', width=100)
        self.shop_table.column('cost', width=100)
        self.shop_table.column('discount', width=100)
        self.shop_table.pack(fill=BOTH, expand=1)
        self.shop_table.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def show(self):
        query = "select customer.cus_Id,customer.first_name,customer.last_name, customer_product.Product_code , " \
                "customer_product.order_date,customer_product.Quantity, product.product_name, " \
                "customer.delivery_address,customer_product.Status, product.cost,discount.discountoffer from " \
                "customer_product,product,customer, discount where customer.cus_Id=customer_product.customer_Id and " \
                "product.product_code=customer_product.product_code and discount.dis_id=product.discount_code and " \
                "customer.cus_Id=%s "
        value = str(self.customer_id),
        rows = self.connection.selectvalue(query, value)
        if len(rows) != 0:
            self.shop_table.delete(*self.shop_table.get_children())
            for row in rows:
                self.shop_table.insert('', END, values=row)

    def get_data(self, ev):
        extract_data = self.shop_table.focus()
        contents = self.shop_table.item(extract_data)
        row = contents['values']
        self.id.set(row[0])

    def update(self):
        message = messagebox.askyesno('Processing', 'Are you sure? ')
        if message:
            if self.address.get('1.0', END) == '' or self.id.get() == '':
                messagebox.showinfo('Data Updating', 'Please fill all the entries ')
            else:
                query = 'update customer set delivery_address=%s where cus_Id=%s'
                values = (self.address.get('1.0', END), int(self.id.get()))
                self.connection.update(query, values)
                messagebox.showinfo('Data updating', 'Data has been updated')
                self.show()

    def shop(self):
        wn = Toplevel()
        Shop(wn)
        self.root.withdraw()


if __name__ == "__main__":
    root = Tk()
    Main_frame(root)
    root.mainloop()
