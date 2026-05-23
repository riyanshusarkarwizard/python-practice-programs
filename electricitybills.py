#Write a Python program to calculate electricity bill according to the following conditions:
#First 100 units → ₹5 per unit
#Next 100 units → ₹7 per unit
#Above 200 units → ₹10 per unit

u=float(input("enter the units used by the customer:   "))
if u<=100:
    t=u*5
    print("the total bill is= ",t)
elif u>100 and u<=200:
    t=100*5+(u-100)*7
    print("the total bill is=  ",t)
else:
    t=100*5+100*7+(u-200)*10
    print("the total bill is=  ",t)
