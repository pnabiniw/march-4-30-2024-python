"""
WAP to prompt the user for hours and rate per hour using input to compute gross pay.
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.

Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
You should use input to read a string and float() to convert the string to a number.

"""

total_hrs = float(input("Enter total hour "))
rate = float(input("Enter rate per hour "))

if total_hrs <= 40:
    total_pay = total_hrs * rate
else:
    ot_hrs = total_hrs - 40
    ot_pay = ot_hrs * rate * 1.5
    normal_pay = rate * 40
    total_pay = ot_pay + normal_pay

print(f"total pay is {total_pay}")
