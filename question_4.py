# Task 1

import random

items = ["Ball", "Peanut", "Knife", "Sandwich", "Headphones", "Finger"]

item = random.choice(items)

guess = input("Out of the items: Ball, Peanut, knife, Sandwich, Headphones, Finger guess which one I am thinking of: ")

if guess == item:
    print("Holy shit you guessed it! It was " + item)
else:
    print("Wrong! It was " + item)
