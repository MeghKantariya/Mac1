#CALCULATE THE AVG HEIGHT FROM THE LIST

height=input("enter everyone's height using comma(,) = ")

list1=height.split(',')
no=len(list1)

for i in range(no):
    list1[i]=int(list1[i])

total=0
for x in list1:
    total+=x

avg=total/no
print(round(avg))
