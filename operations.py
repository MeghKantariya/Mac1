#PERFORMING MATHEMATICAL OPERATIONS

First =input("Enter first number= ")
operator=input("Enter your operator (+,-,*,/)= ")
Second =input("Enter second number= ")

if operator == "+":
    print(int(First)+int(Second))

elif operator == "-":
    print(int(First)-int(Second))

elif operator == "*":
    print(int(First)*int(Second))

elif operator == "/":
    print(int(First)/int(Second))

else:
    print("Invalid Equation")
