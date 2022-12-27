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

            con.execute('''CREATE TABLE IF NOT EXISTS income_statement (
                                id TEXT PRIMARY KEY,
                                date integer,
                                revenue REAL NOT NULL,
                                cost_of_goods_sold REAL NOT NULL,
                                gross_profit REAL NOT NULL,
                                selling_and_administrative_expenses REAL NOT NULL,
                                operating_income REAL NOT NULL,
                                other_income_expense REAL NOT NULL,
                                net_income REAL NOT NULL
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
                        total_liabilities_equity REAL NOT NULL
                        )''')
        con.execute('''CREATE TABLE IF NOT EXISTS pnl (
                        id TEXT PRIMARY KEY,
                        date integer,
                        revenue REAL NOT NULL,
                        cost_of_goods_sold REAL NOT NULL,
                        gross_profit REAL NOT NULL,
                        selling_and_administrative_expenses REAL NOT NULL,
                        operating_income REAL NOT NULL,
                        other_income_expense REAL NOT NULL,
                        net_income REAL NOT NULL
                        )''')
        con.execute('''CREATE TABLE cost_of_goods_sold (
                               id TEXT PRIMARY KEY,
                               date integer,
                               product_name text,
                               quantity integer,
                               unit_cost real,
                               total_cost real
                               )''')
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