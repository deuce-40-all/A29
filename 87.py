#WAP to compute the square of even numbers and cube of odd nos and store in set
out=set()
for i in range(1,11,1):
    if i%2==0:
        out.add(i*i) #(i**2)
    else:
        out.add(i*i*i) #(i**3)
print(out)
        