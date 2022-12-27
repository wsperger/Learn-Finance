import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np



# Define X-Axis
t = np.arange(0, 1000)

#Percentages Values
Temp_Micro_Value = 0.5
Temp_Product_Value = 0.5

# Define the initial values
init_Macro_Amplitude = 8
init_Macro_Growth_Factor = 0.5
init_Macro_Frequency = 0.01

init_Micro_Amplitude = 4
init_Micro_Growth_Factor = 0.5
init_Micro_Frequency = 0.08

init_Product_Amplitude = 2
init_Product_Growth_Factor = 0.5
init_Product_Frequency = 0.2


#Calculations
def Macro_Curve(t, macro_ampl_slider, macro_freq_slider, macro_growth_factor_slider):
    return (macro_ampl_slider * np.sin(macro_freq_slider * t))+(np.sqrt(t*macro_growth_factor_slider))

def Micro_Curve(t, Micro_Amplitude_slider, Micro_Frequency_slider, Micro_Growth_Factor_slider, Temp_Micro_Value, macro_ampl_slider, macro_freq_slider, macro_growth_factor_slider):
    return ((((macro_ampl_slider * np.sin(macro_freq_slider * t))+(np.sqrt(t*macro_growth_factor_slider))+((Micro_Amplitude_slider * np.sin(2*Micro_Frequency_slider * t))+(np.sqrt(t*Micro_Growth_Factor_slider))))/2) * Temp_Micro_Value)

def Product_Demand_Curve(t, Micro_Amplitude_slider, Micro_Frequency_slider, Micro_Growth_Factor_slider, Temp_Micro_Value, macro_ampl_slider, macro_freq_slider, macro_growth_factor_slider,Product_Amplitude_slider, Product_Frequency_slider, Product_Growth_Factor_slider, Temp_Product_Value):
    return ((((((macro_ampl_slider * np.sin(macro_freq_slider * t))+(np.sqrt(t*macro_growth_factor_slider))+((Micro_Amplitude_slider * np.sin(2*Micro_Frequency_slider * t))+(np.sqrt(t*Micro_Growth_Factor_slider))))/2) * Temp_Micro_Value)+((Product_Amplitude_slider * np.sin(2*Product_Frequency_slider * t))+(np.sqrt(t*Product_Growth_Factor_slider))))/3)

import sqlite3

# Connect to the database
conn = sqlite3.connect('variables.db')

# Create a cursor
cursor = conn.cursor()


# Insert the initial values
cursor.execute('''INSERT INTO variables (Temp_Micro_Value, Temp_Product_Value, init_Macro_Amplitude, init_Macro_Growth_Factor, init_Macro_Frequency, init_Micro_Amplitude, init_Micro_Growth_Factor, init_Micro_Frequency, init_Product_Amplitude, init_Product_Growth_Factor, init_Product_Frequency)
VALUES (0.5, 0.5, 8, 0.5, 0.01, 4, 0.5, 0.08, 2, 0.5, 0.2)''')

# Commit the transaction
conn.commit()

# Close the connection
conn.close()



