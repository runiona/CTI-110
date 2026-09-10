# Aiden Runion
# 9/10/26
# P1HW2
# Program with math

print("Hello!")
# use int when using a variable for math
budget_price = int(input("What is your budget? $ "))

travel_des = input("Where is your travel destination? ")

gas_price = int(input("How much will you be spending on gas? $ "))

acom_price = int(input("How much will you be spending on accomodation? $ "))

f_price = int(input("How much will you be spending on food? $ "))

print("-----Travel Expenses-----")
print("Initial Budget: ", budget_price)

print("Fuel: ", gas_price)
print("Accomodation: ", acom_price)
print("Food: ", f_price)

answer = gas_price + acom_price + f_price

print("\n\n"); 
print(gas_price, "+", acom_price, "+", f_price, "= Total price:", answer)

answer2 = budget_price - answer

print(budget_price, "-", answer, "= Total subtracted from budget:", answer2)