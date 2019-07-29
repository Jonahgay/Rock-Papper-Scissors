from random import choice
from time import sleep


RPC_Choices = ["ROCK","PAPER","SCISSORS"]
Player_Score = 0
Computer_Score = 0
Round = 1


doRPC=input("Would you like to play Rock Paper Scissors with a bot ?: \n")

def Error_Sure():
    print("[Consol] ERROR only awnser with Yes or No on these types of questions")
    exit()

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
        Error_Sure()
else:
    Error_Sure()

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
    if (Player_Choice.upper() ==  RPC_Choices[0] and Computer_Choice.upper() == RPC_Choices[1]) or (Player_Choice.upper() == RPC_Choices[1] and Computer_Choice.upper() == RPC_Choices[2]) or (Player_Choice.upper() == RPC_Choices[2] and Computer_Choice.upper() == RPC_Choices[0]):
        Computer_Score += 1
        print(Player+" "+str(Player_Score)+" -(Computer Won)- "+str(Computer_Score)+" Computer"+"\n")
    elif (Player_Choice.upper() ==  RPC_Choices[0] and Computer_Choice.upper() == RPC_Choices[2]) or (Player_Choice.upper() == RPC_Choices[1] and Computer_Choice.upper() == RPC_Choices[0]) or (Player_Choice.upper() == RPC_Choices[2] and Computer_Choice.upper() == RPC_Choices[1]):
        Player_Score += 1
        print(Player+" "+str(Player_Score)+" -(You Won)- "+str(Computer_Score)+" Computer"+"\n")
    elif Player_Choice.upper() == Computer_Choice.upper():
        print(Player+" "+str(Player_Score)+" -(its a Tie)- "+str(Computer_Score)+" Computer"+"\n")
    elif not Player_Choice.upper() in RPC_Choices:
        Round -=1
        print("[Consol] ERROR Please only use the words given to you. ")
    Round +=1
 
    if Round == 15:
        if Player_Score > Computer_Score:
            print("---------You WIN !!---------")
        elif Player_Score < Computer_Score:
            print("---------You LOSE !!---------")
        elif Player_Score == Computer_Score:
            print("---------Its a Tie !!---------")
        break
