# CTI 110
# A Runion
# P2HW1

print("Hello!")
# use int when using a variable for math
budget_price = int(input("What is your budget? $ "))

travel_des = input("Where is your travel destination? ")

gas_price = int(input("How much will you be spending on gas? $ "))

acom_price = int(input("How much will you be spending on accomodation? $ "))

f_price = int(input("How much will you be spending on food? $ "))

print("\n\n"); 

print("---------Travel Expenses---------")
print(f"{"Location: ":<20} {travel_des:<20}")
print(f"{"Initial Budget: ":<20} ${budget_price:<20,.2f}")
print(f"{"Fuel: ":<20} ${gas_price:<20,.2f}")
print(f"{"Accomodation: ":<20} ${acom_price:<20,.2f}")
print(f"{"Food: ":<20} ${f_price:<20,.2f}")
print("---------------------------------")

answer = gas_price + acom_price + f_price

print("\n\n"); 
print(gas_price, "+", acom_price, "+", f_price, "= Total price: $", answer)

answer2 = budget_price - answer

print(budget_price, "-", answer, "= Total subtracted from budget: $", answer2)