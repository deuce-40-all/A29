#WAP to take a string which is mix up of uppercase, lowercase, 
# cond1: if no of upcase are more than number of lowcase, concate upper with lower 
# otherwise print product of uppercases with length of lowercases
a='QuickBrownFox'
out1=''
out2=''
for i in a:
    if 'a'<=i<='z':
        out1+=i
    else:
        out2+=i
if len(out1)>len(out2):
    print(out2*len(out1))      #if str * a number it will repeat the str that many times.
else:
    print(out2+out1)