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

    # Executing a SELECT query to fetch data from the 'users' table
    query = "SELECT * FROM Student"
    cursor.execute(query)

    # Fetching all the rows from the executed query
    rows = cursor.fetchall()

    # Displaying the fetched data
    for row in rows:
        print(f"Roll No: {row[0]}, First Name: {row[1]}, Last Name: {row[2]}, Address: {row[3]}")

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")
finally:
    # Close the connection at the end
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print('MySQL connection closed')
