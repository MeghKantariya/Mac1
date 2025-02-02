#PROGRAM FOR RANDOMLY SELECTING A PERSON TO PAY THE BILL

import random

name=input("Enter everybody's name using comma : ")

list=name.split(",")

selection=random.choice(list)
print(f"{selection} will pay the bill")
