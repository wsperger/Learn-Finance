import sqlite3
import GETIDs

def calculate_income_statement(income_statement_date):
    # Connect to the database
    conn = sqlite3.connect('Financials.db')
    cursor = conn.cursor()
    IDD = GETIDs.get_IDs()

    print("Income Statement")
    print(income_statement_date)

    for i in IDD:
        #print("id "+ str(i))
        #print(income_statement_date - 1)

        # Query the income_statement table to retrieve the values for the current id and date
        query = "SELECT * FROM income_statement WHERE id = ? AND date = ?"
        #print(f"Query: {query}, Parameters: {(int(i), income_statement_date - 1)}")
        cursor.execute(query, (int(i), income_statement_date - 1))

        # Fetch the results
        results = cursor.fetchone()
        #print(results)

        # Unpack the results
        id, date, revenue, cost_of_goods_sold, gross_profit, selling_and_administrative_expenses, operating_income, other_income_expense, net_income = results

        n_revenue = revenue
        n_cost_of_goods_sold = cost_of_goods_sold + 1
        n_gross_profit = gross_profit
        n_selling_and_administrative_expenses = selling_and_administrative_expenses
        n_operating_income = operating_income
        n_other_income_expense = other_income_expense
        n_net_income = net_income
        n_date = income_statement_date

        # Insert the calculated values into the income_statement table
        cursor.execute(
            '''INSERT INTO income_statement (date, id, revenue, cost_of_goods_sold, gross_profit, selling_and_administrative_expenses, operating_income, other_income_expense, net_income) VALUES (?,?,?,?,?,?,?,?,?)''',
            (n_date, i, n_revenue, n_cost_of_goods_sold, n_gross_profit, n_selling_and_administrative_expenses,
             n_operating_income, n_other_income_expense, n_net_income))

        # Commit the changes to the database
        conn.commit()
