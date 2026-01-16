#WAP sum of only ints in a list
a=[10,'hello',3+5j,321]
op=[1,6]
out=[]
for i in a:
    
    if type(i)==int:
        sum=0
        for j in str(i): # this for you to decode for j in str(i) vs len(str(i))
            sum+=int(j)
            
        out+=[sum]
print(out)        