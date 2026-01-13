a=['google.com','gmail.com','pro.html','Home.py','Yahoo.py']
op=['com','com','html','py','py']
out={}
for i in a:
    a=i.split('.')
    out[a[0]]=a[1]
print(out)  