from pickle import GLOBAL

import mysql.connector
global mydb
# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="pandeyji_eatery"
)

def get_order_status(order_id: int):
        # Create a cursor object
        mycursor = mydb.cursor()

        # Execute the SQL query to retrieve the order status
        sql = "SELECT status FROM order_tracking WHERE order_ID = %s"
        val = (order_id,)
        mycursor.execute(sql, val)

        # Fetch the result
        result = mycursor.fetchone()

        # Close the database connection
        mycursor.close()

        if result:
            return result[0]
        else:
            return None



