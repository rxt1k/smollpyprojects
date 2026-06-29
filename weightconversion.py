# lbs to kg converter
print("Welcome to weight converter")
print("what you want to do ?")
print("choose 1 to convert lbs to kg \n choose 2 to convert kg to lbs")
x = int(input("choose 1 or 2"))
if x==1:
    print("LBS to KG")
    lbs = int(input(" enter lbs ="))
    print(lbs/2.2,"kg")
elif x==2:
    print("kg to LBS")
    kg = int(input("enter kg ="))
    print(kg * 2 / 10)
else:
    print("choose right option")
