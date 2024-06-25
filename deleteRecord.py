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

    # Update query parameters
    roll_no = 1  # Update user with ID 1


    # MySQL UPDATE statement to update the email of a specific user
    update_query = "DELETE from Student WHERE roll_no = %s"
    update_data = (roll_no,)

    # Executing the update query
    cursor.execute(update_query, update_data)

    # Committing the changes to the database
    connection.commit()

    # Check if any rows were affected
    if cursor.rowcount > 0:
        print("Record deleted successfully.")
    else:
        print("No record found for the provided Roll no.")
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")
finally:
    # Close the connection at the end
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print('MySQL connection closed')
