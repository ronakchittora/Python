"""
1. Generate a random number (1000,9999)
2. Ask for input
3. Check how many digits from input exist in actual number,
   create a list or set intersection, this is cows + bulls
4. Check if index of any digit from above list exists at same place in input
   and actual number, this is bulls
5. Display cows and bulls
6. Repeat until bulls == 4, Game Over then
"""

"""
from random import randint, sample

def cows_bulls(user_num,num):
    cows, bulls, total, pos = 0,0,0,-1
    for i in user_num:
        pos += 1
        if i in num:
            total += 1
            try:
                if num.index(i,pos) == pos:
                    bulls += 1
            except ValueError:
                pass  # do nothing!
    cows = total - bulls
    return cows, bulls
            

if __name__=="__main__":
    n = {'1','2','3','4','5','6','7','8','9'}
    n_o = {'0','1','2','3','4','5','6','7','8','9'}
    num = sample(n,1)
    n_o = n_o - set(num)
    num.extend(sample(n_o,3))
    print(num)
    cow = 0
    bull = 0
    while bull != 4:
        user_num = list(input("Enter a 4 digit number: "))
        cow, bull = cows_bulls(user_num,num)
        print("cows:",cow,"; bulls:",bull, sep=" ")

    print("Game Over")

"""

import random

def compare_numbers(number, user_guess):
    cowbull = [0,0] #cows, then bulls
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[1]+=1
        else:
            cowbull[0]+=1
    return cowbull

if __name__=="__main__":
    playing = True #gotta play the game
    number = str(random.randint(0,9999)) #random 4 digit number
    print(number)
    guesses = 0

    print("Let's play a game of Cowbull!") #explanation
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
    print("The game ends when you get 4 bulls!")
    print("Type exit at any prompt to exit.")

    while playing:
        user_guess = input("Give me your best guess!")
        if user_guess == "exit":
            break
        cowbullcount = compare_numbers(number,user_guess)
        guesses+=1

        print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

        if cowbullcount[1]==4:
            playing = False
            print("You win the game after " + str(guesses) + "! The number was "+str(number))
            break #redundant exit
        else:
            print("Your guess isn't quite right, try again.")

