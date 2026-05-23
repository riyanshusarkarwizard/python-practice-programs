#Write a Python program for food ordering according to the following menu:
#Burger → ₹120
#Pizza → ₹250
#Momos → ₹100
#Calculate total bill according to quantity entered.

print("MENU")
print("1. BURGER→ ₹120")
print("2. PIZZA→ ₹250")
print("3.MOMOS→ ₹100")
i=int(input("PLEASE ENTER THE ITEM NUMBER::  "))
q=int(input("PLEASE ENTER THE QUANTITY OF THE ITEM::  "))
if i==1:
    t=120*q
elif i==2:
    t=250*q
elif i==3:
    t=100*q
else:
    t=0
    print("invalid choice....")
print("total bill:   ",t)
