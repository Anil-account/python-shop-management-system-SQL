# # List of all users ID
# users_ID = [110, 101, 107, 103, 102, 109, 107, 104, 105, 108, 106]
# # List of users ID assigned to tasks
# tasks_ID = [107,101,105]
#
#
# def free(task, user):
#     for item in user:  # select each item from first user list
#         if item in task:    # check item from user found in task list
#             user.remove(item)   # Remove item from user list
#     return user
#
#
# find = free(tasks_ID, users_ID)
# print(find)     # Prints free users who are not assigned to task

from final_assignment.Front_app.Design import *


# class Dis_con:
#     def __init__(self, root):
#         self.root = root
#         root.title('Customer Details')
#         root.geometry('1540x790+0+0')
#         # root.iconbitmap('icon.ico')
#
#         self.connection = Database()
#
#         image = Image.open("C:/Users/acer/python-program/Front_app/content.png")  # Inserting Background Image
#         self.photo = image.resize((1540, 799), Image.ANTIALIAS)
#         self.photo = ImageTk.PhotoImage(self.photo)
#         lbl = Label(root, image=self.photo, bg='black')
#         lbl.image_ref = self.photo
#         lbl.grid(row=0, column=0)
#
#         dis_con_frame = Frame(root, bg='brown2')
#         dis_con_frame.place(x=30, y=200, height=300, width=550)
#
#         label_frame = Frame(root, bg='brown2')
#         label_frame.place(x=30, y=110, height=90, width=550)
#
#         self.discount_id = StringVar()
#         self.discount = StringVar()
#         self.content_id = StringVar()
#         self.content = StringVar()
#
#         label = Label(label_frame, text='Discount and Content', bg='brown2', fg='Dark Slate Gray1',
#                       font=('arial', 30, 'bold'), )
#         label.pack(pady=10)
#
#         discount_id = Label(dis_con_frame, text='Discount ID', fg='green2', font=('Arial', 20, 'bold'), bg='brown2', )
#         discount_id.grid(row=1, column=0, pady=20, sticky=W)
#
#         discount_id_ent = Entry(dis_con_frame, textvariable=self.discount_id, bd=3, font=('arial', 15, 'bold'),
#                                 relief=GROOVE, )
#         discount_id_ent.grid(row=1, column=1, padx=15, pady=20, sticky=W)
#
#         discount_percent = Label(dis_con_frame, text='Discount', fg='green2', font=('Arial', 20, 'bold'), bg='brown2')
#         discount_percent.grid(row=2, column=0, sticky=W)
#
#         discount_ent = Entry(dis_con_frame, bd=3, textvariable=self.discount, font=('arial', 15, 'bold'),
#                              relief=GROOVE, )
#         discount_ent.grid(row=2, column=1, padx=15, pady=20, sticky=W)
#
#         content_id = Label(dis_con_frame, text='Content ID', fg='green2', font=('Arial', 20, 'bold'), bg='brown2')
#         content_id.grid(row=3, column=0, sticky=W)
#
#         content_id_ent = Entry(dis_con_frame, bd=3, textvariable=self.content_id, font=('arial', 15, 'bold'),
#                                relief=GROOVE, )
#         content_id_ent.grid(row=3, column=1, padx=15, pady=20, sticky=W)
#
#         content = Label(dis_con_frame, text='Content', fg='green2', font=('Arial', 20, 'bold'), bg='brown2', )
#         content.grid(row=4, column=0, sticky=W)
#
#         content_ent = Entry(dis_con_frame, bd=3, textvariable=self.content, font=('arial', 15, 'bold'), relief=GROOVE, )
#         content_ent.grid(row=4, column=1, padx=15, pady=20, sticky=W)
#
#         back = Button(root, text='Product Page', font=('arial', 15, 'bold'), bg='indian red1')
#         back.place(x=1350, y=20)
#
#         table_discount_frame = Frame(root,bd=4)
#         table_discount_frame.place(x=600, y=200, width=300, height=400)
#
#         table_content_frame = Frame(root,bd=4)
#         table_content_frame.place(x=1000, y=200, width=300, height=400)
#
#         # for discount table
#
#         scroll_y = Scrollbar(table_discount_frame, orient=VERTICAL)
#
#         self.discount_data = ttk.Treeview(table_discount_frame, columns=('DiscountID', 'Discount'), yscrollcommand=scroll_y.set)
#         scroll_y.pack(side=RIGHT, fill=Y)
#         scroll_y.config(command=self.discount_data.yview)
#
#         self.discount_data.heading('DiscountID', text='Discount ID')
#         self.discount_data.heading('Discount', text='Discount')
#         self.discount_data['show'] = 'headings'
#
#         self.discount_data.column('DiscountID', width=50)
#         self.discount_data.column('Discount', width=100)
#         self.discount_data.pack(fill=BOTH, expand=1)
#         self.discount_data.bind("<ButtonRelease-1>", self.get_discount_data)
#         self.show_discount()
#
#         #  for content table
#         scroll_y = Scrollbar(table_content_frame, orient=VERTICAL)
#
#         self.content_data = ttk.Treeview(table_content_frame, columns=('ContentID', 'Content'),yscrollcommand=scroll_y.set)
#         scroll_y.pack(side=RIGHT, fill=Y)
#         scroll_y.config(command=self.content_data.yview)
#
#         self.content_data.heading('ContentID', text='Content ID')
#         self.content_data.heading('Content', text='Content')
#         self.content_data['show'] = 'headings'
#
#         self.content_data.column('ContentID', width=50)
#         self.content_data.column('Content', width=100)
#         self.content_data.pack(fill=BOTH, expand=1)
#         self.content_data.bind("<ButtonRelease-1>", self.get_content_data)
#         self.show_content()
#
#         clear_but = Button(root, text='Clear', bg='brown2', bd=3, font=('arial', '12', 'bold'), width=10,
#                            command=self.clear)
#         clear_but.place(x=50, y=520)
#
#         add_dis_but = Button(root, text='Add Discount', bg='brown2', bd=3, font=('arial', '12', 'bold'), width=12, command=self.add_discount)
#         add_dis_but.place(x=190, y=520)
#
#         add_con_but = Button(root, text='Add Content', bg='brown2', bd=3, font=('arial', '12', 'bold'), width=12,command=self.add_content)
#         add_con_but.place(x=350, y=520)
#
#         delete_dis_but = Button(root, text='Delete Discount', bg='brown2', bd=3, font=('arial', '12', 'bold'), width=13,
#                               command=self.delete_discount)
#         delete_dis_but.place(x=600, y=610)
#
#         update_dis_but = Button(root, text='Update Discount', bg='brown2', bd=3, font=('arial', '12', 'bold'), width=13,
#                               command=self.update_discount)
#         update_dis_but.place(x=750, y=610)
#
#         delete_con_but = Button(root, text='Delete Content', bg='brown2', bd=3, font=('arial', '12', 'bold'), width=13,
#                               command=self.delete_content)
#         delete_con_but.place(x=1000, y=610)
#
#         update_con_but = Button(root, text='Update Content', bg='brown2', bd=3, font=('arial', '12', 'bold'), width=13,
#                               command=self.update_content)
#         update_con_but.place(x=1150, y=610)
#
#     def show_discount(self):
#         query = 'select * from discount'
#         values = self.connection.select(query)
#
#         if len(values) != 0:
#             self.discount_data.delete(*self.discount_data.get_children())
#             for item in values:
#                 self.discount_data.insert('', END, values=item)
#
#     def show_content(self):
#         query = 'select * from content'
#         values = self.connection.select(query)
#
#         if len(values) != 0:
#             self.content_data.delete(*self.content_data.get_children())
#             for item in values:
#                 self.content_data.insert('', END, values=item)
#
#     def clear(self):
#         self.discount_id.set('')
#         self.discount.set('')
#         self.content_id.set('')
#         self.content.set('')
#
#     def get_discount_data(self, ev):
#         extract_data = self.discount_data.focus()
#         entries = self.discount_data.item(extract_data)
#         row = entries['values']
#         self.discount_id.set(row[0])
#         self.discount.set(row[1])
#
#     def get_content_data(self, ev):
#         extract_data = self.content_data.focus()
#         entries = self.content_data.item(extract_data)
#         row = entries['values']
#         self.content_id.set(row[0])
#         self.content.set(row[1])
#
#     def add_content(self):
#         if self.content_id.get() == '' or self.content.get() == '':
#             messagebox.showinfo('Adding data', 'No values to Add')
#         else:
#             query = "insert into content (content_id, content_name ) values(%s,%s);"
#             data_ref = Offer(self.discount_id.get(), self.discount.get(), self.content_id.get(), self.content.get())
#             values = (int(data_ref.get_content_id()), data_ref.get_content(),)
#             self.connection.add(query, values)
#             messagebox.showinfo('Content data', 'Content data has been inserted successfully')
#             self.show_content()
#             self.clear()
#
#     def add_discount(self):
#         if self.discount_id.get() == '' or self.discount.get() == '':
#             messagebox.showinfo('Adding Discount', 'No data to Add')
#         else:
#             query = "insert into discount values(%s,%s);"
#             data_ref = Offer(self.discount_id.get(), self.discount.get(), self.content_id.get(), self.content.get())
#             values = (int(data_ref.get_discount_id()), int(data_ref.get_discount()),)
#             self.connection.add(query, values)
#             messagebox.showinfo('Discount data', 'Discount data has been inserted successfully')
#             self.show_discount()
#             self.clear()
#
#     def delete_discount(self):
#         if self.discount_id.get() == '' or self.discount.get() == '':
#             messagebox.showinfo('Deleting data', 'No data to Delete')
#         query = "Delete from discount where dis_id=%s"
#         data_ref = Offer(self.discount_id.get(), self.discount.get(), self.content_id.get(), self.content.get())
#         values = (int(data_ref.get_discount_id()),)
#         self.connection.delete(query, values)
#         messagebox.showinfo('Delete Discount data', 'Discount data has been deleted successfully')
#         self.show_discount()
#         self.clear()
#
#     def delete_content(self):
#         if self.content_id.get() == '' or self.content.get() == '':
#             messagebox.showinfo('Deleting data', 'No values to Delete')
#         else:
#             query = "Delete from content where content_id=%s"
#             data_ref = Offer(self.discount_id.get(), self.discount.get(), self.content_id.get(), self.content.get())
#             values = (int(data_ref.get_content_id()),)
#             self.connection.delete(query,values)
#             messagebox.showinfo('Delete Content data', 'Content data has been deleted successfully')
#             self.show_content()
#             self.clear()
#
#     def update_discount(self):
#         if self.discount_id.get() == '' or self.discount.get() == '':
#             messagebox.showinfo('Updating data', 'No values to Update')
#         else:
#             query = "update discount set discountoffer=%s where dis_id=%s"
#             data_ref = Offer(self.discount_id.get(), self.discount.get(), self.content_id.get(), self.content.get())
#             values = (int(data_ref.get_discount()), int(data_ref.get_discount_id()))
#             self.connection.update(query,values)
#             messagebox.showinfo('Updating Discount data', 'Discount data has been updated successfully')
#             self.show_discount()
#             self.clear()
#
#     def update_content(self):
#         if self.content_id.get() == '' or self.content.get() == '':
#             messagebox.showinfo('Updating data', 'No values to Update')
#         else:
#             query = "update content set content_name=%s where content_id=%s"
#             data_ref = Offer(self.discount_id.get(), self.discount.get(), self.content_id.get(), self.content.get())
#             values = (data_ref.get_content(), int(data_ref.get_content_id()))
#             self.connection.update(query,values)
#             messagebox.showinfo('Updating Content data', 'Content data has been updated successfully')
#             self.show_content()
#             self.clear()
#
class Shop:
    def __init__(self, root):
        self.root = root
        root.title('Shop')
        root.geometry('1540x790+0+0')
        # root.iconbitmap('icon.ico')

        image = Image.open('/final_assignment/Front_app/ShopOnline.jpg')
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
        self.combo['values'] = ['Discount', 'Content', 'Stock', 'Cost']
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

        Button(root, text='Home Page', font=('arial', 14, 'bold'), width=10, bg='snow').place(x=1350, y=20)
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
                    shop_ref.get_product_code(), shop_ref.get_id(), shop_ref.get_quantity(), shop_ref.get_date(),'Not Shipped',)
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
        print(rows)
        values = Shop.search(self.search_value.get(), rows)
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
            values = Shop.sort(rows, index)
            self.shop_table.delete(*self.shop_table.get_children())
            for row in values:
                self.shop_table.insert('', END, values=row)
        elif self.combo.get() == 'Content':
            query = "select product_code,product_name,cost,description,stock,discount_code,content_code," \
                    "discount.discountoffer,content.content_name from product,discount,content where " \
                    "discount.dis_id=product.discount_code and product.content_code=content.content_id; "
            index = 8
            rows = self.connection.select(query)
            values = Shop.sort(rows, index)
            self.shop_table.delete(*self.shop_table.get_children())
            for row in values:
                self.shop_table.insert('', END, values=row)

        elif self.combo.get() == 'Stock':
            query = "select product_code,product_name,cost,description,stock,discount_code,content_code," \
                    "discount.discountoffer,content.content_name from product,discount,content where " \
                    "discount.dis_id=product.discount_code and product.content_code=content.content_id; "
            index = 0
            rows = self.connection.select(query)
            values = Shop.sort(rows, index)
            self.shop_table.delete(*self.shop_table.get_children())
            for row in values:
                self.shop_table.insert('', END, values=row)
        else:
            query = "select product_code,product_name,cost,description,stock,discount_code,content_code," \
                    "discount.discountoffer,content.content_name from product,discount,content where " \
                    "discount.dis_id=product.discount_code and product.content_code=content.content_id; "
            rows = self.connection.select(query)
            index = 6
            values = Shop.sort(rows, index)
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
        Order(wn,self.id.get())
        self.root.withdraw()

    @classmethod
    def search(cls, item, list):
        row = []
        for i in range(len(list)):
            for j in range(len(list[i])):
                if str(item) == str(list[i][2]):
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


class Order:
    def __init__(self, root,id):
        self.customer_id=id
        self.root = root
        root.title('Order List')
        root.geometry('1540x790+0+0')
        # root.iconbitmap('icon.ico')

        image = Image.open('/final_assignment/Front_app/ShopOnline.jpg')
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
        Button(root, text='Shop', font=('arial', 14, 'bold'), width=12, bg='snow', command=self.shop).place(x=1340, y=20)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.shop_table = ttk.Treeview(table_frame, columns=(
            'customerid', 'name', 'last', 'code', 'date', 'quantity', 'productname', 'address','status'),
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
        self.shop_table.pack(fill=BOTH, expand=1)
        self.shop_table.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def show(self):
        query = "select customer.cus_Id,customer.first_name,customer.last_name, customer_product.Product_code ," \
                "customer_product.order_date,customer_product.Quantity, product.product_name," \
                "customer.delivery_address,customer_product.Status from customer_product,product," \
                "customer where customer.cus_Id=customer_product.customer_Id and " \
                "product.product_code=customer_product.product_code and customer.cus_Id=%s "
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


