"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:
1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
""""

a = int(input("Enter a number: "))
if a%2 == 0 and a%4 != 0:
    print("It's even")
elif a%4 == 0:
    print("It's divisible by 4")
else:
    print("It's odd")

b = int(input("Hey!, Enter another number: "))
c = int(input("Hey again!, Enter one more number: "))
if b%c == 0:
    print("It's fully divisible")
else:
    print("You're just stupid")
