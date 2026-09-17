# CTI 110
# P2HW2
# Runion A

# all module grades
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

grades = [module1, module2, module3, module4, module5, module6]

lowest_ = min(grades)
highest_ = max(grades)
sum_ = sum(grades)
average_

print("----------Results----------")
print(f"{"Lowest grade: ":<20} {lowest_:<20}")
print(f"{"Highest grade: ":<20} {highest_:<20}")
print(f"{"Sum of grades: ":<20} {sum_:<20}")
print
print("----------------------------")