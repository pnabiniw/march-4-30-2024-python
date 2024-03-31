"""
Create a class Department with parameters name and number_of_students.
Create a method total students, which takes department object as a parameter and return the total
number of students from all departments.

"""
from functools import reduce
class Department:
    def __init__(self, name, number_of_students):
        self.name = name
        self.number = number_of_students

    def total_students(self, *others):
        summ = 0
        for other in others:
            if isinstance(other, Department):
                summ += other.number
        return self.number + summ

    def total_numbers(self, departments):
        summ = 0
        for other in departments:
            summ += other.number
        return self.number + summ


d1 = Department("CS", 10)
d2 = Department("Electrical", 20)
d3 = Department("Civil", 30)

depts = [d1, d2, d3]

result = d1.total_students(d2, d3)
print(result)  # 60

result2 = d1.total_students(depts)
print(result2)
