import sqlite3

def select_from_table(table_name, columns, where=None):
  """
  Retrieves rows from a table in a SQLite database.
  :param table_name: The name of the table.
  :param columns: A list of columns to select.
  :param where: An optional dictionary of column names and values to use as a WHERE clause.
  :return: A list of rows, where each row is a dictionary mapping column names to values.
  """
  con = sqlite3.connect('database.db')
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
  con = sqlite3.connect('database.db')
  cursor = con.cursor()

  query = 'INSERT INTO {} ({}) VALUES ({})'.format(table_name, ', '.join(values.keys()), ', '.join(['?'] * len(values)))
  cursor.execute(query, list(values.values()))
  con.commit()
  con.close()

def update_table(table_name, updates, where=None):
  """
  Updates rows in a table in a SQLite database.
  :param table_name: The name of the table.
  :param updates: A dictionary mapping column names to update expressions.
  :param where: An optional dictionary of column names and values to use as a WHERE clause.
  """
  con = sqlite3.connect('database.db')
  cursor = con.cursor()

  query = 'UPDATE {} SET {}'.format(table_name, ', '.join(['{}={}'.format(k, v) for k, v in updates.items()]))
  if where:
    query += ' WHERE {}'.format(' AND '.join(['{}=?'.format(k) for k in where.keys()]))
  cursor.execute(query, list(where.values()))
  con.commit()
  con.close()
