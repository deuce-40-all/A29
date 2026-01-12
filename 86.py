#WAP take a str and remove duplicates, no typecasting
a='DEEPAK'
out=''
for i in a:
    if i not in out:
        out+=i
print(out)            
