import sqlite3


def Offer_Ranking(market_size, db_path):
  # Connect to the database and retrieve the offers
  conn = sqlite3.connect(db_path)
  cursor = conn.cursor()
  cursor.execute('''
    SELECT company_id, price
    FROM marketsharetracking
    WHERE date = (SELECT MAX(date) FROM marketsharetracking WHERE company_id = marketsharetracking.company_id)
  ''')
  offers = cursor.fetchall()

  # Sort the offers by price in ascending order
  offers.sort(key=lambda x: x[1])

  # Initialize an empty list to store the ranked offers
  ranked_offers = []

  # Iterate through the sorted offers and add them to the ranked list
  total_price = 0
  for offer in offers:
    company_id, price = offer
    #print(offer)
    if total_price + price > market_size:
      break
    ranked_offers.append(offer)
    total_price += price

  # Return an empty list if the ranked offers list is empty
  if not ranked_offers:
    return []

  print(ranked_offers)
  return ranked_offers

Offer_Ranking(100, 'Financials.db')