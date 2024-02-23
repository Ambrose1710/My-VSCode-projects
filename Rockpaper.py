import random
from enum import IntEnum #applying this didin't work out but i just left it there


while True:
    
    user_choice = input("Enter your choice;(r for rock, s for scissors, p for paper): \n")
    
    
    options = ['rock','paper','scissors']
    comp_choice = random.choice(options)
    
    def game_output():
        if user_choice == comp_choice:
            print(f"We both choose {user_choice}. A tie then😅")
        elif user_choice == 'r':
            if comp_choice == 'paper':
                print(f"I defeat your rock with my {comp_choice}. Bettr luck next time😁")
            else:
                print(f"You smashed my {comp_choice} with your rock. I loose😒")
        elif user_choice == 's':
            if comp_choice == 'rock':
                print(f"I smash your scissors with my {comp_choice}. Bettr luck next time😁")
            else:
                print(f"You cut my {comp_choice} with your scissors. I loose😒")
        elif user_choice == 'p':
            if comp_choice == 'scissors':
                print(f"I cut your paper with my {comp_choice}. Bettr luck next time😁")
            else:
                print(f"You deafeated my {comp_choice} with your paper. I loose😒")
        else:
            print("Hmmm..are you sure you entered the right input? 'Cause something's not right👀")
    
    game_output()

    play_again = input("Do you want to play again? (y/n): \n")
    if play_again.lower() == 'y':
        break

