# lbs to kg converter
print("Welcome to weight converter")
print("what you want to do ?")
print("choose 1 to convert lbs to kg \n choose 2 to convert kg to lbs")
x = int(input("choose 1 or 2"))

if x == 1:
    print("LBS to KG")
    lbs = float(input(" enter lbs ="))
    kg = lbs / 2.20462
    print(kg, "kg")

elif x == 2:
    print("KG to LBS")
    kg = float(input("enter kg ="))
    lbs = kg * 2.20462
    print(lbs, "lbs")

else:
    print("choose right option")