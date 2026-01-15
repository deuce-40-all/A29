#Q
a=int(input("enter an integer"))
c=0
while a>0:
    b=a%10
    if c<b:
        print("yes in order")
    a//=10    
    break