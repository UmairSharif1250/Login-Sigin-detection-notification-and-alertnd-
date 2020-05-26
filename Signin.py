from tkinter import *
import string


import mysql.connector
mydb=mysql.connecter.connect(host="localhost" ,user="root " , password="umair1241707")
print(mydb.connection_id)


root=Tk()

def getvals():


   print(f"{namevalue.get(), Fathervalue.get() , deptvalue.get() , cellnovalue.get() , Designationvalue.get() , termvalue.get() , paswordvalue.get() , confirmvalue.get() }")

   with open("record.txt","a") as f:
       f.write(f"{namevalue.get(), Fathervalue.get() , deptvalue.get() , cellnovalue.get() , Designationvalue.get() , termvalue.get() , paswordvalue.get() , confirmvalue.get() }\n")





root.geometry("450x300")
root.title("DATA-COLLECTION")
#text entries

Label(root, text="Provide your required information "  ,font="SUNKEN 13 bold" , pady=15).grid(row=0,column=3)
name=Label(root,text="Name" ,font="SUNKEN 10 bold")
Father=Label(root,text="F-Name" ,font="SUNKEN 10 bold")
dept=Label(root,text="Department", font="SUNKEN 10 bold")
cellno=Label(root,text="Mobile" , font="SUNKEN 10 bold")
Designation=Label(root,text="Desigination" ,font="SUNKEN 10 bold")
pasword=Label(root,text="Address" ,font="SUNKEN 10 bold")
confirm=Label(root,text="Email" ,font="SUNKEN 10 bold")

#pack text boxes

name.grid(row=1 ,column=2)
Father.grid(row=2,column=2)
dept.grid(row=3 ,column=2)
cellno.grid(row=4 ,column=2)
Designation.grid(row=5 ,column=2)
pasword.grid(row=6,column=2)
confirm.grid(row=7,column=2)
#variables for storing entries

namevalue=StringVar()
Fathervalue=StringVar()
deptvalue=StringVar()
cellnovalue=StringVar()
Designationvalue=StringVar()
termvalue=IntVar()
paswordvalue=StringVar()
confirmvalue=StringVar()

#entry for a form  value

nameentry=Entry(root, textvariable=namevalue )
Fatherentry=Entry(root, textvariable=Fathervalue )
deptentry=Entry(root, textvariable=deptvalue )
cellnoentry=Entry(root, textvariable=cellnovalue )
Designationentry=Entry(root, textvariable=Designationvalue )
paswordentry=Entry(root, textvariable=paswordvalue )
confirmentry=Entry(root, textvariable=confirmvalue )


#packing the entry value

nameentry.grid(row=1 ,column=3)
Fatherentry.grid(row=2 ,column=3)
deptentry.grid(row=3 ,column=3)
cellnoentry.grid(row=4 ,column=3)
Designationentry.grid(row=5 ,column=3)
paswordentry.grid(row=6,column=3)
confirmentry.grid(row=7,column=3)

#Checkbotton and packing it
term=Checkbutton(text="Agreed with term and conditions " ,font="SUNKEN 7 bold" , variable=termvalue)
term.grid(row=8,column=3)


#Button and packing it and assigning enter command

b=Button(text="SUBMIT MY CREDENTIAL" ,command=getvals)
b.grid(row=9,column=3)

root.mainloop()