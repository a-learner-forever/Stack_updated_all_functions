st=[]



def push():
    i=int(input("enter the value to be added:"))
    st.append(i)
    takeChoice()
    

def pull():
    if len(st)>0:
        st.pop()
        print("Value popped")
        show()
    else:
        print("Stack is empty!!")

def show():
    print("The stack is: ")
    j=len(st)-1
    while j>=0:
        print("|",end="")
        print(st[j], end="|")
        print()
        print(" ---")
        j-=1
    takeChoice()

def clean():
    print("Are you sure, you want to clear the stack (y/n) : ")
    ans=input()
    if ans=="y":
        st.clear()
        show()
        
    else:
        print("Okay we won't clear the stack!!")
        takeChoice()

def choose(ch):
    if ch==1:
        push()
    if ch==2:
        pull()
    if ch==3:
        show()
    if ch==4:
        clean()
    if ch==5:
        print("Good Bye !!")
        exit()

    else:
        print("Invalid Input!!!")

def takeChoice():
    ch=int(input("Enter the choice please: push:1, pull:2, show:3, clearStack:4 exit:5 -  "))
    choose(ch)


print("*****Stack Implementation*****")

while True:

    takeChoice()
    
