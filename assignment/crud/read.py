import json

filename = "students.json"


def read_student():
    id = input("Enter the student id ")
    with open(filename, "r") as fp:
        students = json.loads(fp.read())  # [{}, {}, {}]
        for student in students:
            if student["id"] == id:
                print(student)
    cont = input("Do you want to continue?(y/n) ")
    return True if cont.lower() == "y" else False
