father_age = int(input("Enter father's age(1-80):'"))
son_age = int(input("Enter sons's age(1-80)"))
years = father_age - (2*son_age)
if(father_age and son_age >= 1 and father_age and son_age <= 80 and years > 0):
    print("A father wwas twice his son's age ", years, " years ago.")
elif(father_age and son_age >= 1 and father_age and son_age <= 80 and years < 0):
    print("A father will be twice his son's age in: ", years, " years.")
else: 
    print("Error, follow the instructuons.")
    
