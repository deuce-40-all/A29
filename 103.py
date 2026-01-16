#WAP 
a=['how','are','you','all']
op=[1,2,2,1]
out=[]
# for i in range(0,len(a)):
#     c=0
#     for j in range(0,len(a[i])):
#         if(a[i][j] in 'aeiou'):
#             c+=1
#     out+=[c]  
# print(out)  

for i in a:
    c=0
    for j in i:
        if j in 'AEIOUaeiou':
            c+=1
    out+=[c]
print(out)            


