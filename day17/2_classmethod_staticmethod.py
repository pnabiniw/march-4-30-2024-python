

class Person:
    age = 20
    __college = "Trinity"

    @classmethod
    def get_college(cls):
        return cls.__college

    @classmethod
    def set_college(cls, college):
        cls.__college = college

    @staticmethod
    def get_info(address):
        return f"The person lives in {address}"


Person.__college = 40
print(Person.__college)
print(Person.age)  # 20

p = Person()
p.__college = "CCRC"
print(p.__college)
print(Person.__college)

print(Person.get_college())
Person.set_college("ITCOllege")
print(Person.get_college())


# static methods are those methods which do not change the state of an object or class
# static method is created using @staticmethod decorator
print(Person.get_info("PKR"))
print(p.get_info("KTM"))