#FINDING BMI(Body Mass Index) OF A PERSON

weight=input("Enter your Weight in kg? ")
height=input("Enter your Height in m? ")

BMI=int(weight) / float(height)**2
x=int(BMI)

print("Your BMI is "+ str(x))
