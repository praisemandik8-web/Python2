age = int(input("Enter age "))
if(age < 5):
    print("Ticket is free")
elif(age >= 5 and age <=12):
    print("Ticket is $5")
elif(age >= 13 and age <= 64):
    print("Ticket is $12")
elif(age >= 65):
    print("Ticket price is $8")
else:
    print("Invalid age")
