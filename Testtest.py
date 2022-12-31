import sqlite3

def select_from_table(table_name, columns, where=None):
  """
  Retrieves rows from a table in a SQLite database.
  :param table_name: The name of the table.
  :param columns: A list of columns to select.
  :param where: An optional dictionary of column names and values to use as a WHERE clause.
  :return: A list of rows, where each row is a dictionary mapping column names to values.
  """
  con = sqlite3.connect('Financials.db')
  cursor = con.cursor()

  query = 'SELECT {} FROM {}'.format(', '.join(columns), table_name)
  if where:
    query += ' WHERE {}'.format(' AND '.join(['{}=?'.format(k) for k in where.keys()]))
  cursor.execute(query, list(where.values()))

  rows = cursor.fetchall()
  con.close()
  return rows

def insert_into_table(table_name, values):
  """
  Inserts a new row into a table in a SQLite database.
  :param table_name: The name of the table.
  :param values: A dictionary mapping column names to values.
  """
  con = sqlite3.connect('Financials.db')
  cursor = con.cursor()

  query = 'INSERT INTO {} ({}) VALUES ({})'.format(table_name, ', '.join(values.keys()), ', '.join(['?'] * len(values)))
  cursor.execute(query, list(values.values()))
  con.commit()
  con.close()

def update_table(table_name, updates, where=None):
  #"""
  #Updates rows in a table in a SQLite database.
  #:param table_name: The name of the table.
  #:param updates: A dictionary mapping column names to update expressions.
  #:param where: An optional dictionary of column names and values to use as a WHERE clause.
  #"""
  con = sqlite3.connect('Financials.db')
  cursor = con.cursor()

  query = 'UPDATE {} SET {}'.format(table_name, ', '.join(['{}={}'.format(k, v) for k, v in updates.items()]))
  if where:
    query += ' WHERE {}'.format(' AND '.join(['{}=?'.format(k) for k in where.keys()]))
  cursor.execute(query, list(where.values()))
  con.commit()
  con.close()


def take_out_loan(company_id, loan_amount, loan_term, date):
  # Retrieve the macro of the company
  company = select_from_table('Company_Allocation', ['country'], where={'id': company_id})
  if not company:
    print("Error: No such company found")
    return
  company_macro = company[0]['country']

  # Retrieve the interest rate for the company's macro and the given date
  interest_rate = select_from_table('government_policies', ['interest_rate'], where={'macro': company_macro, 'date': date})
  if not interest_rate:
    print("Error: No interest rate found for the given macro and date")
    return
  interest_rate = interest_rate[0]['interest_rate']

  # Calculate the total interest expense for the loan
  total_interest_expense = loan_amount * interest_rate * loan_term

  # Insert the loan details into the loans table
  insert_into_table('loans', {'company_id': company_id, 'amount': loan_amount, 'term': loan_term, 'interest_rate': interest_rate, 'total_interest_expense': total_interest_expense, 'date': date})

  # Update the company's debt and interest expense in the company_financials table
  update_table('balance_sheet', {'debt': 'debt + {}'.format(loan_amount), 'interest_expense': 'interest_expense + {}'.format(total_interest_expense)}, where={'company_id': company_id, 'date': date})

take_out_loan(1, 999999999, 1, 1)