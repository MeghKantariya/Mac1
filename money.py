#PROGRAM FOR HIDING USER'S MONEY IN THE MATRIX

row1=[1,1,1]
row2=[1,1,1]
row3=[1,1,1]

final_row=[row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}")

position=input("Enter the position to hide money(row,column) = ")

row=int(position[0])
column=int(position[1])

row_selected=final_row[row-1]
row_selected[column-1]='x'

print(f"{row1}\n{row2}\n{row3}")

