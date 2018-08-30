#game of rock paper scissors - user vs the computer 
import random 

#making a function called play which tests the conditionals of rps logic. 
def play(choice, computer_choice):
    
    display_tie = "It's a tie!"
    display_win = "You won!"
    display_loss = "You lose :("

    rock = "r"
    paper = "p"
    scissors = "s"

    if (choice == rock and computer_choice == rock):
        return display_tie
    elif (choice == rock and computer_choice == scissors):
        return display_win
    elif (choice == rock and computer_choice == paper):
        return display_loss
    elif (choice == paper and computer_choice == rock):
        return display_win
    elif (choice == paper and computer_choice == scissors):
        return display_loss
    elif (choice == paper and computer_choice == paper):
        return display_tie
    elif (choice == scissors and computer_choice == paper):
        return display_win
    elif (choice == scissors and computer_choice == rock):
        return display_loss
    else: 
        return display_tie
        
#added a for loop to running the function so you can specify in code how many times you want to play - simply change the value in the range()
for x in range(1):
    print("I challenge you to a game of Rock Paper Scissors")
    player_choice = input("Choose (r)ock, (p)aper, or (s)cissors \n")
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    result = play(player_choice, computer_choice)
    print(result)

#test code that tests rock (player_choice) against the computers_choice
# print("I challenge you to a game of Rock Paper Scissors")
# player_choice = "r"
# computer_choice = "r"
# result = play(player_choice, computer_choice)
# print(result)

# print("I challenge you to a game of Rock Paper Scissors")
# player_choice = "r"
# computer_choice = "p"
# result = play(player_choice, computer_choice)
# print(result)

# print("I challenge you to a game of Rock Paper Scissors")
# player_choice = "r"
# computer_choice = "s"
# result = play(player_choice, computer_choice)
# print(result)
    




