#pip install mysql-connector-python
import mysql.connector
import databaseSetting as db
# Establishing a connection to the MySQL database


try:
    # Replace the placeholders with your actual database credentials
    connection = mysql.connector.connect(
        host=db.HOST,  # 'localhost',
        user=db.USER,  # 'root',
        password=db.PASSWORD,
        database=db.DATABASE  # 'stud'
    )

    if connection.is_connected():
        print('Connected to MySQL database')
    cursor = connection.cursor()
    userdata = [
        (1, 'Sachin', 'Tendulkar', 'Mumbai'),

    ]
    add_userdata_quey = "insert into Student (roll_no, frist_name,last_name,address) values(%s,%s,%s,%s)"
    cursor.executemany(add_userdata_quey, userdata)
    connection.commit()
    print(cursor.rowcount, " records inserted.")
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")
finally:
    # Close the connection at the end
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print('MySQL connection closed')
