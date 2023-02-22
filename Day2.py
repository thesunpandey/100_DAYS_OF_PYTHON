"""
    The program prompts the user to enter the total bill amount, the desired tip percentage, 
    and the number of people to split the bill. It then calculates the total tip amount, the 
    total bill amount with the tip, and the amount each person should pay. The final bill 
    amount per person is rounded to two decimal places using the round function.
"""

print("Welcome to the tip calculator!")

while True:
    try:
        bill = float(input("What was the total bill? $"))
        if bill <= 0:
            raise ValueError("The bill amount must be greater than zero.")
        break
    except ValueError as e:
        print("Invalid input:", e)
        continue

while True:
    try:
        tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
        if tip not in [10, 12, 15]:
            raise ValueError("The tip percentage must be 10, 12, or 15.")
        break
    except ValueError as e:
        print("Invalid input:", e)
        continue

while True:
    try:
        people = int(input("How many people to split the bill? "))
        if people <= 0:
            raise ValueError("The number of people must be greater than zero.")
        break
    except ValueError as e:
        print("Invalid input:", e)
        continue

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")
