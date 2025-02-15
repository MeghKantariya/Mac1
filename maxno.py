#TO FIND THE MAX NUMBER IN THE LIST

number=input("Enter a list of no.s using comma: ")
list1=number.split(",")

#for i in list1:
  #  no=max(list1)
#print(f"The max no from the list is {no}")


                 #OR

for x in range(len(list1)):
    list1[x]=int(list1[x])

max_no=0
for i in list1:
    if i>max_no:
        max_no=i

print(f"The maximum number is {max_no}")

