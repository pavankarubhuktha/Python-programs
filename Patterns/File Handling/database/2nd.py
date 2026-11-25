
import pymysql

con = pymysql.connect(
    host='localhost',
    user='root',
    password='M1racle@123',
    database='student'
)

cur = con.cursor()

name = input("Enter student name: ")

query = "SELECT * FROM student_info WHERE name = %s"

cur.execute(query, (name,))

data = cur.fetchall()

if len(data) > 0:
    print("Student record found!")

    for row in data:
        print("ID:", row[0])
        print("Name:", row[1])
        print("Course:", row[2])
        print("Marks:", row[3])
else:
    print("No matching student record found!")

cur.close()
con.close()
