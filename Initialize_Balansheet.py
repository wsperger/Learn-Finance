import sqlite3
import GETIDs
import time


# I know, completly unnecessary to have a loop, i just modified the RC calculations for the setup, will optimize at a later point
def insert_balance_sheet_data(num_days):
    # Connect to the database
    conn = sqlite3.connect('Financials.db')
    cursor = conn.cursor()

    IDD = GETIDs.get_IDs()

    for day in range(num_days):
        time.sleep(0.1)
        for i in IDD:
            id = i
            date = day
            cash_and_cash_equivalents = 1000
            accounts_receivable = 500
            inventories = 250
            investments = 1500
            property_plant_equipment = 2000
            intangible_assets = 1000
            accounts_payable = 250
            notes_payable = 500
            accrued_expenses = 100
            common_stock = 1000
            retained_earnings = 500
            total_assets = cash_and_cash_equivalents + accounts_receivable + inventories + investments + property_plant_equipment + intangible_assets
            total_liabilities_equity = accounts_payable + notes_payable + accrued_expenses + common_stock + retained_earnings

            # Insert the values into the balance_sheet table
            cursor.execute('''INSERT INTO balance_sheet (id, date, cash_and_cash_equivalents, accounts_receivable, inventories, investments, property_plant_equipment, intangible_assets, accounts_payable, notes_payable, accrued_expenses, common_stock, retained_earnings, total_assets, total_liabilities_equity) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (id, date, cash_and_cash_equivalents, accounts_receivable, inventories, investments, property_plant_equipment, intangible_assets, accounts_payable, notes_payable, accrued_expenses, common_stock, retained_earnings, total_assets, total_liabilities_equity))
        # Commit the changes to the database after inserting data for all IDs on the current day
        conn.commit()
    cursor.close()