# Author: Rebecca Schwab
# Copyright 2022 Rebecca Schwab
# PlanktonGirl on GitHub 

import random
import time

a = 2
b = 3
c = 4


def coin_flip():
    player_counter = 0
    computer_counter = 0
    while player_counter < 5 and computer_counter < 5:
        print("")
        while True:
            heads_or_tails = input("Heads or Tails? H/T: ")
            time.sleep(a)
            if heads_or_tails.lower() not in ('h', 't'):
                print("I didn't understand that response. Please answer 'H' or 'T'")
                time.sleep(a)
                print("")
            else:
                break
        print("Flipping...")
        time.sleep(b)
        coin = random.randint(1, 2)
        if coin == 1:
            print("Heads!")
            time.sleep(a)
            if heads_or_tails.lower() == "h":
                player_counter += 1
                print("Good job! You get 1 point!")
                time.sleep(a)
                print("Current score: You: " + str(player_counter) + "     Me: " + str(computer_counter))
                time.sleep(a)
            else:
                computer_counter += 1
                print("Sorry, that's a point for me.")
                time.sleep(a)
                print("Current score: You: " + str(player_counter) + "     Me: " + str(computer_counter))
                time.sleep(a)
                                 
        elif coin ==2:
            print("Tails!")
            time.sleep(a)
            if heads_or_tails.lower() == "t":
                player_counter += 1
                print("Good job! You get 1 point!")
                time.sleep(a)
                print("Current score: You: " + str(player_counter) + "     Me: " + str(computer_counter))
                time.sleep(a)
            else:
                computer_counter += 1
                print("Sorry, that's a point for me.")
                time.sleep(a)
                print("Current score: You: " + str(player_counter) + "     Me: " + str(computer_counter))
                time.sleep(a)
    if player_counter == 5:
        print("")
        print("Congratulations! You have 5 points! You win!")
        print("")
        time.sleep(a)
    else:
        print("")
        print("Sorry! That's 5 points for me! Better luck next time!")
        print("")
        time.sleep(a)
    while True:
        play_again_win = input("Play again? Y/N: ")
        if play_again_win.lower() not in ('y', 'n'):
            print("")
            print("I didn't understand that response. Please answer 'Y' or 'N'")
            print("")
            time.sleep(a)
        else:
            break
    if play_again_win == "Y" or play_again_win == "y":
        player_counter = 0
        computer_counter = 0
        time.sleep(a)
        coin_flip()
    else:
        print("")
        print("Ok, come back again soon!")  
        time.sleep(a)     


print("**************************************************************")
print("*                                                            *")
print("*                 Rebecca's Flip 'O the Coin                 *")
print("*                                                            *")
print("**************************************************************")
print("")
print("")
time.sleep(a)
print("Welcome to 'Flip 'O the Coin!'")
print("")
time.sleep(b)
print("I'm going to flip a coin.")
time.sleep(b)
print("Before I do that, I'm going to ask you to guess, 'Heads or tails?'")
time.sleep(c)
print("If you guess right, you get 1 point.")
time.sleep(c)
print("If you guess wrong, *I* get 1 point.")
time.sleep(c)
print("First person to 5 points wins.")
time.sleep(c)
while True:
    print("")
    ready = input("Ready to play? Y/N: ")
    if ready.lower() not in ('y', 'n'):
        print("")
        print("I didn't understand that response. Please answer 'Y' or 'N'")
    else:
        break
if ready == "Y" or ready == "y":
    print("")
    print("Great! Let's get started.")
    time.sleep(a)
    coin_flip()
else:
    print("")
    print("Ok, come back when you're ready to play.")
