num_one= int(input("Enter first score "))
num_two= int(input("Enter second score "))
num_three= int(input("Enter third score "))
average= ((num_one+num_two+num_three)/3)

if(average >= 90 and average <=100 ):
    print("A")
elif(average >= 80 and average < 90):
    print("B")
elif(average >= 70 and average < 80):
    print("C")
elif(average >= 60 and average < 70):
    print("D")
elif(avergae >= 0 and avergae < 60 ):
    print("F")
else:
    print("invalid")
