i have this function and it returns to me the company id, price and market shar. I need you to write me a new function that takes in that array and the market size which is an integer, and for each company but in the order that they come in the array, increases the market_share size of the first one by a variable amount that can be controlled from outside the company, multplies the market share times the market size and send the result, called revenue,  together with the id for that company int this table "'CREATE TABLE IF NOT EXISTS pnl (
                        id TEXT,
                        date integer,
                        revenue REAL NOT NULL,
                        cost_of_goods_sold REAL NOT NULL,
                        gross_profit REAL NOT NULL,
                        selling_and_administrative_expenses REAL NOT NULL,
                        operating_income REAL NOT NULL,
                        other_income_expense REAL NOT NULL,
                        net_income REAL NOT NULL,
                        FOREIGN KEY (id) REFERENCES Company_Allocation(id)
                        PRIMARY KEY (id, date)
                        )''')"

It is very important that date for the new row is one bigger than the biggest date for that id in that table. It is also important that the market size is substracted by the revnue of that company. Then, the process needs to repeat for every company in the original array.