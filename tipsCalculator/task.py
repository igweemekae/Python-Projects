# Welcome message
print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10 12 15:  "))

people = int(input("How many people to split the bill? "))

tipAmount = (tip/100) * bill

totalAmount = bill + tipAmount

eachPays = round((totalAmount / people),2)

print(f"Hey friends! each person pays ${eachPays}")