#WAP
a='collectionc'
op={'c':3,'o':2,'l':2}
out={}
for i in a:
    if a.count(i)>=2:
        out[i]=a.count(i)
print(out)