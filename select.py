import os
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox



root=Tk()
root.geometry("300x300")
root.title("projectdatabase")
root.configure(bg="blue")

def student():
    root.destroy();
    os.system(' python student.py')
def faculty():
    root.destroy();
    os.system(' python faculty.py')

def staff():
    root.destroy();
    os.system(' python staff.py')


labeltitle=Label(root,font=('arial',13,'bold'),text="SELECT REQUIRED DATABASE",bd=7,fg='white',bg='blue')
labeltitle.place(x=20,y=0)


B1=Button(root,text="STUDENT DATABASE",height=3,width=40,font=("italic",8),bg="white",command=student)
B1.place(x=30,y=40)
B1.configure(bg='yellow')

B2=Button(root,text="FACULTY DATABASE",height=3,width=40,font=("italic",8),bg="white",command=faculty)
B2.place(x=30,y=120)
B2.configure(bg='yellow')

B3=Button(root,text="STAFF DATABASE",height=3,width=40,font=("italic",8),bg="white",command=staff)
B3.place(x=30,y=210)
B3.configure(bg='yellow')

root.mainloop()