from tkinter import *
from PIL import Image, ImageTk


class CustomerDetails:
    def __init__(self,root):
        self.root = root
        root.title('Customer Details')
        root.geometry('1540x790+0+0')
        root.iconbitmap('icon.ico')

        image = Image.open('background.png')
        image = image.resize((1540, 799), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        lbl = Label(root,image=photo)
        lbl.image = photo
        lbl.pack()

        self.first = StringVar()
        self.last = StringVar()
        self.age = StringVar()
        self.id = StringVar()
        self.discount = StringVar()
        self.content = StringVar()
        self.phone = StringVar()

        entry_frame = Frame(root,bg='lavender')
        entry_frame.place(x=20, y=50, height=660,width=500)

        Label(entry_frame,text='Create an Account',bg='lavender',fg='green2', font=('arial',20,'bold'),width=26).grid(row=0, column=0,columnspan=5,pady=10)

        first = Label(entry_frame,text='First Name', bg='lavender', font=('arial',15,'bold'))
        first.grid(row=1,column=0,padx=5,pady=10)

        name_ent = Entry(entry_frame,bd=3,font=('arial',14,'bold'),relief=GROOVE)
        name_ent.grid(row=1, column=1,padx=10,pady=20)

        last = Label(entry_frame,text='Last Name', bg='lavender', font=('arial',15,'bold'))
        last.grid(row=2,column=0,padx=5,pady=10)

        last_ent = Entry(entry_frame,bd=3,font=('arial',14,'bold'),relief=GROOVE)
        last_ent.grid(row=2, column=1,padx=10,pady=10)

        user_id = Label(entry_frame,text='Customer ID', bg='lavender', font=('arial',15,'bold'))
        user_id.grid(row=3, column=0,padx=5,pady=10)

        user_ent = Entry(entry_frame,bd=3,font=('arial',14,'bold'),relief=GROOVE)
        user_ent.grid(row=3, column=1,padx=10,pady=10)

        age = Label(entry_frame,text='Age', bg='lavender', font=('arial',15,'bold'))
        age.grid(row=4,column=0,padx=5,pady=10)

        age_ent = Entry(entry_frame,bd=3,font=('arial',14,'bold'),relief=GROOVE)
        age_ent.grid(row=4, column=1,padx=10,pady=10)

        home_address = Label(entry_frame,text='Home Address', bg='lavender', font=('arial',15,'bold'))
        home_address.grid(row=5,column=0,padx=5,pady=10)

        self.home = Text(entry_frame,bd=3,relief=GROOVE,height=3,width=25,font=('arial', 12,''))
        self.home.grid(row=5, column=1,padx=5,pady=10)

        email = Label(entry_frame,text='Email', bg='lavender', font=('arial',15,'bold'))
        email.grid(row=6,column=0,padx=5,pady=10)

        email_ent = Entry(entry_frame,bd=3,font=('arial',14,'bold'),relief=GROOVE)
        email_ent.grid(row=6, column=1,padx=10,pady=10)

        delivery_address = Label(entry_frame,text='Delivery Address', bg='lavender', font=('arial',15,'bold'))
        delivery_address.grid(row=7,column=0,padx=5,pady=10)

        self.deliver = Text(entry_frame, bd=3, relief=GROOVE, height=3, width=25, font=('arial', 12, ''))
        self.deliver.grid(row=7, column=1, padx=5, pady=10)

        phone = Label(entry_frame,text='Phone', bg='lavender', font=('arial',15,'bold'))
        phone.grid(row=8,column=0,padx=5,pady=10)

        phone_ent = Entry(entry_frame,bd=3,font=('arial',14,'bold'),relief=GROOVE)
        phone_ent.grid(row=8, column=1,padx=10,pady=10)


