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
