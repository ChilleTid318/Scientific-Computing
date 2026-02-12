# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 14:41:13 2026

@author: aidan
"""
import random as ra
from random import randint
def roll():
    Dice1 = ra.randint(1,6)
    Dice2 = ra.randint(1,6)
    total = Dice1 + Dice2 #allows 2 dice to be rolled! I thought it would be fun to try and figure out how to do so.
    answer = f"Dice rolled: {Dice1} + {Dice2} \nMove up {total} spaces."
    return Dice1, Dice2, total, answer
#Dice1, Dice2, total, answer = roll() #unpack everything from the function for use!!! Allows me not to repeat code on here according to Youtube.
p1_position = 1 #keeps track of player one's position, the board starts at space 1
p2_position = 1 #keeps track of p2's position
Final_Space = 100 #game ends when someone reaches this spot.
#cool reply that I invented, google showed me what an f-string is, f"{}" is pretty cool when printing stuff

print("Welcome to the Cool Epic Board Game Aidan Hayes made!") #Name of the game!!!

while True: #rest of code will be under this because this actually allows the game to end!!!! 
#PLAYER 1 Code
    input("PLAYER 1's turn. Press Enter to roll the dice...")
    Dice1, Dice2, total, answer = roll() #this fixed my ERROR below. In the while True: it's a part of the loop, fixing the problem
    print(answer) #prints my beautiful answer from roll()
    
    start_pos = p1_position #keeping track of position
    new_pos = start_pos + total #new position
    
    print(f"Player 1 moves from {start_pos} to {new_pos}") #cool that keeps track of the first turn but not the second. thats hopefully where turn comes to play
    
    p1_position = new_pos #1. ERROR so this isn't changing the dice roll. 2. figured it out.
    
    if new_pos >= Final_Space: #using what we learned in the first class, this allows me to 
        print("PLAYER 1 wins!!! CONGRATULATIONS")
        break #thank you google for teaching me, you are oh so wise. Thank you for telling me about break :O
        #IT WORKS RAHHHHH, now to add special spaces....
#Ruh Roh! It's the special spots on the board!. I just used simple +=, ==, and -= signs, and repeated a bunch of code.
    if new_pos == 5:
        print("Hooray! Move up 3 spaces.")
        new_pos += 3

    if new_pos == 11:
        print("Oops! Move back 2 spaces.")
        new_pos -= 2

    if new_pos == 18:
        print("Hooray! Move up 5 spaces.")
        new_pos += 5

    if new_pos == 23:
        print("Oops! Move back 4 spaces.")
        new_pos -= 4

    if new_pos == 29:
        print("Hooray! Move up 6 spaces.")
        new_pos += 6

    if new_pos == 34:
        print("Oops! Move back 7 spaces.")
        new_pos -= 7

    if new_pos == 41:
        print("Hooray! Move up 4 spaces.")
        new_pos += 4

    if new_pos == 47:
        print("Oops! Move back 5 spaces.")
        new_pos -= 5

    if new_pos == 53:
        print("Hooray! Move up 7 spaces.")
        new_pos += 7

    if new_pos == 60:
        print("Oops! Move back 6 spaces.")
        new_pos -= 6

    if new_pos == 68:
        print("Hooray! Move up 8 spaces.")
        new_pos += 8

    if new_pos == 75:
        print("Oops! Move back 9 spaces.")
        new_pos -= 9

    if new_pos == 83:
        print("Hooray! Move up 5 spaces.")
        new_pos += 5
    if new_pos == 89:
        print("Oops! Move back 4 spaces.")
        new_pos -= 4
    if new_pos == 93:
        print("Hooray! Move up 2 spaces.")
        new_pos += 2
#Now that I'm done the basics, I can now add Player 2 and repeat the code.
#PLAYER 2
    input("Player 2's turn. Press Enter to roll the dice...")
    Dice1, Dice2, total, answer = roll()
    print(answer)

    start_pos = p2_position
    new_pos = start_pos + total

    print(f"Player 2 moves from {start_pos} to {new_pos}")
    
    p2_position = new_pos
    
    if new_pos >= Final_Space:
        print("Player 2 WINS!")
        break
    if new_pos == 5:
        print("Hooray! Move up 3 spaces.")
        new_pos += 3

    if new_pos == 11:
        print("Oops! Move back 2 spaces.")
        new_pos -= 2

    if new_pos == 18:
        print("Hooray! Move up 5 spaces.")
        new_pos += 5

    if new_pos == 23:
        print("Oops! Move back 4 spaces.")
        new_pos -= 4

    if new_pos == 29:
        print("Hooray! Move up 6 spaces.")
        new_pos += 6

    if new_pos == 34:
        print("Oops! Move back 7 spaces.")
        new_pos -= 7

    if new_pos == 41:
        print("Hooray! Move up 4 spaces.")
        new_pos += 4

    if new_pos == 47:
        print("Oops! Move back 5 spaces.")
        new_pos -= 5

    if new_pos == 53:
        print("Hooray! Move up 7 spaces.")
        new_pos += 7

    if new_pos == 60:
        print("Oops! Move back 6 spaces.")
        new_pos -= 6

    if new_pos == 68:
        print("Hooray! Move up 8 spaces.")
        new_pos += 8

    if new_pos == 75:
        print("Oops! Move back 9 spaces.")
        new_pos -= 9

    if new_pos == 83:
        print("Hooray! Move up 5 spaces.")
        new_pos += 5
    if new_pos == 89:
        print("Oops! Move back 4 spaces.")
        new_pos -= 4
    if new_pos == 93:
        print("Hooray! Move up 2 spaces.")
        new_pos += 2
