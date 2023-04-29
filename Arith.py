from tkinter import *

def add():
    n1=int(t1.get())
    n2=int(t2.get())
    ans=n1+n2
    lans.config(text="Addition is "+str(ans));

def sub():
    n1=int(t1.get())
    n2=int(t2.get())
    ans=n1-n2
    lans.config(text="Subtraction is "+str(ans));

def mult():
    n1=int(t1.get())
    n2=int(t2.get())
    ans=n1*n2
    lans.config(text="Multiplication is "+str(ans));

def div():
    n1=int(t1.get())
    n2=int(t2.get())
    ans=n1/n2
    lans.config(text="Division is "+str(ans));
      
   
frm=Tk();
frm.title("Aritmetic Operations");
frm.geometry('350x400');

l1=Label(frm,text="Enter Number 1",bg='#d5f5f4',fg="black",pady=10,width=15);
l1.grid(row=1,column=1)

t1=Entry(frm,width=20);
t1.grid(row=1,column=2);

l2=Label(frm,text="Enter Number 2",bg='#d5f5f4',fg="black",pady=10,width=15);
l2.grid(row=2,column=1)

t2=Entry(frm,width=20);
t2.grid(row=2,column=2);

b1=Button(frm,text="+",width=5,command=add);
b1.grid(row=3,column=0);

b2=Button(frm,text="-",width=5,command=sub);
b2.grid(row=3,column=1);

b3=Button(frm,text="*",width=5,command=mult);
b3.grid(row=3,column=2);

b4=Button(frm,text="/",width=5,command=div);
b4.grid(row=3,column=3);

lans=Label(frm)
lans.grid(row=4,column=0)

