"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
2. Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""

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
