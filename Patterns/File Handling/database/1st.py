import pymysql
con = pymysql.connect(host = 'localhost',user='root',password='M1racle@123',database='books')
cur = con.cursor()

query = "DELETE FROM book_id WHERE id = %s"

cur.execute(query, (2,))

if cur.rowcount > 0:
    print("Record deleted successfully!")
    cur.execute("SELECT * FROM book_id")
    data = cur.fetchall()

    for row in data:
        print(row)
else:
    print("No matching record was found!")

con.commit()

cur.close()
con.close()