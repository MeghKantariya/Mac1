#TO ADD THE NO.S ENTERED BY THE USER

total=0
number=int(input("Enter any no.(0 to quit) = "))
while number!=0:
    total+=number
    number=int(input("Enter any no.(0 to quit) = "))
else:
    print(f"The total is {total}")
