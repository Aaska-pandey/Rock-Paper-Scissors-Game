from random import randint

play_options=["rock","paper","scissors"]

while True:

    computer_play = play_options[randint(0,2)] #play option for computer
    user_play=input("Rock , Paper , Scissors  ?\n"   ).lower()# play option for the user

    if computer_play == user_play:
        print("It's a tie")


    elif user_play == "rock": #computer played either papare or scissors
        if computer_play == "paper":
            print("You lose !",computer_play,"beats",user_play)
        else :
            print(f"YOu win ! {user_play} beats {computer_play}")
        


    elif user_play == "scissors": #computer played either papare or rock
        if computer_play == "paper":
            print("You lose !",computer_play,"beats",user_play)
        else :# rock
            print(f"YOu win ! {user_play} beats {computer_play }")
    

    elif user_play == "paper": #computer played either papare or rock
        if computer_play == "scissors":
            print("You lose !",computer_play,"beats",user_play)
        else :# rock
            print(f"YOu win ! {user_play} beats {computer_play }")


    else:
        print("Not a valid play option , try again !")



