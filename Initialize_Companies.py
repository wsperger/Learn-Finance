import itertools
import sqlite3

def generate_and_store_objects(countries, industries, products, num_companies_per_product, db_name):
    objects = []
    object_id = 0

    for country, industry, product in itertools.product(countries, industries, products):
        for i in range(num_companies_per_product):
            obj = {"id": object_id, "country": country, "industry": industry, "product": product}
            objects.append(obj)
            object_id += 1

    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Company_Allocation (id INTEGER, country TEXT, industry TEXT, product TEXT)")
    for obj in objects:
        c.execute("INSERT INTO Company_Allocation VALUES (?, ?, ?, ?)", (obj["id"], obj["country"], obj["industry"], obj["product"]))
    conn.commit()
    conn.close()

# Example usage
#generate_and_store_objects(["USA", "Canada", "Mexico"], ["Technology", "Finance", "Retail"], ["Computer", "Phone", "Tablet"], 100, "Financials.db")