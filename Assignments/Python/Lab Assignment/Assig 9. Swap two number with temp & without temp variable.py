#swap two number
a=int(input("enter first number (a):"))
b=int(input("enter second number (b):"))
print("before swaping: a=",a, "b=",b)
temp=a
a=b
b=temp
print("after swapping (with temp): a=",a, "b=",b)

#without temp variable
x=int(input("Enter first number (x):"))
y=int(input("Enter second number (y):"))
print("Before swaping: x=",x, "y=",y)
x,y=y,x
print("After swapping (without temp): x=",x, "y=",y)