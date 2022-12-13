import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

#As of now, here a set of 100 companies are created within the class "company".
#That class has some placeholder values like name, what macro, micro and product group its active in. (temporary)
#Within that class is another sub class that will document changes over time, mainly financials.
#At this point in time, its all temporary, but the main idea to have some main stats in the main class and the financial stats in the sub class aims to make calculations easier and scalable. 


#List of placeholder company names
#For now every product has 100 companies servicing the market
Company_base_names = ["Casper", "Predovic and Corwin", "O'Reilly", "Cremin and Runte", "Hilll - Haag", "Klocko, Quitzon and Johns",
"Spinka - Turcotte",
"Hettinger, Schneider and Klein"
"Nikolaus Inc",
"Little, Wiegand and Ziemann",
"Grimes - Dach",
"Kirlin Group",
"Pacocha LLC",
"Feest, Lang and Douglas",
"Larson, Christiansen and Nienow",
"Klocko, Bosco and Terry",
"Rohan, Prosacco and Reynolds",
"Hackett - Purdy",
"Schmeler Inc",
"Renner, Renner and Zemlak",
"Towne and Sons",
"Kovacek and Sons",
"Zboncak - Feest",
"Waelchi, Bernier and Grimes",
"Collins Group",
"Kling - Cartwright",
"Rolfson, Koelpin and O'Conner",
"Barton Inc",
"Bode LLC",
"Ferry - Schuster",
"Herman - Kiehn",
"Gibson - Baumbach",
"Ziemann - Bashirian",
"Abernathy Inc",
"Cronin, Douglas and Crooks",
"Little - Goyette",
"Altenwerth - Greenholt",
"Mills - Turner",
"Torphy and Sons",
"Schulist, Kunde and Corkery",
"Zieme, Boyle and Fisher",
"Hickle - Dare",
"Mitchell - Cole",
"Gislason - Zieme",
"Glover, Abbott and Blick",
"Vandervort and Sons",
"Nader, Yost and Beer",
"Bosco - Rath",
"Braun - Pfannerstill",
"Davis - Tremblay",
"Fadel - Rice",
"Conn Group",
"Roberts LLC",
"Hyatt - Sporer",
"Grant LLC",
"Gleichner, Sipes and Wuckert",
"Stroman Inc",
"Witting - Toy",
"Dare, Sipes and Gerlach",
"Pagac LLC",
"Howe, Schuster and Friesen",
"Steuber - Stehr",
"Smitham - Ledner",
"Cole, Johnson and Haley",
"Emard - Rohan",
"Cassin, Treutel and Kshlerin",
"Hudson Group",
"Kshlerin, Christiansen and Trantow",
"Keebler, Kautzer and Heathcote",
"Kling - Jast",
"Tremblay, Wolf and Johns",
"Bergstrom, McClure and Runte",
"Hills LLC",
"Lebsack and Sons",
"Sporer, Ondricka and Beahan",
"Bernhard Inc",
"Parker, Osinski and Beer",
"Schultz - McClure",
"Hettinger and Sons",
"Nolan - Cruickshank",
"Brekke, Kuvalis and Hartmann",
"Zemlak, Haag and Boyle",
"Goldner, O'Keefe and Lindgren",
"Wiza, Price and Batz",
"Robel, Jaskolski and Kozey",
"Stroman - Glover",
"Doyle, King and Hintz",
"Bartoletti Inc",
"Howe, Luettgen and Schmidt",
"Kub, Collier and Kiehn",
"Oberbrunner - Legros",
"Conn - Cronin",
"Koelpin - Howell",
"Bailey LLC",
"Padberg - Daugherty",
"Nikolaus - Schimmel",
"Corwin, Sauer and Schultz",
"Braun Group",
"Crona - Hagenes",
"Dietrich Inc", "Conn Group", "Koepp - Weber"]

#Creating the company class

class Company:
    def __init__(self, company_name, macro, micro, product):
        self.company_name = company_name
        self.macro = macro
        self.micro = micro
        self.product = product


    class financials:
        def __init__(self, time, revenue,market_share, costs):
            self.time = time
            self.revenue = revenue
            self.market_share = market_share
            self.costs = costs

    def print_details(self):
        print(self.company_name, self.macro, self.micro, self.product, self.financials.time, self.financials.revenue, self.financials.market_share, self.financials.costs)


#This market share calculation will likely be exported to another file as its complexity grows.
#For now it just provides some basic values to test the classes company and financials. 

    #Create a random arrangment of market shares
    #Normalize them towards 100%
    #Each number refers to the % of market share a company has of one product

    #Hierarchy = Macro Economy (Country) > Micro Economy (Industry) > Product > Company
    #Here the distribution of marketshare of Product for each company is determined

company_distribution_seed = np.random.rand(100, 1)
company_distribution_seed_sum = sum(company_distribution_seed)
company_distribution_fraction = company_distribution_seed/company_distribution_seed_sum

#print(company_distribution_fraction)

str(company_distribution_fraction)

x = np.arange(0, 100, 1)
company_name_marketshare = []

for i in Company_base_names:
    i = Company(i , "macro1", "micro1", "product1")
    i.financials.time = np.random.rand(1, 1)
    i.financials.revenue = np.random.rand(1, 1)
    i.financials.market_share = []
    i.financials.costs = np.random.rand(1, 1)
    #i.print_details()

#How can i add the market share directly into the object???
#Right now its sepeate, that will probably cause some headache down the line
for i in x:
    tmp = [Company_base_names[i], company_distribution_fraction[i]]
    company_name_marketshare.append(tmp)

#This shows that company name and marketshare are connected in the list = company_name_marketshare
#12 is just an example element in the list
print(company_name_marketshare[12])