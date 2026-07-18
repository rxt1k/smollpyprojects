def add(*args):
    return sum(args)
total = []

while True:
    x = input("enter a number to add to press q to quit : ")
    if x=="q" or x=="Q":
        break
    else:
        total.append(int(x))
        
   
result = add(*total)
print("total : ",result)
