letter = input("Enter a letter")
if(letter == "a" or letter == "e" or letter == "i" or letter == 0 or letter == "u"):
    print("Vowel")
elif(type(letter) != str):
    print("Invalid data type, enter a letter.")
else:
    print("Consonant") 
