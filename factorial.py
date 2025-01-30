#FIND FACTORIAL OF ANY NUMBER

no=int(input("Enter any number you find its factorial : "))
fact=1
for i in range(1,no+1):
    fact*=i
    i+=1
print(f"The factorial of {no} is {fact}")