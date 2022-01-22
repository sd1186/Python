import random
from art import logo, vs
from game_data import data


def personA(compA, compB):
    if compA == None :
        compA = random.randrange(50)
    else:
        compA = compB
    print(f"Compare A: {data[compA]['name']}, a {data[compA]['description']}, from {data[compA]['country']}")
    return compA

def personB(compB):
    compB = random.randrange(50)
    while compB == compA:
        compB = rand.randrang(50)
    print(f"Compare B: {data[compB]['name']}, a {data[compB]['description']}, from {data[compB]['country']}")
    return compB

def comparing():
    ans = input("Who has more followers? Type'A' or 'B': ")
    aTotal = data[compA]['follower_count']
    bTotal = data[compB]['follower_count']
    if aTotal > bTotal:
        winner = 'a'
    else:
        winner = 'b'
    if winner == ans.lower():
        print("WINNER")
        return True
    else:
        print("Loser")
        return False



compA = None
compB = None
won = True
winCount = 0

while won == True:
    print(logo)
    if winCount > 0:
        print(f"You're right! Current score: {winCount}")
    compA = personA(compA, compB)
    print(data[compA]['follower_count'])
    print(vs)
    compB = personB(compB)
    print(data[compB]['follower_count'])
    won = comparing()
    winCount = winCount + 1

print(logo)
print(f"Sorry, the's wrong. Final scor: {winCount}")
