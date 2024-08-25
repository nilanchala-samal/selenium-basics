import mysql.connector as db

insert_query = "insert into employees(id, first_name, last_name, email_id) values(3, 'Somya', 'Mohanty', 'somyamohanty@gmail.com')"
update_query = "update employees set first_name='Pupun' where id=3"
delete_query = "delete from employees where first_name='Pupun'"

try:
    conn = db.connect(host="localhost", port=3306, user="root", passwd="root", database="ems")
    cursor = conn.cursor()
    # cursor.execute(insert_query)
    # cursor.execute(update_query)
    cursor.execute(delete_query)
    conn.commit()
    conn.close()
except:
    print("Unsuccessful connection. Cannot connect to the database...")

print("Finished...")
