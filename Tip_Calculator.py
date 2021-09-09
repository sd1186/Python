print("Welcome to the Tip Calculator.")
bill = (input("What was your total bill? $"))
tip_percent = (input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = (input("How many people to split the bill? "))

pay_per_person = (round(float(bill)/float(num_people)*(1 + int(tip_percent)/100), 2))

print(f"Each person should pay: ${pay_per_person}")
