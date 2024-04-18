"""
1. What is the order of the arguments in functions and methods
a. Keyword Args / Default Args  2
b. Positional  1
c. **kwargs  4
d. *args  3

2. Explain *arsg and **kwargs
"""


def addition(*args, **kwargs):
    print(args)  # (1, 2, "Hello", "World", [3, 4])
    print(kwargs)  # {"name": "Ram", "age": 20}


addition(1, 2, "Hello", "World", [3, 4], name="Ram", age=20)
