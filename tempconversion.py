#temperature conversion
unit = input("is this temp in celsius or farhrenheit (C/F) : ")
temp = float(input("enter temperature = "))
if unit=="C":
    temp = round((9 * temp) / 5 + 32)
    print("the temperature in farhrenheit is",temp,"F")
elif unit=="F":
    temp = (temp -32) * 5 / 9 
    print("the temperature in celsius is",temp,"C")
else:
    print("invalid unit")