import csv
from day21.estd_connection import estd_connection

filename = "students.csv"

cursor = estd_connection()


with open(filename, "r") as cr:
    rows = csv.DictReader(cr)
    for each in rows:
        id = each["id"]
        name = each["name"]
        age = each["age"]
        address = each["address"]

        sql = f"""
        INSERT INTO STUDENT (ID, NAME, AGE, ADDRESS) values ('{id}', '{name}', '{age}', '{address}')
        """
        cursor.execute(sql)
        print("Student added successfully !")
