#WAP
a='aBcDefg'
op='abcdefg'
out=''
for i in a:
    if 'A'<=i<='Z':
        out+=chr(ord(i)+32)
    else:
        out+=i
print(out)        
    