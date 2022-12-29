import sqlite3
import GETIDs

def calculate_pnl(pnl_date):
    # Connect to the database
    conn = sqlite3.connect('Financials.db')
    cursor = conn.cursor()
    IDD = GETIDs.get_IDs()

    print("PNL")
    print(pnl_date)

    for i in IDD:
        #print("id "+ str(i))
        #print(pnl_date - 1)

        # Query the pnl table to retrieve the values for the current id and date
        query = "SELECT * FROM pnl WHERE id = ? AND date = ?"
        #print(f"Query: {query}, Parameters: {(int(i), pnl_date - 1)}")
        cursor.execute(query, (int(i), pnl_date - 1))

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
        n_date = pnl_date

        # Insert the calculated values into the pnl table
        cursor.execute(
            '''INSERT INTO pnl (date, id, revenue, cost_of_goods_sold, gross_profit, selling_and_administrative_expenses, operating_income, other_income_expense, net_income) VALUES (?,?,?,?,?,?,?,?,?)''',
            (n_date, i, n_revenue, n_cost_of_goods_sold, n_gross_profit, n_selling_and_administrative_expenses,
             n_operating_income, n_other_income_expense, n_net_income))

        # Commit the changes to the database
        conn.commit()
