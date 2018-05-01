from datetime import datetime

name = input("Your name: ")
age = int(input("Your  age: "))

c_month = datetime.now().strftime('%B')

q_str = "Did you born in or before " + c_month + "? (Y/N) "

birthday_fl = input(q_str)
c_yr = datetime.now().year

year2 = abs(c_yr + 100 - age)

n = int(input("Enter a num: "))

for i in range(0,n):
    if birthday_fl.lower() == 'y' and year2 > c_yr:
        print("You will turn 100 in year:", year2)
    elif birthday_fl.lower() == 'n' and year2-1 > c_yr:
        print("You will turn 100 in year:", year2-1)
    elif age >= 100:
        print("You already turned 100 in year: ", year2)
