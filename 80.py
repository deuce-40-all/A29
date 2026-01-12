#WAP to extract all the uppercase from a given string
a=input("enter a string")
out=''
for i in a:
    if('A'<=i<='Z'):
        out+=i
print(out)        
    