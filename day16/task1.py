class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name is {self.name}. Age is {self.age}"


class Employee(Person):
    def __init__(self, name, age, salary, designation):
        super().__init__(name, age)
        self.salary = salary
        self.designation = designation

    def get_details(self):
        print(super().get_details())
        return f"salary is {self.salary} and designation is {self.designation}"


obj = Employee("Jon", 30, 20000, "Manager")
print(obj.get_details())

print(obj.name)  # Jon
