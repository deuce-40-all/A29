a=['google.com','gmail.com','pro.html','Home.py','Yahoo.py']
#op=['com':['google','gmail'],'html':['pro'],'py':['home'],'in':['yahoo']]
out={}
for i in a:
    a=i.split('.')
    if a[1] not in out:
        out[a[1]]=[a[0]]
    else:
        out[a[1]]+=[a[0]]
print(out)        