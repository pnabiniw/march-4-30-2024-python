import json
import os

filename = "students.json"


def create_student():
    id = input("Enter student id ")
    name = input("Enter student name ")
    age = input("Enter student age ")
    address = input("Enter student address ")

    sql = f"""
    INSERT INTO STUDENT (ID, NAME, AGE, ADDRESS) VALUES '{id}', '{name}'
    """
    print("Student added successfully !!")
    cont = input("Do you want to continue?(y/n) ")
    return True if cont.lower() == "y" else False
