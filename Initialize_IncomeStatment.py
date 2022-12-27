import sqlite3
import GETIDs
import time


def insert_income_statement_data(num_days):
    # Connect to the database
    conn = sqlite3.connect('Financials.db')
    cursor = conn.cursor()

    IDD = GETIDs.get_IDs()

    for day in range(num_days):
        time.sleep(0.1)
        for i in IDD:
            id = i
            date = day
            revenue = 1000
            cost_of_goods_sold = 500
            gross_profit = revenue - cost_of_goods_sold
            selling_and_administrative_expenses = 250
            operating_income = gross_profit - selling_and_administrative_expenses
            other_income_expense = 100
            net_income = operating_income + other_income_expense

            # Insert the values into the income_statement table
            cursor.execute('''INSERT INTO income_statement (id, date, revenue, cost_of_goods_sold, gross_profit, selling_and_administrative_expenses, operating_income, other_income_expense, net_income) VALUES (?,?,?,?,?,?,?,?,?)''', (id, date, revenue, cost_of_goods_sold, gross_profit, selling_and_administrative_expenses, operating_income, other_income_expense, net_income))
        # Commit the changes to the database after inserting data for all IDs on the current day
        conn.commit()
    cursor.close()