menu = {"pizza": 3.00,
        "soda":2.00,
        "burger":2.00,
        "coke":1.00,
        "chips":1.00,
        "fries":4.00,
        "popcorn":5.00}

cart = []
total = 0

print("~~~~~MENU~~~~~")
for key , value in menu.items():
    print(f"{key:10}: {value}")

print("~~~~~~~~~~~~~~~")

while True:
    food = input("select an item ( q to quit): ")
    if food.lower() == "q":
        break 
    elif menu.get(food) is not None:
        cart.append(food)
print("~~~YOUR CART~~~")
for food in cart: #total 
    total = total + menu.get(food)
    
    print(food,end =" || ")
print()
print("Your total amount is - ",total)