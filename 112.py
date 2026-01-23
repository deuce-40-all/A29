#WAP to print all the uppercase from the collection
def upper():
    a=input("Enter a string: ")
    out=''
    for i in a:
        if 'A'<=i<='Z':
            out+=i
    return out
print(upper())