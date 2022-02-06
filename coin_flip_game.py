import random
from tkinter import Y

def coin_flip():
    player_counter = 0
    computer_counter = 0
    while player_counter < 5 and computer_counter < 5:
        heads_or_tails = input("Heads or Tails? H/T: ")
        print("Flipping...")
        coin = random.randint(1, 2)
        if coin == 1:
            print("Heads!")
            if heads_or_tails == "H" or heads_or_tails == "h":
                player_counter += 1
                print("Good job! You get 1 point!")
                print("Current score: You - " + str(player_counter) + "     Me - " + str(computer_counter))
            else:
                computer_counter += 1
                print("Sorry, that's a point for me.")
                print("Current score: You - " + str(player_counter) + "     Me - " + str(computer_counter))
                          
        elif coin ==2:
            print("Tails!")
            if heads_or_tails == "T" or heads_or_tails == "t":
                player_counter += 1
                print("Good job! You get 1 point!")
                print("Current score: You - " + str(player_counter) + "     Me - " + str(computer_counter))
            else:
                computer_counter += 1
                print("Sorry, that's a point for me.")
                print("Current score: You - " + str(player_counter) + "     Me - " + str(computer_counter))
    if player_counter == 5:
        print("Congratulations! You have 5 points! You win!")
    else:
        print("Sorry! That's 5 points for me! Better luck next time")
    play_again_win = input("Play again? Y/N: ")
    if play_again_win == "Y" or play_again_win == "y":
        player_counter = 0
        computer_counter = 0
        coin_flip()
    else:
        print("Ok, come back again soon!")       


print("**************************************************************")
print("*                                                            *")
print("*                 Rebecca's Flip 'O the Coin                 *")
print("*                                                            *")
print("**************************************************************")
print("")
print("")
print("Welcome to 'Flip 'O the Coin!'")
print("I'm going to flip a coin.")
print("Before I do that, I'm going to ask you to guess, 'Heads or tails?'")
print("I you guess right, you get 1 point.")
print("If you guess wrong, I get 1 point.")
print("First person to 5 points wins.")
ready = input("Ready to play? Y/N: ")
if ready == "Y" or ready == "y":
    print("Great! Let's get started.")
    coin_flip()
else:
    print("Ok, come back when you're ready to play.")
