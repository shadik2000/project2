import sqlite3
from tkinter import*
from tkinter import messagebox

root=Tk()
root.title("Facebook")
root.geometry('600x450')
e1=StringVar()
e2=StringVar()
e3=StringVar()
e4=StringVar()
e5=StringVar()
e6=StringVar()
var=StringVar()
delete=StringVar()

Label(root,text="First Name").grid(row=0,column=0)
Label(root,text="Last Name").grid(row=1,column=0)
Label(root,text="Age").grid(row=2,column=0)
Label(root,text="City").grid(row=3,column=0)
Label(root,text="Zipcode").grid(row=4,column=0)
Label(root,text="Password").grid(row=5,column=0)
Label(root,text="Select Your Gender").grid(row=6,column=0)

Radiobutton(root,value="Male",text="Male",variable=var,width=20).grid(row=6,column=1)
Radiobutton(root,value="Female",text="Female",variable=var,width=20).grid(row=6,column=2)

E1=Entry(root,textvariable=e1,width=40).grid(row=0,column=1,pady=3)
E2=Entry(root,textvariable=e2,width=40).grid(row=1,column=1,pady=3)
E3=Entry(root,textvariable=e3,width=40).grid(row=2,column=1,pady=3)
E4=Entry(root,textvariable=e4,width=40).grid(row=3,column=1,pady=3)
E5=Entry(root,textvariable=e5,width=40).grid(row=4,column=1,pady=3)
E6=Entry(root,textvariable=e6,width=40).grid(row=5,column=1,pady=3)


def create_table():
         conn=sqlite3.connect("facebook.db")
         c=conn.cursor()
         query="CREATE TABLE users(Firstname text,Lastname text,Age text,City text,Zipcode text,password text,Gender text)"
         c.execute(query)
         messagebox.showinfo("Success","Table Sucessfully created")
         conn.commit()
         conn.close()
        

def Add_data():
    fname=e1.get()
    lname=e2.get()
    age=e3.get()
    city=e4.get()
    zipcode=e5.get()
    password=e6.get()
    gender=var.get()
    conn1=sqlite3.connect("facebook.db")
    c1=conn1.cursor()
    my_data=(fname,lname,age,city,zipcode,password,gender)
    query2="INSERT INTO users values(?,?,?,?,?,?,?)"
    c1.execute(query2,my_data)
    messagebox.showinfo("success","Sucessfully inserted data")
    conn1.commit()
    conn1.close()
    

def show_record():
    conn3=sqlite3.connect("facebook.db")
    c3=conn3.cursor()
    query3="SELECT * FROM users"
    c3.execute(query3)
    alldata=c3.fetchall()
    record=""
    datas=""
    Label(root,text="Records Shows here.").grid(row=16,column=0)
    for record in alldata:
       datas+=str(record[0])+str(record[1])+"|"+str(record[2])+"|"+str(record[3])+"|"+str(record[4])+"|"+str(record[5])+"|"+str(record[6])+"\n"
    Label(root,text=datas).grid(row=17,column=0)  

def delete_record():
    num=delete.get()
    conn4=sqlite3.connect("facebook.db")
    c4=conn4.cursor()
    query4="DELETE FROM users WHERE Zipcode=?"
    c4.execute(query4,num)
    messagebox.showinfo("success","Record Deleted sucessfully")
    conn4.commit()
    conn4.close()
   
def update_data():
       fname=e1.get()
       lname=e2.get()
       age=e3.get()
       city=e4.get()
       zipcode=e5.get()
       password=e6.get()
       gender=var.get() 
       conn5=sqlite3.connect("facebook.db")
       c5=conn5.cursor()
       data=(fname,lname,age,city,password,gender,zipcode)
       query5="UPDATE users SET Firstname=?,Lastname=?,Age=?,City=?,Password=?,Gender=? WHERE  Zipcode=?"
       c5.execute(query5,data)
       messagebox.showinfo("Updated","update sucessfully")
       conn5.commit()
       conn5.close()

Button(root,text="Create Table",command=create_table,width=30).grid(row=9,column=1,pady=2)
Button(root,text="Add Data",command=Add_data,width=30).grid(row=10,column=1,pady=2)
Button(root,text="Show record",width=30,command=show_record).grid(row=11,column=1,pady=2)
Button(root,text="Update Record",width=30,command=update_data).grid(row=12,column=1,pady=2)
Button(root,text="Delete Record",width=30,command=delete_record).grid(row=13,column=1,pady=2)

root.mainloop()