#Write a Python program to perform ATM operations according to the following menu:
#1 → Deposit Money
#2 → Withdraw Money
#3 → Check Balance
#Conditions:
#Withdrawal amount should not exceed balance.
#Initial balance = ₹10000

b=10000
print("PLEASE PRESS 1 TO DEPOSIT MONEY.")
print("PLEASE PRESS 2 TO WITHDRAW MONEY.")
print("PLEASE PRESS 3 TO CHECK BALANCE.")
t=int(input("PLEASE ENTER YOUR CHOICE:: "))
if t==1:
    a=int(input("Please enter the amount to be depositted:  "))
    b=b+a
    print("The updated balance is:  ",b)
elif t==2:
    w=int(input("please enter the amount to be withdrawn: "))
    if w<=b:
        b=b-w
        print("The updated balance is:  ",b)
    else:
        print("INSUFFICIENT AMOUNT.....")
elif t==3:
    print("Current balance:  ",b)
else:
    print("INVALID CHOICE!!!!")
    
