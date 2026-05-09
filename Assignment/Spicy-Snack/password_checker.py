password = input("Enter password: ")
length = len(password)
if(length > 6 and length <= 10):
    print("Medium")
elif(length < 6):
    print("Weak")
elif(length > 10):
    print("Strong")
elif(length < 1):
    print("invalid")
else:
    print("error")
