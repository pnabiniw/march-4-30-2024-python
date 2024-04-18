"""
What is the output of the following code?
"""

student = {"name": "Krish", "age": 24}
print(student["id"])  # IndexError, KeyError, None

student.get("id")  # None
student.get("id", 3)
