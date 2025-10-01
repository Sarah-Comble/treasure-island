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

direction = input("There is a crossroad in front of you. You can go left or right. Which way do you choose? ")
direction = direction.lower()

if direction == "left":
  action = input("You have reached a lake. There is an island in the middle. Do you want to swim or wait for a boat ? type swim or wait ").lower()
  if action == "wait":
    door = input("You have arrived at the island. There is a house with 3 doors. Which one do you choose ? red, yellow or white? ").lower()
    if door == "red":
      print("You have been burned by fire, sorry game over.")
    elif door == "yellow":
      print("You have been attacked by bees, sorry game over.")
    elif door == "white" :
      print ("Congratulation, you have found the treasure.")
    else:
      print("Sorry we don't understand, game over.")
  else:
    print("An aligator eats you, Game Over.")  
else:
  print("Game over. You have been attacked by indigenes.")
