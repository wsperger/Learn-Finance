import sqlite3
import random

def init_Goverment_Policies(db_path, macro):
    # Connect to the database
    conn = sqlite3.connect(db_path)

    # Create a cursor
    cursor = conn.cursor()

    # Iterate through the macro array
    for m in macro:
        # Generate random values for the Tax_Rate, Interest_Rates, and Risk_Free_Rate columns
        tax_rate = random.uniform(0, 1)
        interest_rates = random.uniform(0, 1)
        risk_free_rate = random.uniform(0, 1)
        Date = 0

        # Insert a new row into the Goverment_Policies table
        cursor.execute("INSERT INTO Goverment_Policies (Macro, Tax_Rate, Interest_Rates, Risk_Free_Rate, Date) VALUES (?,?,?,?,?)", (m, tax_rate, interest_rates, risk_free_rate, Date))

    # Commit the transaction
    conn.commit()

    # Close the connection
    conn.close()