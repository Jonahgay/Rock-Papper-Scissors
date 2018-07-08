from random import choice
from time import sleep

'''

'''

RPC_Choices = ["Rock","Paper","Scissors"]
Player_Score = 0
Computer_Score = 0
Round = 1
#Player Choice at Line 49.


doRPC=input("Would you like to play Rock Paper Scissors with a bot ?: \n")

if doRPC.upper() == "YES":
    sleep(0.5)
    print("Alright Lets Start ! (...)")
    sleep(2)
elif doRPC.upper()=="NO":
    sureRPC = input("Are you Sure ? \n")
    if sureRPC.upper() == "YES":
        sleep(0.5)
        print("Ok then Shutting down ...")
        sleep(2)
        quit()
    elif sureRPC.upper()=="NO":
        sleep(0.5)
        print("Lets play the game then...")
        sleep(2)
    else:
        print("[Consol] ERROR only say Yes or No on these types of questions")
        exit()
else:
    print("[Consol] ERROR only say Yes or No on these types of questions")
    exit()

del doRPC
try:
    del sureRPC
except NameError:
    pass
Player = input("Please pick a Username: ")

# vvvvvvv Game Starts from here vvvvvvv
while True:
    sleep(0.5)
    print("Round "+str(Round)+", GO!")
    Player_Choice = input("Rock, paper or scissors ?\n")
    Computer_Choice = choice(RPC_Choices)
    sleep(0.5)
    if (Player_Choice.upper() ==  "ROCK" and Computer_Choice.upper() == "PAPER") or (Player_Choice.upper() == "PAPER" and Computer_Choice.upper() == "SCISSORS") or (Player_Choice.upper() == "SCISSORS" and Computer_Choice.upper() == "ROCK"):
        Computer_Score += 1
        print(Player+" "+str(Player_Score)+" -(Computer Won)- "+str(Computer_Score)+" Computer"+"\n")
    elif (Player_Choice.upper() ==  "ROCK" and Computer_Choice.upper() == "SCISSORS") or (Player_Choice.upper() == "PAPER" and Computer_Choice.upper() == "ROCK") or (Player_Choice.upper() == "SCISSORS" and Computer_Choice.upper() == "PAPER"):
        Player_Score += 1
        print(Player+" "+str(Player_Score)+" -(You Won)- "+str(Computer_Score)+" Computer"+"\n")
    elif Player_Choice.upper() == Computer_Choice.upper():
        print(Player+" "+str(Player_Score)+" -(its a Tie)- "+str(Computer_Score)+" Computer"+"\n")
    Round +=1
    
    if Round == 15:
        if Player_Score > Computer_Score:
            print("---------You WIN !!---------")
        elif Player_Score < Computer_Score:
            print("---------You LOSE !!---------")
        elif Player_Score == Computer_Score:
            print("---------Its a Tie !!---------")
        break