print("Welcome to the tip calculator.")

bill = float(input("What was the total bill?\n"))

people = int(input("How many people to split the bill?\n"))

tip = int(input("What percentage tip would you like to give? 10, 12, 15 or 20?\n"))

tip_percent = tip / 100

total_tip_amount = bill * tip_percent

total_bill = bill + total_tip_amount

bill_per_person = total_bill / people

print("The total bill for each person is: " + str(round(bill_per_person)))