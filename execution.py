import Restart_Database
import Initialize_Companies
import Initialize_Balansheet
import Initialize_IncomeStatment
import Initialize_PnL
import Define_Curves
import Insert_Goverment_Policy
import numpy as np
import RCBL
import RC_Income_ST
import RC_PNL
import random

#Initializing Variables
#countries = ["eda", "fds", "afds"]
#industries = ["Technology", "Finance", "Retail"]
#products = ["Computer", "Phone", "Tablet"]

countries = ["eda", "asdasd", "dasda"]
industries = ["Technology", "Farming", "Cars"]
products = ["Computer", "Tractors", "Car"]


# Declare variables with random values

#For how many days should the simulation run
num_days = 3
#this carries the num_days values, but it is converted to an array so it can be ingested by the financial calculation functions further down the line
a = []

for i in range(1, num_days+1):
    a.append(i)

#This is just a conversion of variable names to fit into the different function. This should be normalized in the future.
macro = countries
micro = industries
product = products

#This determines how many companies are established per product
companies_per_product = 7

#This block of variables is used to generate the macro, micro and product curves. They determine the overall demand for all products over time
id_ma = random.randint(1, 100)
id_mi = random.randint(1, 100)
id_po = random.randint(1, 100)
Temp_Micro_Value = 1/len(micro)
Temp_Product_Value = 1/len(product)
macro_ampl_slider = random.uniform(0, 10)
macro_growth_factor_slider = random.uniform(0, 1)
macro_freq_slider = random.uniform(0, 1)
Micro_Amplitude_slider = random.uniform(0, 10)
Micro_Growth_Factor_slider = random.uniform(0, 1)
Micro_Frequency_slider = random.uniform(0, 1)
Product_Amplitude_slider = random.uniform(0, 10)
Product_Growth_Factor_slider = random.uniform(0, 1)
Product_Frequency_slider = random.uniform(0, 1)


#Establish the balance sheet starter values
cash_and_cash_equivalents = 3200
accounts_receivable = 5003
inventories = 2350
investments = 122500
property_plant_equipment = 12000
intangible_assets = 1000
accounts_payable = 250
notes_payable = 500
accrued_expenses = 100
common_stock = 1000
retained_earnings = 500

#Initialize Income Statement
revenue = 654
cost_of_goods_sold = 500

selling_and_administrative_expenses = 250

other_income_expense = 100



randomness = 0.9
percentage_change = 0.1
min_days_between_updates = 1

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

Initialize_Companies.generate_and_store_objects(countries, industries, products, companies_per_product, "Financials.db")

print("Objects are stored in the database")

#Because I want to simulate these companies at a deep level, i will be simulating all of their financial statements on a daily basis
#Therefore, in the next three steps, i will be initializing these statements with some starter values
    #It is planned to modify the functions in the future so that we can determine these starting values as well
Initialize_Balansheet.insert_balance_sheet_data(cash_and_cash_equivalents, accounts_receivable, inventories, investments, property_plant_equipment, intangible_assets, accounts_payable, notes_payable, accrued_expenses, common_stock, retained_earnings)

print("Balance Sheets are initialized")

Initialize_IncomeStatment.insert_income_statement_data(num_days, revenue, cost_of_goods_sold, selling_and_administrative_expenses, other_income_expense)

print("Income Statements are initialized")

Initialize_PnL.insert_pnl_data(1)

print("P&Ls are initialized")

#Here we generate three major types of curves. Macro curves representing an economies GDP, a micro curve representing a microeconomic sector within an economy,
# and a product curve representing the demand for a product nested within the previous curves.
    #It should be noted that here we don't generated one curve for each type, but several so that we can simulate the demand for multiple products for example within an economy.
    #It is planned to modify the function to enable control of variables within the function from outside

# Call the generate_market_curves function with the generated variables as arguments
Define_Curves.generate_market_curves(1, macro, micro, product, id_ma, id_mi, id_po, Temp_Micro_Value, Temp_Product_Value, macro_ampl_slider, macro_growth_factor_slider, macro_freq_slider, Micro_Amplitude_slider, Micro_Growth_Factor_slider, Micro_Frequency_slider, Product_Amplitude_slider, Product_Growth_Factor_slider, Product_Frequency_slider)


print("Curves are defined")






for i in a:
    print(i)
    RCBL.calculate_balance_sheet(i)
    RC_Income_ST.calculate_income_statement(i)
    RC_PNL.calculate_pnl(i)
    Insert_Goverment_Policy.init_Goverment_Policies('Financials.db', macro, randomness, percentage_change, min_days_between_updates)











#Upcoming: Implementing functions that calculate daily for every company the financial statements. This is the part where the company can adjust variables in order to achive better performance.
# The functions are mainly done, but the heart is missing. That would be the part where we identify what variables should be changeable, by how much and what else should the company be
#able to change. 
    #In the end, it is planned to implant a neural network into that function that through self play learns how to adjust to several scenarious and run a company most efficiently.
    #In this part help would be greatly appreciated.































