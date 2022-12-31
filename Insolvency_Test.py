def check_insolvency(con, company_id, date):
    # Retrieve the balance sheet and income statement for the given company and date
    balance_sheet_query = '''SELECT * FROM balance_sheet WHERE id=? AND date=?'''
    balance_sheet = con.execute(balance_sheet_query, (company_id, date)).fetchone()

    income_statement_query = '''SELECT * FROM income_statement WHERE id=? AND date=?'''
    income_statement = con.execute(income_statement_query, (company_id, date)).fetchone()

    # If either the balance sheet or income statement is not available, return None
    if balance_sheet is None or income_statement is None:
        return None

    # Extract the relevant values from the balance sheet and income statement
    total_assets = balance_sheet['total_assets']
    total_liabilities_equity = balance_sheet['total_liabilities_equity']
    net_income = income_statement['net_income']

    # Determine if the company is insolvent
    is_insolvent = False
    if total_assets < total_liabilities_equity:
        is_insolvent = True
    elif net_income < 0 and abs(net_income) < deficit:
        is_insolvent = True
    elif net_income > 0 and net_income < deficit:
        is_insolvent = True

    # Insert the data into the appropriate table
    insert_query = '''INSERT INTO insolvency_status (id, is_insolvent, date) VALUES (?, ?, ?)'''
    con.execute(insert_query, (company_id, is_insolvent, date))
    con.commit()

    # Return the insolvency status
    return is_insolvent
