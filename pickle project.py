## pickle
import pickle
import os
class Bank:
    def __init__(self,a,n,br,b):
        self.ac=a
        self.name=n
        self.branch=br
        self.bal=b
    def show(self):
        print(f"{self.ac}\t {self.name}\t {self.branch}\t {self.bal}")
    def getname(self):
        return self.name
    def getbranch(self):
        return self.branch
    def getbal(self):
        return self.bal
    def cname(self,n):
        self.name=n
        print(f"new name is : {self.name}")
    def cbranch(self,b):
        self.branch=b
        print(f"new branch is : {self.branch}")
        
    def withdraw(self,amt):
        if(self.bal>amt):
            self.bal-=amt
            print(f"your account has been debited by Rs {amt} balance is {self.bal}")
        else:
            print("\n insufficient balance")
    def deposit(self,amt):
        if(amt>0):
            self.bal+=amt
            print(f"your account has been credited by Rs {amt} balance is {self.bal}")
        else:
            print("\n please deposit positive amount")

def CreateAc():
    print("Enter customer details")
    a=int(input("enter ac num : "))
    n=input("enter name : ")
    br=input("enter branch : ")
    bal=int(input("enter opening balance : "))
    ob=Bank(a,n,br,bal)
    f=open("bank.dat","ab")
    pickle.dump(ob,f)
    f.close()
    
def Display():
    a=int(input("enter ac num : "))
    f=open("bank.dat","rb")
    while(True):
        try:
            ob=pickle.load(f)
            if(ob.ac==a):
                ob.show()
        except:
            break
    f.close()

def Deposit():
    a=int(input("enter ac num : "))
    f=open("bank.dat","rb")
    t=open("temp.dat","ab")
    while(True):
        try:
            ob=pickle.load(f)
            if(ob.ac==a):
                amt=int(input("enter amount : "))
                ob.deposit(amt)
            pickle.dump(ob,t)
        except:
            break
    f.close()
    t.close()
    os.remove("bank.dat")
    os.rename("temp.dat","bank.dat")
    
def Withdraw():
    a=int(input("enter ac num : "))
    f=open("bank.dat","rb")
    t=open("temp.dat","ab")
    while(True):
        try:
            ob=pickle.load(f)
            if(ob.ac==a):
                amt=int(input("enter amount : "))
                ob.withdraw(amt)
            pickle.dump(ob,t)
        except:
            break
    f.close()
    t.close()
    os.remove("bank.dat")
    os.rename("temp.dat","bank.dat")

def ChangeDetail():
    a=int(input("enter ac num : "))
    f=open("bank.dat","rb")
    t=open("temp.dat","ab")
    while(True):
        try:
            ob=pickle.load(f)
            if(ob.ac==a):
                ch=int(input("name change : 1\n branch chnage :2 "))
                if(ch==1):
                    name=input("enter new name : ")
                    ob.cname(name)
                elif(ch==2):
                    branch=input("enter new branch : ")
                    ob.cbranch(branch)
                else:
                    print("no details changed")
            pickle.dump(ob,t)
        except:
            break
    f.close()
    t.close()
    os.remove("bank.dat")
    os.rename("temp.dat","bank.dat")

def menu():
    temp="y"
    while(temp=='y'):
        try:
            print("1. Create your account /n 2.Display your account /n 3.Deposit /n 4.Withdraw")
            choice=int(input("enter your choice:"))
            if(choice==1):
                CreateAc()
            elif(choice==2):
                Display()
            elif(choice==3):
                Deposit()
            elif(choice==4):
                whithdraw()
            else:
                print("incorrect password")
            temp=input("do you want to do more repititions")
        except:
            break
        
            
    
   









    






