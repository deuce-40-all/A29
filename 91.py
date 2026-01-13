#WAP to perform
a='abcdabab'
op='a1b2c3d4a1b2a1b2'
out=''
for i in a:
    out+=i+(str(ord(i)-96))
print(out)  