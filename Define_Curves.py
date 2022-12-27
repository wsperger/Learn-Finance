import sqlite3
import numpy as np
import sqlite3

def generate_market_curves():
    # Connect to the database
    conn = sqlite3.connect('Financials.db')

    # Create a cursor
    cursor = conn.cursor()

    # Define X-Axis
    t = np.arange(0, 3640)



        #Market Share Value
            #Percentage of total product GDP/demand that the company takes


    macro = ["Germany", "France", "Italy", "Indonesia", "2das"]

    #List of placeholder industry names
    micro = ["Source", "Manufacturing", "Retail"]

    #List of placeholder product names
    product = ["bike", "phone"]

    id_ma = 1
    id_mi = 1
    id_po = 1

    Temp_Micro_Value = 1/len(micro)
    Temp_Product_Value = 1/len(product)


    # Define the initial values of the sliders
    macro_ampl_slider = 8
    macro_growth_factor_slider = 0.5
    macro_freq_slider = 0.01

    Micro_Amplitude_slider = 4
    Micro_Growth_Factor_slider = 0.5
    Micro_Frequency_slider = 0.08

    Product_Amplitude_slider = 2
    Product_Growth_Factor_slider = 0.5
    Product_Frequency_slider = 0.2

    #Calculations
    def Macro_Curve(t, macro_ampl_slider, macro_freq_slider, macro_growth_factor_slider):
        return (macro_ampl_slider * np.sin(macro_freq_slider * t))+(np.sqrt(t*macro_growth_factor_slider))

    def Micro_Curve(t, Micro_Amplitude_slider, Micro_Frequency_slider, Micro_Growth_Factor_slider, Temp_Micro_Value, macro_ampl_slider, macro_freq_slider, macro_growth_factor_slider):
        return ((((macro_ampl_slider * np.sin(macro_freq_slider * t))+(np.sqrt(t*macro_growth_factor_slider))+((Micro_Amplitude_slider * np.sin(2*Micro_Frequency_slider * t))+(np.sqrt(t*Micro_Growth_Factor_slider))))/2) * Temp_Micro_Value)

    def Product_Demand_Curve(t, Micro_Amplitude_slider, Micro_Frequency_slider, Micro_Growth_Factor_slider, Temp_Micro_Value, macro_ampl_slider, macro_freq_slider, macro_growth_factor_slider,Product_Amplitude_slider, Product_Frequency_slider, Product_Growth_Factor_slider, Temp_Product_Value):
        return ((((((macro_ampl_slider * np.sin(macro_freq_slider * t))+(np.sqrt(t*macro_growth_factor_slider))+((Micro_Amplitude_slider * np.sin(2*Micro_Frequency_slider * t))+(np.sqrt(t*Micro_Growth_Factor_slider))))/2) * Temp_Micro_Value)+((Product_Amplitude_slider * np.sin(2*Product_Frequency_slider * t))+(np.sqrt(t*Product_Growth_Factor_slider))))/3)

    # Create the table
    cursor.execute("CREATE TABLE IF NOT EXISTS macro (id TEXT, y_values REAL, x_values REAL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS micro (id TEXT, y_values REAL, x_values REAL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS product (id TEXT, y_values REAL, x_values REAL)")

    for ma in macro:
        y_values = Macro_Curve(t, macro_ampl_slider, macro_freq_slider, macro_growth_factor_slider)
        macro_id = "macro " + ma + str(id_ma)
        x_values = t

        # Iterate through the y_values and x_values arrays
        for y, x in zip(y_values, x_values):
            # Convert the x value to a string
            x_string = str(x)

            # Insert a row into the table
            cursor.execute("INSERT INTO macro (id, y_values, x_values) VALUES (?, ?, ?)", (macro_id, y, x_string))

        # Commit the changes
        conn.commit()

        id_ma += 1
        for mi in micro:
           y_values = Micro_Curve(t, Micro_Amplitude_slider, Micro_Frequency_slider, Micro_Growth_Factor_slider, Temp_Micro_Value, macro_ampl_slider, macro_freq_slider, macro_growth_factor_slider)
           micro_id = "micro " + ma + " " + mi + str(id_mi)
           x_values = t

           # Iterate through the y_values and x_values arrays
           for y, x in zip(y_values, x_values):
               # Convert the x value to a string
               x_string = str(x)

               # Insert a row into the table
               cursor.execute("INSERT INTO micro (id, y_values, x_values) VALUES (?, ?, ?)", (micro_id, y, x_string))

           # Commit the changes
           conn.commit()

           id_mi += 1
           for po in product:

               y_values = Product_Demand_Curve(t, Micro_Amplitude_slider, Micro_Frequency_slider, Micro_Growth_Factor_slider, Temp_Micro_Value, macro_ampl_slider, macro_freq_slider, macro_growth_factor_slider,Product_Amplitude_slider, Product_Frequency_slider, Product_Growth_Factor_slider, Temp_Product_Value)
               product_id = "product " + ma + " " + mi + " " + po + str(id_po)
               x_values = t

               # Iterate through the y_values and x_values arrays
               for y, x in zip(y_values, x_values):
                   # Convert the x value to a string
                   x_string = str(x)

                   # Insert a row into the table
                   cursor.execute("INSERT INTO product (id, y_values, x_values) VALUES (?, ?, ?)", (product_id, y, x_string))

               # Commit the changes
               conn.commit()



               id_po += 1

    # Close the connection
    conn.close()
