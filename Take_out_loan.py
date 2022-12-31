def take_out_loan(company_id, loan_amount, loan_term, date):
  # Retrieve the macro of the company
  company_macro = select_from_table('companies', ['macro'], where={'id': company_id})[0]['macro']

  # Retrieve the interest rate for the company's macro and the given date
  interest_rate = select_from_table('government_policies', ['interest_rate'], where={'macro': company_macro, 'date': date})[0]['interest_rate']

  # Calculate the total interest expense for the loan
  total_interest_expense = loan_amount * interest_rate * loan_term

  # Insert the loan details into the loans table
  insert_into_table('loans', {'company_id': company_id, 'amount': loan_amount, 'term': loan_term, 'interest_rate': interest_rate, 'total_interest_expense': total_interest_expense, 'date': date})

  # Update the company's debt and interest expense in the company_financials table
  update_table('company_financials', {'debt': 'debt + {}'.format(loan_amount), 'interest_expense': 'interest_expense + {}'.format(total_interest_expense)}, where={'company_id': company_id, 'date': date})