import json


filename = "students.json"


def update_student():
    id = input("Enter student id ")
    key = input("Enter info you want to change ")
    value = input(f"Enter the new {key} ")
    with open(filename, "r+") as fp:
        students = json.loads(fp.read())  # [{}, {}, {}]
        for student in students:
            if student["id"] == id:
                student[key] = value
        fp.seek(0)
        fp.write(json.dumps(students, indent=2))
    print("Student info updated successfully !!")
    cont = input("Do you want to continue?(y/n) ")
    return True if cont.lower() == "y" else False
