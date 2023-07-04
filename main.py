from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
def Insert():
   id = id_entry.get()
   name = name_entry.get()
   phone = phone_entry.get()
  
   if(id == "" or name == "" or phone == ""):
       MessageBox.showinfo("ALERT", "There are some fields that are missing!")
   else:
       con = mysql.connect(host="bqwpp00amvqwhp9fnu3q-mysql.services.clever-cloud.com", user="ufddvczlfkrnwbem", password="LRSTfIMzj0BRNoDtKzM1", database="bqwpp00amvqwhp9fnu3q")
       cursor = con.cursor()
       cursor.execute("insert into Person values('" + id +"', '"+ name +"', '" + phone +"')")
       cursor.execute("commit")
  
       MessageBox.showinfo("Status", "Inserted!")
       con.close();

def Update():
   id = id_entry.get()
   name = name_entry.get()
   phone = phone_entry.get()
  
   if(name == "" or phone == ""):
       MessageBox.showinfo("ALERT", "There are some fields that are missing!")
   else:
       con = mysql.connect(host="bqwpp00amvqwhp9fnu3q-mysql.services.clever-cloud.com", user="ufddvczlfkrnwbem", password="LRSTfIMzj0BRNoDtKzM1", database="bqwpp00amvqwhp9fnu3q")
       cursor = con.cursor()
       cursor.execute("update Person set name = '"+ name +"', phone='"+ phone +"' where id ='"+ id +"'")
       cursor.execute("commit");
  
       MessageBox.showinfo("Status", "Updated!")
       con.close();

def Del():
  
   if(id_entry.get() == ""):
       MessageBox.showinfo("ALERT", "Please enter ID to delete row")
   else:
       con = mysql.connect(host="bqwpp00amvqwhp9fnu3q-mysql.services.clever-cloud.com", user="ufddvczlfkrnwbem", password="LRSTfIMzj0BRNoDtKzM1", database="bqwpp00amvqwhp9fnu3q")
       cursor = con.cursor()
       cursor.execute("delete from Person where id='"+ id_entry.get() +"'")
       cursor.execute("commit");
  
       id_entry.delete(0, 'end')
       name_entry.delete(0, 'end')
       phone_entry.delete(0, 'end')
  
       MessageBox.showinfo("Status", "Deleted!")
       con.close();

def Select():
  
   if(id_entry.get() == ""):
       MessageBox.showinfo("ALERT","ID is required to select row!")
   else:
       con = mysql.connect(host="bqwpp00amvqwhp9fnu3q-mysql.services.clever-cloud.com", user="ufddvczlfkrnwbem", password="LRSTfIMzj0BRNoDtKzM1", database="bqwpp00amvqwhp9fnu3q")
       cursor = con.cursor()
       cursor.execute("select * from Person where id= '" + id_entry.get() +"'")
       rows = cursor.fetchall()
  
       for row in rows:
           name_entry.insert(0, row[1])
           phone_entry.insert(0, row[2])
  
       con.close();
root = Tk()
root.geometry("500x300")
root.title("Simple CRUD _ Kodland Python Pro Test _ PG")
id = Label(root, text="ID:", font=("arial 12"))
id.place(x=50, y=30)
id_entry = Entry(root, font=("arial 12"))
id_entry.place(x=150, y=30)
  
name = Label(root, text="Name:", font=("arial 12"))
name.place(x=50, y=80)
name_entry = Entry(root, font=("arial 12"))
name_entry.place(x=150, y=80)
  
phone = Label(root, text="Phone:", font=("arial 12"))
phone.place(x=50, y=130)
phone_entry= Entry(root, font=("arial 12"))
phone_entry.place(x=150, y=130)
  
btnInsert = Button(root, text="Insert", command=Insert, font=("arial 12")).place(x=100, y=190)
btnDelete = Button(root, text="Delete", command=Del, font=("arial 12")).place(x=200, y=190)
btnUpdate = Button(root, text="Update", command=Update, font=("arial 12")).place(x=320, y=190)
btnSelect= Button(root, text="Select", command=Select, font=("arial 12")).place(x=200, y=240)
  
root.mainloop()