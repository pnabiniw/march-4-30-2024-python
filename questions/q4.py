"""
1. What are the methods to get keys, values and key-value pair in a dictionary?
2. How to loop in key-value pair?

"""

student = {"name": "ram", "age": 30}  # [(name, ram), (age, 30)]

keys = student[0]  # Error

print(student.keys())

print(student.values())

print(list(student.items()))

for key, value in student.items():
    print(key, value)
