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
quest1 = input('There are two boats departing the port... left is going to unknown island and right is going to Flordia. Which boat do you want get on "right" or "left"?\n').lower()

if quest1 == "left":
  quest2 = input('On your trip to the unknow island, the boat starts to sink. You are now stuck in the middle of the ocean. Do you "swim" and look for lan or do you "wait" and hope someone resuces you?\n').lower()
  if quest2 == "wait":
    quest3 = input('You are resuced by local fishers and they take you an unknown island. They tell you that there is teasure for you but you must choice the correct color drink. Choice "red", "blue", or "yellow"\n').lower()
    if quest3 == "yellow":
      print("You drink the yellow drink while he men bring you to a vast teasure of gold and jewels. They offer to take you back to you home! YOU WIN!!!")
    elif quest3 == "blue":
      print("You drink the blue drink and you realize you can no longer move... and then you are feed to the local wild beast! GAME OVER")
    elif quest3 == "red":
      print("You drinkk the red drink and immediately become weak. Locals come and take you away to the local volcano. You are shortly thrown into the volcano as sacrifice to the GODS. GAME OVE")
    else:
      print("Thats not a choice!!! Local are offended and throw back into the ocean. GAME OVER")
  else:
    print("You're not a good swmin, you have drowned... WHOMP WHOMP WHAAAA. GAME OVER")
else:
  print("You get on the boat to Florida, on the trip the crew finds out you didnt pay for a ticket and you are now forces to work for an elderly home for the next 10 years to pay off the debt. Game Over.")
