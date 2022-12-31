import random
import sqlite3
import GETIDs

def generate_market_shares_and_insert_into_database(company_ids, database_path):
    def generate_market_shares(company_ids):
        # Initialize the table
        table = []

        # Generate market share values for each company
        market_share_sum = 1
        for company_id in company_ids:
            market_share = random.uniform(0, 1)
            market_share_sum += market_share
            table.append({'company_id': company_id, 'marketshare': market_share, 'date': 0})

        # Normalize the market share values so that they add up to 1
        for row in table:
            row['marketshare'] /= market_share_sum

        # Make sure that the sum of market share values is exactly 1
        market_share_sum = sum(row['marketshare'] for row in table)
        diff = 1 - market_share_sum
        if diff > 0:
            # If the sum is less than 1, increase the market share of the first company
            table[0]['marketshare'] += diff
        elif diff < 0:
            # If the sum is greater than 1, decrease the market share of the first company
            table[0]['marketshare'] += diff

        return table

    # Connect to the database
    conn = sqlite3.connect(database_path)

    # Create the table (if it doesn't already exist)
    conn.execute("CREATE TABLE IF NOT EXISTS marketsharetracking (company_id TEXT, price REAL,marketshare REAL, date INTEGER)")

    # Insert the data into the table
    table = generate_market_shares(company_ids)
    for row in table:
        conn.execute("INSERT INTO marketsharetracking (company_id, price, marketshare, date) VALUES (?, ?, ?, ?)", (row['company_id'], random.uniform(1, 100), row['marketshare'], row['date']))
    # Save the changes and close the connection
    conn.commit()
    conn.close()

# Test the function
generate_market_shares_and_insert_into_database(GETIDs.get_IDs(), 'Financials.db')