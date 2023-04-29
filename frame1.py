from tkinter import *

def greet():
    l2.config(text="Hello Students")
   

frm=Tk();
frm.title("First Frame");
frm.geometry('350x350');

l1=Label(frm,text="Akshay",bg='#d5f5f4',fg="black",pady=20,width=30);
l1.grid(row=0,column=0)

l2=Label(frm,text="Pune",bg='#d5f5f4',fg="black",pady=20,width=20);
l2.grid(row=0,column=1)

t1=Entry(frm);
t1.grid(row=1,column=0);
b1=Button(frm,text="Click",width=15,command=greet).grid(row=2,column=0)




