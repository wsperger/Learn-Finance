import sqlite3

def get_IDs():
    # Connect to the database
    conn = sqlite3.connect('Financials.db')
    cursor = conn.cursor()

    # Query the Company_Allocation table to retrieve the unique id values
    cursor.execute("SELECT DISTINCT id FROM Company_Allocation")

    # Fetch all the rows of the result set
    rows = cursor.fetchall()

    # Create an empty array to store the id values
    id_values = []

    # Iterate through the rows and append the id value to the array
    for row in rows:
        id_values.append(row[0])

    # Close the connection to the database
    conn.close()

    # Return the array of id values
    return id_values