rsp = ["paper", "scissors", "rock"]

in1 = ''
in2 = ''

replay1 = 'y'

win_fl = 0

while ((in1==in2) or win_fl == 2) and replay1 == 'y':
    if replay1 == 'y':
        in1 = input("Player 1: ")
        in2 = input("Player 2: ")
        
        if in1 not in rsp or in2 not in rsp:
            win_fl = 2
            replay1 = input("Invalid input! You have not entered rock, paper or scissors, do you want to try again? (y/n) ")
        elif (rsp.index(in1) > rsp.index(in2) and rsp.index(in1) - rsp.index(in2) != 2) or rsp.index(in1) - rsp.index(in2) == -2:
            win_fl = 1
            print("Player 1 won")
            print("Thanks for playing")
            replay1 = 'n'
        elif in1 != in2:
            win_fl = 1
            print("Player 2 won")
            print("Thanks for playing")
            replay1 = 'n'
        else:
            win_fl = 0
            replay1 = input("Draw!! Play again ? ")
    
"""
in1 = ''
in2 = ''
in3 = ''

replay1 = 'y'
replay2 = 'y'

while ((in1!=in2 and in2!=in3 and in1!=in3) or (in1==in2==in3)) and replay1 == 'y':
    if replay1 == 'y':
        in1 = input("Player 1: ")
        in2 = input("Player 2: ")
        in3 = input("Player 3: ")

        if rsp.index(in1)==rsp.index(in2) and rsp.index(in1)!=rsp.index(in3):
            if (rsp.index(in3)==0) and rsp.index(in1)!=1:
                print("Player 3 won")
            else:
                while rsp.index(in1)==rsp.index(in2) and replay2=='y':
                    in1 = input("Player 1: ")
                    in2 = input("Player 2: ")
                    if in1==in2:
                        replay2 = input("Draw!! Play again ? ")
                    elif rsp.index(in1) > rsp.index(in2) and rsp.index(in2)-rsp.index(in1)==1:
                        print("Player 1 won")
                    else:
                        print("Player 2 won")

        elif rsp.index(in2)==rsp.index(in3) and rsp.index(in2)!=rsp.index(in1):
            if (rsp.index(in1)==0 or rsp.index(in1)==1) and rsp.index(in2)!=1:
                print("Player 1 won")
            else:
                while rsp.index(in2)==rsp.index(in3) and replay2=='y':
                    in2 = input("Player 2: ")
                    in3 = input("Player 3: ")
                    if in3==in2:
                        replay2 = input("Draw!! Play again ? ")
                    elif rsp.index(in2) > rsp.index(in3) and rsp.index(in3) != 0:
                        print("Player 2 won")
                    else:
                        print("Player 3 won")

        elif rsp.index(in1)==rsp.index(in3) and rsp.index(in2)!=rsp.index(in1):
            if (rsp.index(in2)==0 or rsp.index(in2)==1) and rsp.index(in3)!=1:
                print("Player 2 won")
            else:
                while rsp.index(in1)==rsp.index(in3) and replay2=='y':
                    in1 = input("Player 1: ")
                    in3 = input("Player 3: ")
                    if in1==in3:
                        replay2 = input("Draw!! Play again ? ")
                    elif rsp.index(in1) > rsp.index(in3) and rsp.index(in3) != 0:
                        print("Player 1 won")
                    else:
                        print("Player 3 won")
        else:
            replay1 = input("Play again? ")

    else:
        replay1 = input("Nobody won, play again? ")

print("Thanks for playing")

"""
#####Pseudo-Code#####
"""
in1 = input("Player 1: ")
in2 = input("Player 2: ")
in3 = input("Player 3: ")

rock, scissors, paper
2, 1, 0
rock > scissors 2>1
scissors > paper 1>0
paper > rock 0>2

play again = Y

while none equal or all equal and play again = Y
    type something to play again
if play again? - Y
    in1 = input("Player 1: ")
    in2 = input("Player 2: ")
    in3 = input("Player 3: ")

    if index pl 1==index pl 2 and index pl 1!=index pl 3
        if index pl 3 == 0 or 1 and index pl 1!=1
            winner 3
        else
            while index pl 1==index pl 2
                print - 1 and 2 play again
                in1 = input("Player 1: ")
                in2 = input("Player 2: ")
                if index pl 1 > index pl 2 and index pl 2 != 0
                    winner 1
                else
                    winner 2
                    
    elif index pl 2==index pl 3 and index pl 2!=index pl 1
        if index pl 1 == 0 or 1 and index pl 2!=1
            winner 1
        else
            while index pl 2==index pl 3
                print - 2 and 3 play again
                in2 = input("Player 2: ")
                in3 = input("Player 3: ")
                if index pl 2 > index pl 3 and index pl 3!= 0
                    winner 2
                else
                    winner 3
    elif index pl 1==index pl 3 and index pl 1!=index pl 2
        if index pl 2 == 0 or 1 and index pl 3!=1
            winner 2
        else
            while index pl 1==index pl 3
                print - 1 and 3 play again
                in1 = input("Player 1: ")
                in3 = input("Player 3: ")
                if index pl 1 > index pl 3 and index pl 3!= 0
                    winner 1
                else
                    winner 3
else
    Nobody won, play again? - ?
"""
