import mysql.connector

# MySQL database configuration
db_config = {
    "host": "localhost",    # Replace with your MySQL server host
    "user": "root",         # Replace with your MySQL username
    "password": "root",         # Replace with your MySQL password (leave empty if no password)
    "database": "sakila",   # Replace with the name of your MySQL database (e.g., Sakila)
}

try:
    # Connect to the MySQL server
    connection = mysql.connector.connect(**db_config)

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Example query: Select all records from a table (e.g., actor)
    table_name = "actor"
    query = f"SELECT * FROM {table_name}"

    # Execute the query
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Print the results
    print(f"Results from '{table_name}' table:")
    for row in rows:
        print(row)

except mysql.connector.Error as e:
    print(f"Error in connection: {e}")

finally:
    # Close the cursor and connection
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed.")
