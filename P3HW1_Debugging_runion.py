# Runion
# 10/1/2026
# P3HW1
# Debugging


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low_ = min(grades)
high_ = max(grades)
sum_ = sum(grades)
avg_ = sum_ / len(grades)

# determine letter grade for average

print("----------Results----------")
print(f"{"Lowest grade: ":<20} {low_:<20}")
print(f"{"Highest grade: ":<20} {high_:<20}")
print(f"{"Sum of grades: ":<20} {sum_:<20}")
print(f"{"Average: ":<20} {avg_:<20,.2f}")
print("----------------------------")

if avg_ >= 90:
    print('Your grade is: A')
elif avg_ >= 80:
        print('Your grade is: B')
elif avg_ >= 70:
        print('Your grade is: C')
elif avg_ >= 60:
        print('Your grade is: D')
else:
        print('Your grade is: F')







