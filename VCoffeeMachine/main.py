from menu import MENU, resources


def resourcereport(amount):
    for r in resources:
        print(r, ':', resources[r])
    print(f"Money: ${amount}")


def checkresources(option):
    enough = True
    for i in MENU[option]['ingredients']:
        if MENU[option]['ingredients'][i] > resources[i]:
            print("Sorry there is not enough", i)
            enough = False
            break
    if enough:
        return True
    else:
        return False


def takemoney():
    print("Please insert coins")
    coins = {
        "quarters": .25,
        "dimes": .10,
        "nickles": .05,
        "pennies": .01,
    }
    total = 0.00
    for c in coins:
        coin = float(input(f"How many {c}?: ")) * coins[c]
        total = total + coin
    return total


def updateresources(drink):
    ingredients = MENU[drink]['ingredients']
    for i in ingredients:
        newamount = resources[i] - ingredients[i]
        resources.update({i: newamount})


def makedrink(drink, totalmoney):
    if MENU[drink]['cost'] > totalmoney:
        print("Sorry that's not enough moeny. Money refunded.")
    else:
        cost = MENU[drink]['cost']
        change = totalmoney - cost
        print(f'Here is ${change} in change.')
        print(f'Here is your {drink}☕. Enjoy!')
        updateresources(drink)
    return cost


def coffeemachine():
    machinceon = True
    money = .00
    while machinceon:
        answer = input("What would you like? (espresso/latte/cappuccino): ")
        if answer == "off":
            machinceon = False
        elif answer == "report":
            resourcereport(money)
        else:
            if checkresources(answer):
                moneycollected = takemoney()
                payment = makedrink(answer, moneycollected)
                money = money + payment
    return


coffeemachine()
