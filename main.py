import Restart_Database
import Initialize_Companies
import Initialize_Balansheet
import Initialize_IncomeStatment
import Initialize_PnL
import Define_Curves

num_days = 12

#Reset the database for a fresh start
Restart_Database.reset_tables("Financials.db")

print("Database restarted")

# Define a class for companies so we have a vessel in which to ship the data to the SQLite database
class Dataset:
    def __init__(self, countries, industries, products, num_companies_per_product):
        self.countries = countries
        self.industries = industries
        self.products = products
        self.num_companies_per_product = num_companies_per_product
        self.objects = []
        self.object_id = 0

Dataset(["USA", "Canada", "Mexico"], ["Technology", "Finance", "Retail"], ["Computer", "Phone", "Tablet"], 100)
Initialize_Companies.dataset.generate_objects()

print("Objects Generated")

Initialize_Companies.dataset.store_objects_in_database("Financials.db")

print("Objects are stored in the database")

#Because I want to simulate these companies at a deep level, i will be simulating all of their financial statements on a daily basis
#Therefore, in the next three steps, i will be initializing these statements with some starter values
    #It is planned to modify the functions in the future so that we can determine these starting values as well
Initialize_Balansheet.insert_balance_sheet_data(1)

print("Balance Sheets are initialized")

Initialize_IncomeStatment.insert_income_statement_data(1)

print("Income Statements are initialized")

Initialize_PnL.insert_pnl_data(1)

print("P&Ls are initialized")

#Here we generate three major types of curves. Macro curves representing an economies GDP, a micro curve representing a microeconomic sector within an economy,
# and a product curve representing the demand for a product nested within the previous curves.
    #It should be noted that here we don't generated one curve for each type, but several so that we can simulate the demand for multiple products for example within an economy.
    #It is planned to modify the function to enable control of variables within the function from outside

Define_Curves.generate_market_curves()

print("Curves are defined")

#Upcoming: Implementing functions that calculate daily for every company the financial statements. This is the part where the company can adjust variables in order to achive better performance.
# The functions are mainly done, but the heart is missing. That would be the part where we identify what variables should be changeable, by how much and what else should the company be
#able to change. 
    #In the end, it is planned to implant a neural network into that function that through self play learns how to adjust to several scenarious and run a company most efficiently.
    #In this part help would be greatly appreciated.































