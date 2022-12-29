import sqlite3
import GETIDs

conn = sqlite3.connect('Financials.db')
cursor = conn.cursor()
IDD = GETIDs.get_IDs()



# print("id "+ str(i))
# print(income_statement_date - 1)

# Query the income_statement table to retrieve the values for the current id and date
query = "SELECT * FROM income_statement WHERE id = 1 AND date = 1"
# print(f"Query: {query}, Parameters: {(int(i), income_statement_date - 1)}")
cursor.execute(query)

# Fetch the results
results = cursor.fetchone()
print(results)