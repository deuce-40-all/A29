#WAP to uppercase at even index
a=input("enter a string")
out=''
for i in a:
    if('A'<=i<='Z') and a:
        out+=i
print(out)  