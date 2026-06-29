price = int(input("Enter Amount of order : "))
coupan = str(input("Do you have coupan yes/no : "))

if coupan=="yes":
    valid = str(input("Enter your coupan code : "))
    if coupan=="yes" and valid=="ilove10":
        print("Congo you got 40% Discount !")
        print("Your Amount : ", price - price * (40/100))
    else:
        ("no discount")
elif coupan=="no":
    if price>=500:
        print("Congo you got 20% Discount !")
        print("Your Amount : ", price - price * (20/100))
    else:
        print("no discount")
else:
    print("No discount")