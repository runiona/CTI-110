# Aiden Runion
# 10/28/2026
# P4LAB2
# While loop and for loop together

'''
# Get integer from user 
# determine if integer is pos or neg
# if number is pos, display multiplication table
# if number is neg, cannot accept
# ask user to run program again
# user says yes, run again
# user says no, end program
'''

run_again = 'yes' 

while run_again != "no":

    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
        # display multiplicaation for that value and range 
         for item in range(1, 13):
           print(f"{user_num} * {item} = {user_num * item}")
    else: 
         print("This program does not handle negative values.")

    run_again = input("Would you like to run the program again?: ")

#Loop has broken. User entered no
print("Program is ending...")