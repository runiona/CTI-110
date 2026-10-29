# Aiden Runion
# CTI-110
# P5LAB
# 10/29/2026
# Self checkout machine simulator. Makes change.
import random
# Put in other functions here.
# Turn the program P3LAB into a function called disperse_change. It should take one float parameter and have no return value.
def disperse_change(amount):
    #print out the change needed.
    # input: float
    # return: nothing
    print(f"Change is: ${amount:.2f}")
    print()
    # put p3lab code here: print number of dollars, quarters, dimes, nickels, pennies.
    amount = round(amount * 100) #100/100=1 dollar 25/100=.25(quarter) etc.

    # values for dollars and cents
    # // = floor division symbol, how much is able to fit before moving onto next line, ex: 3.25 (3 dollars max then moves to quarters)
    dolla_ = amount // 100
    amount = amount - (dolla_ * 100)

    quarter_ = amount // 25
    amount = amount - (quarter_ * 25)

    dime_ = amount // 10
    amount = amount - (dime_ * 10)

    nick_ = amount // 5
    amount = amount - (nick_ * 5)

    pennies_ = amount

#    if the value is more than zero it will print, if its exactly 1 it will provide the singular term(dollar, penny), else use plural
    if dolla_ > 0: 
        if dolla_ == 1:
            print(f"{dolla_} Dollar")
        else:
            print(f"{dolla_} Dollars")

    if quarter_ > 0: 
        if quarter_ == 1:
            print(f"{quarter_} Quarter")
        else:
            print(f"{quarter_} Quarters")

    if dime_ > 0: 
        if dime_ == 1:
            print(f"{dime_} Dime")
        else:
            print(f"{dime_} Dimes")     

    if nick_ > 0: 
        if nick_ == 1:
            print(f"{nick_} Nickel")
        else:
            print(f"{nick_} Nickels")   

    if pennies_ > 0: 
        if pennies_ == 1:
            print(f"{pennies_} Penny")
        else:
            print(f"{pennies_} Pennies")
# Main
def main():
    # Declare varibales
    cost = 0.0
    amount_paid = 0.0
    change_owed = 0.0
    print("Welcome to the self-checkout sim.")
    # Generate a random float value for the cost
    cost = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${cost:.2f}")
    # Ask the user how much $ they put in
    amount_paid = float(input("How much money do you put in the self checkout? $"))
    # calc change owed
    change_owed = amount_paid - cost

    print("Here is your change: ")
    disperse_change(change_owed)



# Last line - start the program
main()