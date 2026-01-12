#WAP print fact of a number
a=int(input("enter an integer"))
fact=1
for i in range(1,a+1,1):
    fact*=i
print(fact)    