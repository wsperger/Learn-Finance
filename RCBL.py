import sqlite3
import GETIDs
import random


def calculate_balance_sheet(balance_sheet_date):
    # Connect to the database

    #print(balance_sheet_date)

    print("Balance_sheet")
    print(balance_sheet_date)

    conn = sqlite3.connect('Financials.db')
    cursor = conn.cursor()
    IDD = GETIDs.get_IDs()

    for i in IDD:
        #print("id "+ str(i))
        #print(balance_sheet_date - 1)

        # Query the balance_sheet table to retrieve the values for the current id and date
        query = "SELECT * FROM balance_sheet WHERE id = ? AND date = ?"
        #print(f"Query: {query}, Parameters: {(int(i), balance_sheet_date - 1)}")
        cursor.execute(query, (int(i), balance_sheet_date - 1))

        # Fetch the results
        results = cursor.fetchone()
        #print(results)

        # Query the income_statement table to retrieve the values for the current id and date
        query = "SELECT * FROM income_statement WHERE id = ? AND date = ?"
        cursor.execute(query, (int(i), balance_sheet_date - 1))

        # Fetch the results
        inc_sta_results = cursor.fetchone()

        print(inc_sta_results)

        inc_sta_id, inc_sta_date, inc_sta_revenue, inc_sta_cost_of_goods_sold, inc_sta_gross_profit, inc_sta_selling_and_administrative_expenses, inc_sta_operating_income, inc_sta_other_income_expense, inc_sta_net_income = inc_sta_results

        # Query the pnl table to retrieve the values for the current id and date
        query = "SELECT * FROM pnl WHERE id = ? AND date = ?"
        cursor.execute(query, (int(i), balance_sheet_date - 1))

        # Fetch the results
        pnl_results = cursor.fetchone()

        print(pnl_results)

        pnl_id, pnl_date, pnl_revenue, pnl_cost_of_goods_sold, pnl_gross_profit, pnl_selling_and_administrative_expenses, pnl_operating_income, pnl_other_income_expense, pnl_net_income = pnl_results

        # Unpack the results
        id, date, cash_and_cash_equivalents, accounts_receivable, inventories, investments, property_plant_equipment, intangible_assets, accounts_payable, notes_payable, accrued_expenses, common_stock, retained_earnings, total_assets, total_liabilities_equity = results

        n_cash = inc_sta_gross_profit + cash_and_cash_equivalents


        # Generate a random number between 0 and 9
        random_number = random.randint(0, 9)

        # If the random number is 0, we will transfer a random proportion of cash to n_investments
        if random_number == 0:
            # Generate a random proportion between 0 and 1
            random_proportion = random.uniform(0, 1)

            # Calculate the amount of cash to transfer
            cash_to_transfer = n_cash * random_proportion

            # Update n_cash and n_investments
            n_cash -= cash_to_transfer
            investments += cash_to_transfer

        n_investments = investments

        n_accounts_receivable = accounts_receivable
        n_inventories = inventories + 1

        n_property_plant_equipment = property_plant_equipment
        n_intangible_assets = intangible_assets
        n_accounts_payable = accounts_payable
        n_notes_payable = notes_payable
        n_accrued_expenses = accrued_expenses
        n_common_stock = common_stock
        n_retained_earnings = retained_earnings
        n_total_assets = total_assets
        n_total_liabilities_equity = total_liabilities_equity
        n_date = balance_sheet_date

        #Insert the calculated values into the balance_sheet table
        cursor.execute(
            '''INSERT INTO balance_sheet (date, id, cash_and_cash_equivalents, accounts_receivable, inventories, investments, property_plant_equipment, intangible_assets, accounts_payable, notes_payable, accrued_expenses, common_stock, retained_earnings, total_assets, total_liabilities_equity) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?, ?)''',
            (n_date, i, n_cash, n_accounts_receivable, n_inventories, n_investments, n_property_plant_equipment,
             n_intangible_assets, n_accounts_payable, n_notes_payable, n_accrued_expenses, n_common_stock,
             n_retained_earnings,
             n_total_assets, n_total_liabilities_equity))

        # Commit the changes to the database
        conn.commit()