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
            print("Invalid input. Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")
        
while True:
    try:
        tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
        if tip not in [10, 12, 15]:
            print("Invalid input. Please enter a valid tip percentage (10, 12, or 15).")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")
        
while True:
    try:
        people = int(input("How many people to split the bill?"))
        if people <= 0:
            print("Invalid input. Please enter a positive integer.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")