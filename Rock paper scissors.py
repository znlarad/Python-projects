#Rock paper scissors game with record
#This code is written by znl_arad


import random
name=input('What is your name friend?')
print("welcom to game", name)
print("we are going to play rock paper scissors")
print("we are going to play the game as long as  you lose more than one time ")
print("when the game ends you will see your record ")

x=input("are you ready?(yes/no)")

#creating the random function used for picking one
def choice():
    list = ["rock", "paper", "scissors"]
    global answer
    answer = random.choice(list)
    global user_input
    user_input1=input("rock?paper?scissors")
    user_input=user_input1.lower()
    print( "-",answer)
lost=0
won=0

#designing loops 
#continue as long as user has not lost twice and is ready
while lost<2 and x=="yes":
    choice()
    if answer== user_input:#when both the user and computer say the same thing
        print("one more time")
        choice()
    if answer == "rock":
        if user_input == "paper":
            print("won")
            won=won+1
        if user_input == "scissors":
            print("lost")
            lost = lost + 1 #adding one lost to total
    if answer == "scissors":
        if user_input == "paper":
            print("lost")
            lost = lost + 1
        if user_input == "rock":
            print("won")
            won = won + 1
    if answer == "paper":
        if user_input == "rock":
            print("lost")
            lost = lost + 1
        if user_input == "scissors":
            print("won")
            won = won + 1

    if lost>1:#when you have lost more than on time
     total = lost + won #gives your record
     print("you have lost the game")
     print("you played",total,"times")
     print("your record : ",won)

     break



