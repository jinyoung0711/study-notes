# =====================================
# 🚀 TASK 1: If Else
# =====================================

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride")


""" Comparison Operators
    Operator / Meaning 
    > / Greater than
    < / Less than
    >= / Greater than or equal to
    <= / Less than or equal to
    == / Equal to
    != Not equal to
"""

# =====================================
# 🚀 TASK 2: Modulo
# =====================================

number_to_check = int(input("What is the number you want to check? "))

if number_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")

# =====================================
# 🚀 TASK 3: Nesting and Elif 
# 🚀 TASK 4: Multiple Ifs 
# =====================================

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age > 18:
        bill = 12
        print("You should pay $12.")
    elif (age > 12 and age < 18):
        bill = 7
        print("You should pay $7.")
    else:
        bill = 5
        print("You should pay $5.")

    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
    if wants_photo == 'y':
        # Add $3 to their bill
        bill += 3

    print(f"Your final bill is {bill}.")  
else:
    print("Sorry you have to grow taller before you can ride.")


"""
if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age <= 12:
        print("You should pay $5.")
    elif age <=18:
        print("You should pay $7.")
    else:
        print("You should pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")
"""


# =====================================
# 🚀 TASK 5: Python Pizza 
# =====================================

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo : work out how much they need to pay based on their size choice.

bill = 0 
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else: 
    print("You typed the wrong inputs.")

# todo : work out how much to add to their bill based on their pepperoni choice.
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# todo : work out their final amount based on whether if they want extra cheese.
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}.")


# =====================================
# 🚀 TASK 6: Logical Operators 
# =====================================

# True and True is True
# False and True is False
# True and False is False

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("You should pay $5.")
    elif age <= 18:
        bill = 7
        print("You should pay $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("You should pay $12.")

    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
    if wants_photo == 'y':
        # Add $3 to their bill
        bill += 3

    print(f"Your final bill is {bill}.")  
else:
    print("Sorry you have to grow taller before you can ride.")

# =====================================
# 🚀 TASK 7: Treasure Island Project
# =====================================

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____ 
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____ 
/______/______/______/______/______/______/______/______/______/______/[TomekK] 
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")  

choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()

if choice1 == "left":
    choice2 = input(
        "You've come to a lake. There is an island in the middle of the lake.\n"
        "Type 'wait' to wait for a boat or 'swim' to swim across: "
    ).lower()
    
    if choice2 == "wait":
        choice3 = input(
            "You arrive at the island unharmed.\n"
            "There is a house with 3 doors: One red, one yellow, and one blue.\n"
            "Which color do you choose? "
        ).lower()

        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure. You win! 🎉")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")  

    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")