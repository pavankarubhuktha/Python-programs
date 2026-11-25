from idlelib import query

import pymysql

con = pymysql.connect(host='localhost', user='root', password='M1racle@123', database='student')
cur = con.cursor()
d = input("enter:")
if d.lower() == "f":
    n = int(input("enter no of student to add:"))
    record=[]
    for i in range(n):
        print("\n enter the values of student",i+1)
        id = int(input("enter id:"))
        name = input("enter name:")
        course = input("enter")
        marks = int(input("enter marks"))
        record.append((id,name,course,marks))
    query = """
    insert into student_info (id,name,course,marks) values(%s,%s,%s,%s)
    """
    cur.executemany(query,record)
    con.commit()
    print("\n compleated")
else:
    print("\n fail")
cur.close()
con.close()
