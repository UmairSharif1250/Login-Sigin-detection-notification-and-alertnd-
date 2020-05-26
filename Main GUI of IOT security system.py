from tkinter import *
import string



root=Tk()
def signin():
    root = Tk()

    def getvals():
        print(
            f"{namevalue.get(), Fathervalue.get(), deptvalue.get(), cellnovalue.get(), Designationvalue.get(), termvalue.get(), paswordvalue.get(), confirmvalue.get()}")

        with open("record.txt", "a") as f:
            f.write(
                f"{namevalue.get(), Fathervalue.get(), deptvalue.get(), cellnovalue.get(), Designationvalue.get(), termvalue.get(), paswordvalue.get(), confirmvalue.get()}\n")

    root.geometry("450x300")
    root.title("DATA-COLLECTION")
    # text entries

    Label(root, text="Provide your required information ", font="SUNKEN 13 bold", pady=15).grid(row=0, column=3)
    name = Label(root, text="Name", font="SUNKEN 10 bold")
    Father = Label(root, text="F-Name", font="SUNKEN 10 bold")
    dept = Label(root, text="Department", font="SUNKEN 10 bold")
    cellno = Label(root, text="Mobile", font="SUNKEN 10 bold")
    Designation = Label(root, text="Desigination", font="SUNKEN 10 bold")
    pasword = Label(root, text="Address", font="SUNKEN 10 bold")
    confirm = Label(root, text="Email", font="SUNKEN 10 bold")

    # pack text boxes

    name.grid(row=1, column=2)
    Father.grid(row=2, column=2)
    dept.grid(row=3, column=2)
    cellno.grid(row=4, column=2)
    Designation.grid(row=5, column=2)
    pasword.grid(row=6, column=2)
    confirm.grid(row=7, column=2)
    # variables for storing entries

    namevalue = StringVar()
    Fathervalue = StringVar()
    deptvalue = StringVar()
    cellnovalue = StringVar()
    Designationvalue = StringVar()
    termvalue = IntVar()
    paswordvalue = StringVar()
    confirmvalue = StringVar()

    # entry for a form  value

    nameentry = Entry(root, textvariable=namevalue)
    Fatherentry = Entry(root, textvariable=Fathervalue)
    deptentry = Entry(root, textvariable=deptvalue)
    cellnoentry = Entry(root, textvariable=cellnovalue)
    Designationentry = Entry(root, textvariable=Designationvalue)
    paswordentry = Entry(root, textvariable=paswordvalue)
    confirmentry = Entry(root, textvariable=confirmvalue)

    # packing the entry value

    nameentry.grid(row=1, column=3)
    Fatherentry.grid(row=2, column=3)
    deptentry.grid(row=3, column=3)
    cellnoentry.grid(row=4, column=3)
    Designationentry.grid(row=5, column=3)
    paswordentry.grid(row=6, column=3)
    confirmentry.grid(row=7, column=3)

    # Checkbotton and packing it
    term = Checkbutton(text="Agreed with term and conditions ", font="SUNKEN 7 bold", variable=termvalue)
    term.grid(row=8, column=3)

    # Button and packing it and assigning enter command

    b = Button(text="SUBMIT MY CREDENTIAL", command=getvals)
    b.grid(row=9, column=3)

    print("please signin")
def login():

    def getvals():
        uservalue.get()
        paswordvalue.get()
        if paswordvalue == paswordvalue.get():

            Button(root, text="Motion detection", fg="blue").grid(row=6, column=3)
            Button(root, text="Face recognition ", fg="blue").grid(row=7, column=3)
            Button(root, text="Notification ", fg="blue").grid(row=8, column=3)
            Button(root, text="Create Alert", fg="blue").grid(row=9, column=3)

        else:
            print("wrong pasword")



    root = Tk()
    root.geometry("450x200")
    root.title("SERVER LOGIN FOR ADMIN")

    Label(root, text="Use your credential information  to enter in the System", font="SUNKEN 10 bold", pady=15).grid(
        row=0,
        column=3)
    user = Label(root, text="user name", font="SUNKEN 10 bold")
    user.grid(row=1, column=2)
    pasword = Label(root, text="Pasword", font="SUNKEN 10 bold")
    pasword.grid(row=2, column=2)
    Secret = Label(root, text="Secret key", font="SUNKEN 10 bold")
    Secret.grid(row=3, column=2)

    uservalue = StringVar()
    paswordvalue = StringVar()
    Secretvalue = StringVar()

    userentry = Entry(root, textvariable=uservalue)
    paswordentry = Entry(root, textvariable=paswordvalue)
    Secretentry = Entry(root, textvariable=Secretvalue)

    userentry.grid(row=1, column=3)
    paswordentry.grid(row=2, column=3)
    Secretentry.grid(row=3, column=3)
    b = Button(bg="blue", text="NEXT ", font="SUNKEN 10 bold", command=getvals)
    b.grid(row=4, column=3)







#widthxheight
root.geometry("660x424")
#Gui Title
root.title("IOT security system")
#min size of width and height
root.minsize(300,100)

#max size of width and height
root.maxsize(660,414)

#photo= PhotoImage(file="u2.jpg")

#lable=Label(image=photo).pack()



lable5 = Label (root, text="The Internet of Things (IoT) carries enormous potential to change the world for the better."
                      ,  fg="White" ,bg="Black" ,padx=20 ,pady=50 ,font=("BOLD") ,borderwidth=10 , relief=SUNKEN  )

lable5.grid()



f1=Frame(root, bg="grey" ,borderwidth=6, relief=SUNKEN  ).grid()
#f1.pack( side="left" )
l=Label(f1, text="We Serve our best Your Satisfaction is our success " , padx=20 ,pady=20 ,font=("BOLD") ,borderwidth=10 , relief=SUNKEN ).grid()
#l.pack(pady=142)


l1=Label(root, text="Welcome to the IOT Smart Security world " , padx=20 ,pady=50 ,font=("BOLD") ,borderwidth=10 , relief=SUNKEN ).grid()
#l1.pack()


Button(root,text="LOG-IN" ,fg="blue" ,command=login).grid(row=7 ,column=0)


Button(root,text="SIGN-IN" ,fg="blue" ,command=signin).grid()
#b1=Button( bg="blue" , text="LOG-IN").pack(pady=123)

#b2=Button( bg="blue" , text="SIGN-IN" ).pack()




"""
text - add text
bg- background 
fg- foreground
font- set the font
padX- xpadding
padY- ypadding
relief- for border styling (sunken , raised ,groove , Ridge)
"""


#Important pack
#anchor= nw for side change of button or etc
#side= top, bottom ,right ,left
#fill
#padx
#pady





root.mainloop()

