"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:
1. Keep the game going until the user types “exit”
2. Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

from random import randint

num_guess = randint(1,9)
print(num_guess)

count_guesses = 0

while True:
    usr_in = input("Enter a number (1-9): ")
    count_guesses += 1

    if usr_in == 'exit':
        print("Number of guesses: ", count_guesses-1)
        break
    elif int(usr_in) == num_guess:
        print("exactly right")
        print("Number of guesses: ", count_guesses)
        break
    elif int(usr_in) > num_guess:
        print("Too high")
        continue
    else:
        print("Too low")
        continue


