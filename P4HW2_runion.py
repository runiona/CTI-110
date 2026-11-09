# Runion
# 11/8/2026
# P3HW2
# Salary Calculator

# request employee info
name = input("Enter employee name or 'done' to finish: ")

overtimepay_total = 0
regularpay_total = 0
grosspay_total = 0
employee_count = 0

while name != 'done':
    employee_count += 1 
    hours = float(input("How many hours did " +name+ " work this week? "))
    rate = float(input("What is " +name+ "'s hourly payrate? "))

    # eval overtime
    if hours > 40:
        # calculate overtime
        overtime_hours = hours - 40
        # calculate over pay
        overtime_pay = overtime_hours * (rate * 1.5)
        # calculate salary for regular hours
        regular_pay = 40 * rate
        # calculate gross pay
        gross_pay = regular_pay + overtime_pay
    else:
        overtime_pay = 0
        overtime_hours = 0
        regular_pay = hours * rate
        gross_pay = regular_pay

    overtimepay_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay


    # Display results!
    print("--------------------------------------------------------------------------------")
    print("Employee name: ", name)
    print(f'{"Hours worked":<15}{"Pay rate":<12}{"Overtime pay":<15}{"Regular pay":<15}{"Gross pay":<12}')
    print("--------------------------------------------------------------------------------")
    print(f'{hours:<15}{rate:<12}{overtime_pay:<15}{regular_pay:<15}{gross_pay:<15}')

    name = input("Enter employee's name or 'done' to finish: ")

print("Total number of employee's entered:", employee_count)
print("Total amount paid for overtime: $", format(overtimepay_total, ',.2f'))
print("Total amount paid for regular time: $", format(regularpay_total, ',.2f'))