import json

filename = "students.json"


def delete_student():
    id = input("Enter student id ")
    with open(filename, "r") as fp:
        students = json.loads(fp.read())  # [{}, {}, {}]
    for student in students:
        if student["id"] == id:
            students.remove(student)

    with open(filename, "w") as fp:
        fp.write(json.dumps(students, indent=2))
    print("Student deleted successfully !!")
    cont = input("Do you want to continue?(y/n) ")
    return True if cont.lower() == "y" else False
