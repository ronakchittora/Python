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


