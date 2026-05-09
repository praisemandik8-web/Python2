x = int(input("Enter number "))
y = int(input("Enter second number "))

if(x > 0 and y > 0 ):
    print("Q1")
elif(x < 0 and y > 0 ):
    print("Q2")
elif(x < 0 and y < 0 ):
    print("Q3")
elif(x > 0 and y < 0 ):
    print("Q4")
elif(x == 0 and y== 0):
    print("Q5")
elif(x != 0 and y==0):
    print("X-axis")
elif(x == 0 and y != 0):
    print("Y-axis")
elif(x == 0 and y == 0):
    print("Origin")
else:
    print("Invalid")
