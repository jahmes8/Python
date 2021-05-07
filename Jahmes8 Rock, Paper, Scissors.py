###################
#
# Jahmes8
#
# Program: Rock,Paper,Scissors.py
#
# Date: 05/05/21
#
# Description: A Game of Rock Paper Scissors
#
###################

# Import Statements

import random

# Function as Definitions

run=True
player=input("Welcome to Rock, Paper, Scissors! Press Any Button To Get Started... ")
playerScore=0
cpuScore=0
while True:
    player=input("Choose 'r' for Rock, 'p' for Paper, 's' for Scissors Or Bye to quit: ")
    choices=['r','p','s']
    cpu=random.choice(choices)

    if player==cpu:
        print("Tie")

    elif(player=='p' and cpu=='r'):
        print("Player Wins")
        playerScore+=1

    elif(player=='s' and cpu=='p'):
        print("Player Wins")
        playerScore+=1

    elif(cpu=='r' and player=='s'):
        print("CPU Wins")
        cpuScore+=1

    elif(cpu=='p' and player=='r'):
        print("CPU Wins")
        cpuScore+=1

    elif(cpu=='s' and player=='p'):
        print("CPU Wins")
        cpuScore+=1

    elif(player=='bye'):
        break
    elif(player=='Bye'):
        break
    elif(player=='BYE'):
        break

    else:
        print("Error: Wrong Input!")

    print("Score: Player " + str(playerScore) + " CPU " + str(cpuScore))
print("FINAL SCORE: Player " + str(playerScore) + " CPU " + str(cpuScore))


