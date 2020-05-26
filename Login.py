from tkinter import *

def getvals():
    uservalue.get()
    paswordvalue.get()


   # print(f"the value of user name is {uservalue.get()}")
    #print(f"the value of password is {paswordvalue.get()} ")

    if paswordvalue==paswordvalue.get():
        Button(root, text="Motion detection", fg="blue").grid(row=6, column=3)
        Button(root, text="Face recognition ", fg="blue").grid(row=7, column=3)
        Button(root, text="Notification ", fg="blue").grid(row=8, column=3)
        Button(root, text="Create Alert", fg="blue").grid(row=9, column=3)
    else:
        print("wrong pasword")




root=Tk()
root.geometry("450x200")
root.title("SERVER LOGIN FOR ADMIN")

Label(root, text="Use your credential information  to enter in the System"  ,font="SUNKEN 10 bold" , pady=15).grid(row=0,column=3)
user=Label(root,text="user name" ,font="SUNKEN 10 bold")
user.grid(row=1 ,column=2)
pasword=Label(root,text="Pasword" ,font="SUNKEN 10 bold")
pasword.grid(row=2 ,column=2)
Secret=Label(root,text="Secret key" ,font="SUNKEN 10 bold")
Secret.grid(row=3 ,column=2)


uservalue=StringVar()
paswordvalue=StringVar()
Secretvalue=StringVar()


userentry=Entry(root, textvariable=uservalue)
paswordentry=Entry(root, textvariable=paswordvalue)
Secretentry=Entry(root, textvariable=Secretvalue)

userentry.grid(row=1 ,column=3)
paswordentry.grid(row=2 ,column=3)
Secretentry.grid(row=3,column=3)
b=Button(bg="blue" ,text="Login " ,font="SUNKEN 10 bold" , command=getvals)
b.grid(row=4 ,column=3)



root.mainloop()
