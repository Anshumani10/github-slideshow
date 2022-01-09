from tkinter import *

root=Tk()
root.geometry("400x600")
root.title("calculator")
######frame

f1=Frame(root,height=100,width=400,bg="green")
f1.pack(side=TOP)

f2=Frame(root,height=500,width=400,bg="grey")
f2.pack(side=LEFT)

#####label
lb=Label(f1,font=("ALGERIAN",25),bg="yellow",text="calculator").grid()

########calculator design
op=" "
var=StringVar()
def btclick(num):
    global op
    op=op+str(num)
    var.set(op)
def btneq():
    global op
    ans=str(eval(op))
    var.set(ans)
    op=ans
def btnclr():
    global op
    op=" "
    var.set(op)

###entry
e=Entry(f2,font=("arial",20),textvariable=var,bg="steel blue",justify="right",bd=20).grid(row=0,columnspan=4)
###button

b1=Button(f2,font=("arial",16),text="1",command=lambda : btclick(1),bd=10,padx=20,pady=15,fg="black",bg="steel blue").grid(row=1,column=0)
b2=Button(f2,font=("arial",16),text="2",command=lambda : btclick(2),bd=10,padx=20,pady=15,fg="black",bg="steel blue").grid(row=1,column=1)
b3=Button(f2,font=("arial",16),text="3",command=lambda : btclick(3),bd=10,padx=20,pady=15,fg="black",bg="steel blue").grid(row=1,column=2)
bp=Button(f2,font=("arial",16),text="+",command=lambda : btclick('+'),bd=10,padx=20,pady=15,fg="black",bg="steel blue").grid(row=1,column=3)

b4=Button(f2,font=("arial",16),text="4",command=lambda : btclick(4),bd=10,padx=20,pady=15,fg="black",bg="steel blue").grid(row=2,column=0)
b5=Button(f2,font=("arial",16),text="5",command=lambda : btclick(5),bd=10,padx=20,pady=15,fg="black",bg="steel blue").grid(row=2,column=1)
b6=Button(f2,font=("arial",16),text="6",command=lambda : btclick(6),bd=10,padx=20,pady=15,fg="black",bg="steel blue").grid(row=2,column=2)
bs=Button(f2,font=("arial",16),text="-",command=lambda : btclick('-'),bd=10,padx=20,pady=15,fg="black",bg="steel blue").grid(row=2,column=3)

b7=Button(f2,font=("arial",16),text="7",command=lambda : btclick(7),bd=10,padx=20,pady=15,fg="black",bg="steel blue").grid(row=3,column=0)
b8=Button(f2,font=("arial",16),text="8",command=lambda : btclick(8),bd=10,padx=20,pady=15,fg="black",bg="steel blue").grid(row=3,column=1)
b9=Button(f2,font=("arial",16),text="9",command=lambda : btclick(9),bd=10,padx=20,pady=15,fg="black",bg="steel blue").grid(row=3,column=2)
bm=Button(f2,font=("arial",16),text="*",command=lambda : btclick('*'),bd=10,padx=20,pady=15,fg="black",bg="steel blue").grid(row=3,column=3)

bclr=Button(f2,font=("arial",16),text="c",command=lambda : btnclr(),bd=10,padx=20,pady=15,fg="black",bg="steel blue").grid(row=4,column=0)
b0=Button(f2,font=("arial",16),text="0",command=lambda : btclick(0),bd=10,padx=20,pady=15,fg="black",bg="steel blue").grid(row=4,column=1)
beq=Button(f2,font=("arial",16),text="=",command= lambda : btneq(),bd=10,padx=20,pady=15,fg="black",bg="steel blue").grid(row=4,column=2)
bd=Button(f2,font=("arial",16),text="/",command=lambda : btclick('/'),bd=10,padx=20,pady=15,fg="black",bg="steel blue").grid(row=4,column=3)

