#WAP
a='abcstqz'
op='abcdefg'
out=''
for i in a:
    if i!='z':
        out+=chr(ord(i)+1)
    elif i=='z':
        out+='a'
print(out)   