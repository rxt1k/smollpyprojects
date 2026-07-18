# gst adder

def gst(amount,gt = 18):
    gs = amount * (gt/100)
    return amount + gs

amount = int(input("enter your amount = "))
print(gst(amount))
