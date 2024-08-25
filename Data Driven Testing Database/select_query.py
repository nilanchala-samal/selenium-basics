import mysql.connector as db

try:
    conn = db.connect(host="localhost", port=3306, user="root", passwd="root", db="ems")
    cursor = conn.cursor()
    cursor.execute("SELECT id, first_name, last_name, email_id FROM employees")
    print(cursor)
    print(type(cursor))

    for row in cursor:
        print(row[0], '===>', row[1], '===>', row[2], '===>', row[3])
    conn.close()
except:
    print("Connection unsuccessful...")

print("Finished...")
