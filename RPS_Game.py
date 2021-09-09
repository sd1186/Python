import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

tied = "Tied, Try again"
win = "You Win! Good Job"
lose = "You Lost! Try again"

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 Scissor\n"))

if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)
else:
  print("Please chice a correct number")

print("The computer picks:")
computer = random.randint(0,2)
if computer == 0:
  print(rock)
elif computer == 1:
  print(paper)
elif computer == 2:
  print(scissors)

if choice == 0:
  if computer == 0:
    print(tied)
  elif computer == 1:
    print(lose)
  else:
    print(win)
elif choice == 1:
  if computer == 0:
    print(win)
  elif computer == 1:
    print(tied)
  else:
    print (lose)
elif choice == 2:
  if computer == 0:
    print(lose)
  elif computer == 1:
    print(win)
  else:
    print(tied)
else:
  print("There has been and error")
