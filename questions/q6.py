"""
1. How to swap two variables in python without using a third variable?
2. What will be the output of following code?
"""


names = ["Jon", "Jane", "Eren", "Ragnar", "Arya"]
print(list(enumerate(names, start=1)))

a = list(enumerate(names, start=1))

# [(1,Jon), (2, Jane), (3, Eren)...]

for count, value in a:
    print(count)  # 1
    print(value) # Jon