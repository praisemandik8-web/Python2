a = int(input("Enter first number "))
b = int(input("Enter second number "))
c= int(input("Enter third number"))

largest = a
if(b > a and b> c):
    largest = b
    print("largest is ", largest)
if(c > a and c > b):
    largest = c
    print("largest is ", largest)
else:
    print("largest is "largest)
