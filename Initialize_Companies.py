import itertools
import sqlite3

class Dataset:
    def __init__(self, countries, industries, products, num_companies_per_product):
        self.countries = countries
        self.industries = industries
        self.products = products
        self.num_companies_per_product = num_companies_per_product
        self.objects = []
        self.object_id = 0

    def generate_objects(self):
        for country, industry, product in itertools.product(self.countries, self.industries, self.products):
            for i in range(self.num_companies_per_product):
                obj = {"id": self.object_id, "country": country, "industry": industry, "product": product}
                self.objects.append(obj)
                self.object_id += 1

    def store_objects_in_database(self, db_name):
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS Company_Allocation (id INTEGER, country TEXT, industry TEXT, product TEXT)")
        for obj in self.objects:
            c.execute("INSERT INTO Company_Allocation VALUES (?, ?, ?, ?)", (obj["id"], obj["country"], obj["industry"], obj["product"]))
        conn.commit()
        conn.close()

# Example usage
dataset = Dataset(["USA", "Canada", "Mexico"], ["Technology", "Finance", "Retail"], ["Computer", "Phone", "Tablet"], 100)
dataset.generate_objects()
dataset.store_objects_in_database("Financials.db")
