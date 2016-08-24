# We will be playing rock, paper, scissors!
from random import randint
from time import sleep

options = ["R", "P", "S"]

WINNER_MSGE = "Congrats! Come getcha monayyyy!"
LOSER_MSGE = "You lost!"
def decide_winner(user_choice, computer_choice):
    print "You selected %s" % user_choice
    print "Computer selecting..."
    sleep(1)
    print "Computer selected: %s" % computer_choice
    user_choice_index = options.index(user_choice)
    computer_choice_index = options.index(computer_choice)
    if user_choice_index == computer_choice_index:
        print "It's a tie so no one won! jejeje!"
    elif user_choice == options[0] and computer_choice == options[2]:
        print WINNER_MSGE
    elif user_choice == options[1] and computer_choice == options[0]:
        print WINNER_MSGE
        
    elif user_choice == options[2] and computer_choice == options[1]:
        print WINNER_MSGE
    elif user_choice > options[2]:
        print "Invalid selection! Try again."
        return
    else:
        print LOSER_MSGE
        
def play_RPS():
    print "Welcome to Rock, Paper, Scissors!"
    user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors: ")
    sleep(1)
    user_choice = user_choice.upper()
    computer_choice =  options[randint(0, len(options) -1)]
    decide_winner(user_choice, computer_choice)
    
play_RPS()
