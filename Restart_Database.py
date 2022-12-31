import sqlite3 as sl

def reset_tables(db_name):
    con = sl.connect(db_name)

    # Get a list of all the tables in the database
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Loop through each table and drop it
    for table in tables:
        table_name = table[0]
        con.execute(f"DROP TABLE {table_name};")

    # Recreate the tables as empty tables
    with con:
        with con:
            con.execute('''CREATE TABLE IF NOT EXISTS Company_Allocation (
                              id INTEGER PRIMARY KEY, 
                              country TEXT, 
                              industry TEXT, 
                              product TEXT
                              )''')

            con.execute('''CREATE TABLE IF NOT EXISTS insolvency_status (
                            id TEXT,
                            is_insolvent INTEGER NOT NULL,
                            date INTEGER NOT NULL,
                            PRIMARY KEY (id, date)
                            )''')

            cursor.execute(
                "CREATE TABLE IF NOT EXISTS macro (id TEXT, y_values REAL, y_value_derivative, x_values REAL)")
            cursor.execute("CREATE TABLE IF NOT EXISTS micro (id TEXT, y_values REAL, x_values REAL)")
            cursor.execute("CREATE TABLE IF NOT EXISTS product (id TEXT, y_values REAL, x_values REAL)")

            con.execute('''CREATE TABLE IF NOT EXISTS income_statement (
                                            id TEXT,
                                            date integer,
                                            revenue REAL NOT NULL,
                                            cost_of_goods_sold REAL NOT NULL,
                                            gross_profit REAL NOT NULL,
                                            selling_and_administrative_expenses REAL NOT NULL,
                                            operating_income REAL NOT NULL,
                                            other_income_expense REAL NOT NULL,
                                            net_income REAL NOT NULL,
                                            PRIMARY KEY (id, date)
                                            )''')
        con.execute('''CREATE TABLE IF NOT EXISTS balance_sheet (
                        id integer,
                        date integer,
                        cash_and_cash_equivalents REAL NOT NULL,
                        accounts_receivable REAL NOT NULL,
                        inventories REAL NOT NULL,
                        investments REAL NOT NULL,
                        property_plant_equipment REAL NOT NULL,
                        intangible_assets REAL NOT NULL,
                        accounts_payable REAL NOT NULL,
                        notes_payable REAL NOT NULL,
                        accrued_expenses REAL NOT NULL,
                        common_stock REAL NOT NULL,
                        retained_earnings REAL NOT NULL,
                        total_assets REAL NOT NULL,
                        total_liabilities_equity REAL NOT NULL,
                        FOREIGN KEY (id) REFERENCES Company_Allocation(id)
                        PRIMARY KEY (id, date)
                        )''')
        con.execute('''CREATE TABLE IF NOT EXISTS pnl (
                        id TEXT,
                        date integer,
                        revenue REAL NOT NULL,
                        cost_of_goods_sold REAL NOT NULL,
                        gross_profit REAL NOT NULL,
                        selling_and_administrative_expenses REAL NOT NULL,
                        operating_income REAL NOT NULL,
                        other_income_expense REAL NOT NULL,
                        net_income REAL NOT NULL,
                        FOREIGN KEY (id) REFERENCES Company_Allocation(id)
                        PRIMARY KEY (id, date)
                        )''')
        cursor.execute('''
          CREATE TABLE loans (
            id INTEGER PRIMARY KEY,
            company_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            term INTEGER NOT NULL,
            interest_rate REAL NOT NULL,
            total_interest_expense REAL NOT NULL,
            date INTEGER NOT NULL,
            FOREIGN KEY (company_id) REFERENCES companies(id)
          );
        ''')

        con.execute("""
                    CREATE TABLE Goverment_Policies (
                        Macro TEXT,
                        Tax_Rate float,
                        Interest_Rates float,
                        Risk_Free_Rate float,
                        Date integer
                    );
                """)


# Example usage: reset all tables in the "Financials.db" database
reset_tables("Financials.db")