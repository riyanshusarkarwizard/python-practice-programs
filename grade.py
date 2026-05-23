#Write a Python program to input marks of 3 subjects and calculate total marks, percentage, and grade according to the following conditions:
#Percentage ≥ 90 → Grade A
#Percentage ≥ 75 and < 90 → Grade B
#Percentage ≥ 50 and < 75 → Grade C
#Percentage < 50 → Fail.

name=input("enter the name of the student:   ")
m1=float(input("please enter the marks of the first subject"))
m2=float(input("please enter the marks of the second subject"))
m3=float(input("please enter the marks of the third subject"))
t=m1+m2+m3
p=t/3
if p>90:
    print("the name of the student is:", name)
    print("the total marks obtained by the student is:", t)
    print("the total percentage obtained by the student is:", p)
    print(name,"obtained GRADE A")
elif p>=75 and p<90:
    print("the name of the student is:", name)
    print("the total marks obtained by the student is:", t)
    print("the total percentage obtained by the student is:", p)
    print(name,"obtained GRADE B")
elif p>=50 and p<75:
    print("the name of the student is:", name)
    print("the total marks obtained by the student is:", t)
    print("the total percentage obtained by the student is:", p)
    print(name,"obtained GRADE C")
else:
    print("the name of the student is:", name)
    print("the total marks obtained by the student is:", t)
    print("the total percentage obtained by the student is:", p)
    print(name,"HAS FAILED THE EXAMINATION")



    
