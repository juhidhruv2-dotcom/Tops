#Program to calculate sum of three integers
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a==b or b==c or a==c:
    total=0
else:
    total=a+b+c
print("result:",total)