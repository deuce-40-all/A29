#WAP 

a = 'Python is very easy'.split()
b={}
for i in range(1,len(a)):
    if i%2==0:
        for j in a[i]:
            b[i]=a[i][::-1]+str(len(a[i]))
    else:
        b[i]=a[i][::-1]
print(b)