from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox
import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-8NC23TP;'
                      'Database=dataproj;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
# cursor.execute("select * from student")
# for data in cursor:
#     print(data)

def insert():
    id=enter_id.get();
    first_name= enter_first_name.get();
    last_name = enter_last_name.get();
    address= enter_add.get();
    department = enter_dep.get();
    semester=enter_semester.get();
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-8NC23TP;'
                          'Database=dataproj;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute("select * from student")
    count=0
    for data in cursor:
        if id==str(data[0]):
            count=count+1
            messagebox.showinfo("Insert status", "record already exits");
            conn.close()
            break;
    if count!=1:
     if id=="" or first_name=="" or last_name=="" :
         messagebox.showinfo("Insert status", 'all fields are required')
     else:
         conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-8NC23TP;'
                              'Database=dataproj;'
                              'Trusted_Connection=yes;')
         cursor = conn.cursor()
         cursor.execute("insert into student values('"+str(id)+"','"+str(first_name)+"','"+str(last_name)+"','"+str(department)+"','"+str(address)+"','"+str(semester)+"')")
         conn.commit()
         messagebox.showinfo("insert status",'Inserted successfully')
         conn.close()


def delete():
    id = enter_id.get();
    first_name = enter_first_name.get();
    last_name = enter_last_name.get();
    address = enter_add.get();
    department = enter_dep.get();
    semester = enter_semester.get();
    if enter_id.get() == "":
         messagebox.showinfo("delete status", "id is must to delete")
    else:
         conn = pyodbc.connect('Driver={SQL Server};'
                               'Server=DESKTOP-8NC23TP;'
                               'Database=dataproj;'
                               'Trusted_Connection=yes;')
         cursor = conn.cursor()
         cursor.execute("delete from student where (student_id='"+ str(id) +"')")
         conn.commit()
         messagebox.showinfo("Delete status", 'Deleted successfully')
         conn.close()

def update():
    id = enter_id.get();
    first_name = enter_first_name.get();
    last_name = enter_last_name.get();
    address = enter_add.get();
    department = enter_dep.get();
    semester = enter_semester.get();
    if id=="" or first_name=="" or last_name=="" or address=="" or department=="" or semester=="":
        messagebox.showinfo("update status", "all fields are required")
    else:
     conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-8NC23TP;'
                          'Database=dataproj;'
                          'Trusted_Connection=yes;')
     cursor = conn.cursor()
     cursor.execute("UPDATE student SET first_name='"+str(first_name)+"',last_name='"+str(last_name)+"',department='"+str(department)+"',addres='"+str(address)+"',semester='"+str(semester)+"' where student_id='"+str(id)+"'")
     cursor.execute("commit")
     messagebox.showinfo("update status","updated successfully")
     conn.commit()
     conn.close()


def view_table():
   table=enter_Table_name.get();
   conn = pyodbc.connect('Driver={SQL Server};'
                         'Server=DESKTOP-8NC23TP;'
                         'Database=dataproj;'
                         'Trusted_Connection=yes;')
   cursor = conn.cursor()
   cursor.execute("Select * from  student")
   for data in cursor:
       trv.insert("",'end',values=(data[0],data[1],data[2],data[3],data[4],data[5]))
   conn.close()
# def list_tables:

def clear():
    id = enter_id.get();
    first_name = enter_first_name.get();
    last_name = enter_last_name.get();
    address = enter_add.get();
    department = enter_dep.get();
    semester = enter_semester.get();
    enter_id.delete(0,'end')
    enter_first_name.delete(0, 'end')
    enter_last_name.delete(0, 'end')
    enter_add.delete(0, 'end')
    enter_dep.delete(0, 'end')
    enter_semester.delete(0, 'end')
    for item in trv.get_children():
            trv.delete(item)
def Search():
    id=enter_id.get();
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-8NC23TP;'
                          'Database=dataproj;'
                          'Trusted_Connection=yes;')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM student WHERE (student_id='" + str(id) + "')")
    for data in cursor:
            trv.insert("", 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5]))
    conn.close()
root=Tk()
#root.geometry("800x800")
root.title("projectdatabase")


mainframe=Frame(root,width=770, height=990,relief=RIDGE,bg='cadet blue')
mainframe.grid()
# scroll=Scrollbar(mainframe)
# scroll.pack(side=RIGHT,fill=Y)
trv=ttk.Treeview(mainframe,selectmode=BROWSE)
trv.grid(row=2,column=0)
# scrollbar = Scrollbar(trv.column(7), orient=VERTICAL)
# scrollbar.grid(row=0, column=2, sticky=N+S)




trv["columns"]=["1","2","3","4","5","6"]
trv["show"]='headings'
trv.column("1",width=100,anchor='c')
trv.column("2",width=180,anchor='c')
trv.column("3",width=180,anchor='c')
trv.column("4",width=230,anchor='c')
trv.column("5",width=100,anchor='c')
trv.column("6",width=90,anchor='c')
trv.heading("1",text="Id")
trv.heading("2",text="First_Name")
trv.heading("3",text="last_Name")
trv.heading("4",text="Department")
trv.heading("5",text="Address")
trv.heading("6",text="Semester")


titleframe=Frame(mainframe,bd=7,width=770,height=70,relief=RIDGE)
titleframe.grid(row=0,column=0)


topframe=Frame(mainframe,bd=5,width=770,height=990,relief=RIDGE)
topframe.grid(row=1,column=0)

left = Label(topframe, text="STUDENT PORTAL ",bg='blue',fg='white')
left.pack()

leftframe=Frame(topframe,bd=5,width=770,height=300,relief=RIDGE)
leftframe.pack(side=LEFT)
# leftframe=Frame(leftframe,bd=5,width=600,height=180,padx=2,pady=4,relief=RIDGE)
# leftframe.pack(side=TOP,padx=0,pady=0)

rightframe=Frame(topframe,bd=5,width=100,height=300,padx=2,relief=RIDGE)
rightframe.pack(side=RIGHT)


labeltitle=Label(titleframe,font=('arial',25,'bold'),text="UNIVERSITY MANAGEMENT SYSTEM",bd=7,bg='white')
labeltitle.grid(row=0,column=0,padx=120)


id=Label(leftframe,text='Enter ID',font=('bold',10))
id.place(x=20,y=10)
enter_id=Entry()
enter_id.place(x=140,y=110)

first_name=Label(leftframe,text='Enter first name',font=('bold',10))
first_name.place(x=20,y=50)
enter_first_name=Entry()
enter_first_name.place(x=140,y=150)

last_name=Label(leftframe,text='Enter last name',font=('bold',10))
last_name.place(x=20,y=90)
enter_last_name=Entry()
enter_last_name.place(x=140,y=190)

department=Label(leftframe,text='Enter department',font=('bold',10))
department.place(x=20,y=130)
enter_dep=Entry()
enter_dep.place(x=140,y=230)

address=Label(leftframe,text='Enter address',font=('bold',10))
address.place(x=20,y=170)
enter_add=Entry()
enter_add.place(x=140,y=270)


semester=Label(leftframe,text='Enter semester',font=('bold',10))
semester.place(x=20,y=210)
enter_semester=Entry()
enter_semester.place(x=140,y=310)

Table_name=Label(leftframe,text='Table name',font=('bold',10))
Table_name.place(x=20,y=250)
enter_Table_name=Entry()
enter_Table_name.place(x=140,y=350)

insert=Button(rightframe,text="INSERT",font=("italic",8),bg="white",width=8,height=1,command=insert)
insert.place(x=8,y=5)

delete=Button(rightframe,text="DELETE",font=("italic",8),width=10,height=1,bg="white",command=delete)
delete.place(x=8,y=50)

view_table=Button(rightframe,text="VIEW TABLE",height=1,width=10,font=("italic",8),bg="white",command=view_table)
view_table.place(x=8,y=100)

Modify=Button(rightframe,text="UPDATE",height=1,width=10,font=("italic",8),bg="white",command=update)
Modify.place(x=8,y=150)

clear=Button(rightframe,text="CLEAR",height=1,width=10,font=("italic",8),bg="white",command=clear)
clear.place(x=8,y=200)

Search=Button(rightframe,text="SEARCH",height=1,width=10,font=("italic",8),bg="white",command=Search)
Search.place(x=8,y=250)

root.mainloop()

