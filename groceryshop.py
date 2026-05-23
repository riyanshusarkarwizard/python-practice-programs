#Write a Python program to calculate grocery bill according to the following conditions:
#If total amount is greater than ₹2000, give 10% discount.
#Otherwise, no discount.

i1=float(input("enter the price of item1"))
i2=float(input("enter the price of item2"))
i3=float(input("enter the price of item3"))
t=i1+i2+i3
if t>2000:
    p=10/100*t
else:
    p=0
d=t-p
print("price of item1:  ",i1)
print("price of item2:  ",i2)
print("price of item3:  ",i3)
print("total price before discount:  ",t)
print("discount:  ",p)
print(" final amount to be paid::  ",d)
