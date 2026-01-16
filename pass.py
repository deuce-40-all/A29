#WAP to demostrate the use of pass statement
for i in range(1,11):
    if i%2==0:
        pass
    else:
        print(i)
#Explanation: In the above code, when the condition i%2==0 is true (i.e., when i is even), 
# the pass statement is executed, which means "do nothing" and 
# the loop continues to the next iteration without any action. 
# When i is odd, it prints the value of i.        