import sqlite3
import random

def init_Goverment_Policies(db_path, macro, randomness, percentage_change, min_days_between_updates):
    # Connect to the database
    conn = sqlite3.connect(db_path)

    # Create a cursor
    cursor = conn.cursor()

    # Get the current maximum date in the income_statement table
    cursor.execute("SELECT MAX(date) FROM income_statement")
    current_max_date = cursor.fetchone()[0]

    # Iterate through the macro array
    for m in macro:
        # Select the last row for the current macro
        cursor.execute("SELECT * FROM Goverment_Policies WHERE Macro=? ORDER BY Date DESC LIMIT 1", (m,))
        last_row = cursor.fetchone()

        # If a row was found, check if the minimum number of days have passed since the last update
        if last_row:
            last_update_date = last_row[4]
            last_update_date = int(last_update_date)
            days_since_last_update = current_max_date - last_update_date
            if days_since_last_update >= min_days_between_updates:
                # Check if a new row should be inserted
                if random.random() < randomness:
                    # Use the values from the last row and apply the percentage change
                    tax_rate = last_row[1] * (1 + percentage_change)
                    interest_rates = last_row[2] * (1 + percentage_change)
                    risk_free_rate = last_row[3] * (1 + percentage_change)
                    date = current_max_date + 1

                    # Insert a new row into the Goverment_Policies table
                    cursor.execute("INSERT INTO Goverment_Policies (Macro, Tax_Rate, Interest_Rates, Risk_Free_Rate, Date) VALUES (?,?,?,?,?)", (m, tax_rate, interest_rates, risk_free_rate, date))
        # If no row was found, generate random values for the Tax_Rate, Interest_Rates, and Risk_Free_Rate columns
        else:
            tax_rate = random.uniform(0, 1)
            interest_rates = random.uniform(0, 1)
            risk_free_rate = random.uniform(0, 1)
            date = current_max_date + 1

            # Insert a new row into the Goverment_Policies table
            cursor.execute("INSERT INTO Goverment_Policies (Macro, Tax_Rate, Interest_Rates, Risk_Free_Rate, Date) VALUES (?,?,?,?,?)", (m, tax_rate, interest_rates, risk_free_rate, date))

    # Commit the transaction
    conn.commit()

    print("Policy evaluated")

    # Close the connection
    conn.close()