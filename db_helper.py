import mysql.connector


db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Mysql@88",
    "database": "classicmodels",
}

def get_customer_status(customer_name):
    # Replace these with your actual database credentials


    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(**db_config)

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Define the SQL query to retrieve the data based on customerName
        query = "SELECT * FROM customers WHERE customerName = %s"

        # Execute the query with the provided customer_name
        cursor.execute(query, (customer_name,))

        # Fetch the result (assuming there is only one row for the customer)
        result = cursor.fetchone()

        if result:
            # Extract the data from the result
            # CustNumber = result[0]
            data = result
            # print(f"Data for customer '{customer_name}': {data}")
            # print(f"Data for customer '{customer_name}': {CustNumber}")
            return data
        else:
            # print(f"No data found for customer '{customer_name}'")
            return "No data found for customer"
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    # Get customerName as input
    customer_name_input = input("Enter customerName: ")

    # Call the function with the provided customerName
    print(get_customer_status(customer_name_input))




def get_employees_status(employee_number):

    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(**db_config)

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Define the SQL query to retrieve the data based on customerName
        query = "SELECT * FROM employees WHERE employeeNumber = %s"

        # Execute the query with the provided customer_name
        cursor.execute(query, (employee_number,))

        # Fetch the result (assuming there is only one row for the customer)
        result = cursor.fetchone()

        if result:
            # Extract the data from the result
            # CustNumber = result[0]
            data = result
            # print(f"Data for customer '{customer_name}': {data}")
            # print(f"Data for customer '{customer_name}': {CustNumber}")
            return data
        else:
            # print(f"No data found for customer '{customer_name}'")
            return "No data found for employees"
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    # Get customerName as input
    employee_number = input("Enter employeeNumber: ")

    # Call the function with the provided customerName
    print(get_employees_status(employee_number))