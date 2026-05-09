total_bill = int(input("Enter total bill "))
is_member = input("Enter member status(yes or no) ")

discount = 0.1*total_bill
discount_two = total_bill - discount

discount_three = 0.05*total_bill
discount_four = total_bill - discount_three

if(total_bill >= 1000 and is_member == "yes"):
    print("You have 10% discount")
    print("Bill after discount is: ", discount_two)

if(total_bill >= 1000 and is_member == "no"):
    print("You have 5% discount")
    print("Bill after discount is: ", discount_four)

else:
    print("No discount.")


