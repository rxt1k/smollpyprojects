# shopping cart 
foods = []
prices = []
total = 0

while True:
    food = input("Enter a Food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter Price of {food} : "))
        foods.append(food)
        prices.append(price)
print("---Your cart---")

for food in foods:
    print(food,end=" || ")
for price in prices:
    total = total + price
print()
print(f"Your Total is {total}")