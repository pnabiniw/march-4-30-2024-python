# WAP to take a number input. If the number is divisible by 3 then print "fizz", if divisible by 5 then
# print "buzz", if divisible by both 3 and 5 then print "fizzbuzz", if not divisible by 3 or 5 then print
# the number as it is

num = int(input("Enter a number "))
if num % 3 == 0 and num % 5 == 0:
    print("fizzbuzz")
elif num % 3 == 0:
    print("fizz")
elif num % 5 == 0:
    print("buzz")
else:
    print(num)
