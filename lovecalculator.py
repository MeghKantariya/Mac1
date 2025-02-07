#CODING A LOVE CALCULATOR
boy=input("What is your name? ")
girl=input("What is your partner's name? ")

x=boy.lower()
y=girl.lower()

a=x.count("t")
b=y.count("t")
c=x.count("r")
d=y.count("r")
e=x.count("u")
f=y.count("u")
g=x.count("e")
h=y.count("e")
i=x.count("l")
j=y.count("l")
k=x.count("o")
l=y.count("o")
m=x.count("v")
n=y.count("v")
o=x.count("e")
p=y.count("e")

true=a+b+c+d+e+f+g+h
love=i+j+k+l+m+n+o+p
tru_lob="Your love score is"+" "+str(true)+str(love)
print(str(tru_lob))