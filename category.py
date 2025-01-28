#PROGRAM TO CHECK YOUR BMI CATEGORY

weight=int(input("Enter your weight in kg = "))
height=float(input("Enter your height in m = "))
print()

BMI=round(weight/height**2)

if BMI<18:
    print(f"Your BMI is {BMI} , You are in under-weight category")
elif BMI<=25:
    print(f"Your BMI is {BMI} ,You are in normal category")
elif BMI<=30:
    print(f"Your BMI is {BMI} ,You are in over-weight category")
else:
     print(f"Your BMI is {BMI} ,You are in obese category")

print()
print("Thank You for using our BMI calculator")
