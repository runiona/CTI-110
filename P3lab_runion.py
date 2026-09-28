# CTI 110
# 9/27/2026
# Runiona
# Making a program to give change

change_ = float(input("Enter an amount of money: $"))

# int will not give you exact rounded calculation
change_ = round(change_ * 100) #100/100=1 dollar 25/100=.25(quarter) etc.

# values for dollars and cents
# // = floor division symbol, how much is able to fit before moving onto next line, ex: 3.25 (3 dollars max then moves to quarters)
dolla_ = change_ // 100
change_ = change_ - (dolla_ * 100)

quarter_ = change_ // 25
change_ = change_ - (quarter_ * 25)

dime_ = change_ // 10
change_ = change_ - (dime_ * 10)

nick_ = change_ // 5
change_ = change_ - (nick_ * 5)

pennies_ = change_

# if the value is more than zero it will print, if its exactly 1 it will provide the singular term(dollar, penny), else use plural
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