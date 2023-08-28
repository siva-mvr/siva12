import mysql.connector

# Database configuration
#Connect to the database
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='mvr',
        user='root',
        password='root'
    )
    
    if conn.is_connected():
        print("Connected to the database!")
        cursor = conn.cursor()
        
        # Execute queries here
        # Retrieve data from the table
        cursor.execute('SELECT * FROM student')
        data = cursor.fetchall()

        for row in data:
            print(row)

        conn.close()
        print("Connection closed.")
except mysql.connector.Error as e:
    print("Error:", e)

