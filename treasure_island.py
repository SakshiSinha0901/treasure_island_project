print('''*******************************************************************************
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



print("Welcome to the treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below the line

choice1 = input("You are at a crossroad. There are two turns. Where do you want to go 'left' or 'right' ?" ).lower()
if choice1 == "left":
  choice2 = input('You have come to a lake safely. Their is a island in the middle of the lake. Would you like to wait for the boat then type "wait"or "swim" if you can swim.').lower()
  if choice2 == "wait":
    choice3 = input('You have reached to the island unharmed and their is a house which you have entered which is having three doors. One is red, yellow and blue. Which one will you choose ?')
    if choice3 == "red":
      print("The room was full of beast and you died. Game Over.")
    elif choice3 =="yellow":
      print("You chose the right door and have found the tresure. You Won.")
    elif choice3 == "blue":
      print("You chose the wrong door full of snakes. Game Over.")
    else:
      print("You chose the door that do not exist. Game Over.")
  else:
    print("The lake was full of crocodile and you lost. Game Over")
else:
  print("The room was full of fire and you have lost. Game Over.")
    


