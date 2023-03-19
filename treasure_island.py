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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input("You're at a crossroad, where do you want to go? Type 'left' or 'right' ")

if choice1.lower() == "left":
    choice2 = input("You've come to a lake, what do you want to do? Type 'wait' to wait for a boat or 'swim' to swim across ")
    if choice2.lower() == "wait":
        choice3 = input("You see a house in the distance, it has 3 doors. Type 'blue' to enter the blue door, 'yellow' to enter the yellow door or 'red' to enter the red door ")
        if choice3.lower() == "yellow":
            print("YOU FOUND THE TREASURE, YOU WIN")
        elif choice3.lower() == "blue":
            print("You enter a room full of gorillas and get beaten to death, game over.")
        elif choice3.lower() == "red":
            print("You walk into a room of fire, game over.")
    else: 
        print("You get hypothermia and die halfway across, game over.")
else:
    print("You get hit by a high speed tractor, game over.")
