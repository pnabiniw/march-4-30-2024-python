# map(), reduce() and filter() are the built-in functions in python
# They are higher order functions which take function as an argument

# map()
# map takes two arguments. First argument is a function and second should be an iterable
# map function changes each item of the iterable into a new form.
# the change of the element is based on the function definition
# The final count of the mapped elements and the initial iterable is same in the case of map.

data = [1, 2, 3, 4, 5]


def add_ten_to_each_element(element):
    return element + 10


result = map(add_ten_to_each_element, data)

print(list(result))  # [11, 12, 13, 14, 15]


# filter()
# filter takes two arguments. First argument is a function and second should be an iterable
# filter function picks certain items of the iterable.
# the choosing of the element is based on the function definition
# The final count of the filtered elements and the initial iterable may or may not be same

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_odd_number(element):
    if element % 2 == 0:
        return False  # Falsy
    return True  # Truthy


result = filter(is_odd_number, data)

print(list(result))  # [1, 3, 5, 7, 9]


students = [
    {"name": "Jon", "age": 21, "address": "KTM"},
    {"name": "Jane", "age": 25, "address": "BKT"},
    {"name": "Alex", "age": 27, "address": "LTP"},
    {"name": "Hary", "age": 30, "address": "PKR"},
    {"name": "Arya", "age": 28, "address": "KTM"},
]

# filter those students whose age is greater than 25 using filter() function
# 1. Normal Solution
# 2. using filter() function

# [
#     {"name": "Alex", "age": 27, "address": "LTP"},
#     {"name": "Hary", "age": 30, "address": "PKR"},
#     {"name": "Arya", "age": 28, "address": "KTM"},
# ]

result = []
for each in students:
    if each['age'] > 25:  # type(each) == dict
        result.append(each)
print(result)

# using filter
def is_greater_than_25(element):  # type(element) == dict
    if element['age'] > 25:
        return True
    return False

result = filter(is_greater_than_25, students)  # type(students) == list; [{}, {}, {}]
print(list(result))



students = [
    {"name": "Jon", "age": 24, "address": "KTM"},
    {"name": "Jane", "age": 25, "address": "BKT"},
    {"name": "Alex", "age": 27, "address": "LTP"},
    {"name": "Hary", "age": 30, "address": "PKR"},
    {"name": "Arya", "age": 28, "address": "KTM"},
]

"""
students = [
    {"name": "JON", "age": 21, "address": "KTM"},
    {"name": "JANE", "age": 25, "address": "BKT"},
    {"name": "ALEX", "age": 27, "address": "LTP"},
    {"name": "HARY", "age": 30, "address": "PKR"},
    {"name": "ARYA", "age": 28, "address": "KTM"},
]
"""

result = []
for each in students:
    each["name"] = each["name"].upper()
    result.append(each)
print(result)


def name_to_upper(element):  # type(element) == dict
    element['name'] = element["name"].upper()
    return element


result = map(name_to_upper, students)
print(list(result))


# reduce()
# reduce takes two arguments. First argument is a function and second should be an iterable
# reduce function process the input and gives a single result.
# the processing of the element is based on the function definition
# The final result is a single item

import functools

data = [1, 2, 3, 4, 5]

def sum_of_all(x, y):
    return x + y

result = functools.reduce(sum_of_all, data)
print(result)  # 15


"""
students = [
    {"name": "JON", "age": 20, "address": "KTM"},
    {"name": "JANE", "age": 20, "address": "BKT"},
    {"name": "ALEX", "age": 20, "address": "LTP"},
    {"name": "HARY", "age": 20, "address": "PKR"},
    {"name": "ARYA", "age": 20, "address": "KTM"},
]
"""

students = [
    {"name": "JON", "age": 20, "address": "KTM"},
    {"name": "JANE", "age": 20, "address": "BKT"},
    {"name": "ALEX", "age": 20, "address": "LTP"},
    {"name": "HARY", "age": 20, "address": "PKR"},
    {"name": "ARYA", "age": 20, "address": "KTM"},
]

def sum_of_ages(x, y):  # x can be a dict; x can be a number
    if type(x) == dict:
        return x["age"] + y["age"]  # 40
    return x + y["age"]


result = functools.reduce(sum_of_ages, students)
print("------>", result)
