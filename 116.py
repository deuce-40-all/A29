#WAP to declare a function that would check for palindrome
def palin():
    num=int(input("Enter a number:"))
    temp=num #reverse the original number num.
    rev=0
    while temp>0:
        rev=rev*10+temp%10 #temp%10 extract the last digit of a number.
        temp//=10
    if rev==num:
        return (f"Yes the number {num} is palindrome number.")
    else:
        return (f"No, the number {num} is not a palindrome.")
    
print(palin())        