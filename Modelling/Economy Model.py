import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

#Micro
#amplitude = 12
#frequency = 0.1
#growth_factor = 0.1

#Demand Distribution
#Determined what percentage of the total upper level demand the object receives
    #Economy Share Value
        #Percentage of total country GDP that the industry takes
Temp_Micro_Value = 0.5

    #Market Share Value
        #Percentage of total product GDP/demand that the company takes
Temp_Product_Value = 0.5

#What about interdependencies of procucts?

# Create a figure with tight layout
fig = plt.figure(tight_layout=True)

# Define X-Axis
t = np.arange(0, 3640)

# Create three axes on the figure
Macro_ax1 = fig.add_subplot(221)
Macro_ax1.set_title('Macro Curve')
Macro_ax1.set_xlabel('Days')
Macro_ax1.set_ylabel('y')

Micro_ax2 = fig.add_subplot(222)
Micro_ax2.set_title('Micro Curve')
Micro_ax2.set_xlabel('Days')
Micro_ax2.set_ylabel('y')


Compa_ax3 = fig.add_subplot(223)
Compa_ax3.set_title('Product Curve')
Compa_ax3.set_xlabel('Days')
Compa_ax3.set_ylabel('y')

# Define the initial values of the sliders
init_Macro_Amplitude = 8
init_Macro_Growth_Factor = 0.5
init_Macro_Frequency = 0.01

init_Micro_Amplitude = 4
init_Micro_Growth_Factor = 0.5
init_Micro_Frequency = 0.08

init_Product_Amplitude = 2
init_Product_Growth_Factor = 0.5
init_Product_Frequency = 0.2

# Add the macro_ampl_slider to the figure
Macro_Amplitude = fig.add_axes([0.6, 0.0, 0.3, 0.05])
macro_ampl_slider = Slider(Macro_Amplitude, label="Macro_Amplitude", valmin=0, valmax=10, valinit=init_Macro_Amplitude)

# Add the macro_growth_factor_slider to the figure
Macro_Growth_Factor = fig.add_axes([0.6, 0.05, 0.3, 0.05])
macro_growth_factor_slider = Slider(Macro_Growth_Factor, label="Macro_Growth_Factor", valmin=0, valmax=10, valinit=init_Macro_Growth_Factor)

# Add the macro_freq_slider to the figure
Macro_Frequency = fig.add_axes([0.6, 0.1, 0.3, 0.05])
macro_freq_slider = Slider(Macro_Frequency, label="Macro_Frequency", valmin=0, valmax=10, valinit=init_Macro_Frequency)

# Add the Micro_Amplitude_slider to the figure
Micro_Amplitude = fig.add_axes([0.6, 0.15, 0.3, 0.05])
Micro_Amplitude_slider = Slider(Micro_Amplitude, label="Micro_Amplitude", valmin=0, valmax=10, valinit=init_Micro_Amplitude)

# Add the fifth slider to the figure
Micro_Growth_Factor = fig.add_axes([0.6, 0.2, 0.3, 0.05])
Micro_Growth_Factor_slider = Slider(Micro_Growth_Factor, label="Micro_Growth_Factor", valmin=0, valmax=10, valinit=init_Micro_Growth_Factor)

# Add the Micro_Frequency_slider to the figure
Micro_Frequency = fig.add_axes([0.6, 0.25, 0.3, 0.05])
Micro_Frequency_slider = Slider(Micro_Frequency, label="Micro_Frequency", valmin=0, valmax=10, valinit=init_Micro_Frequency)

# Add the Product_Frequency_slider to the figure
Product_Frequency = fig.add_axes([0.6, 0.3, 0.3, 0.05])
Product_Frequency_slider = Slider(Product_Frequency, label="Product_Frequency", valmin=0, valmax=10, valinit=init_Product_Frequency)

# Add the Product_Amplitude_slider to the figure
Product_Amplitude = fig.add_axes([0.6, 0.35, 0.3, 0.05])
Product_Amplitude_slider = Slider(Product_Amplitude, label="Product_Amplitude", valmin=0, valmax=10, valinit=init_Product_Amplitude)

# Add the Product_Growth_Factor_slider to the figure
Product_Growth_Factor = fig.add_axes([0.6, 0.4, 0.3, 0.05])
Product_Growth_Factor_slider = Slider(Product_Growth_Factor, label="Product_Growth_Factor", valmin=0, valmax=10, valinit=init_Product_Growth_Factor)

#Calculations
def Macro_Curve(t, macro_ampl_slider, macro_freq_slider, macro_growth_factor_slider):
    return (macro_ampl_slider * np.sin(macro_freq_slider * t))+(np.sqrt(t*macro_growth_factor_slider))

def Micro_Curve(t, Micro_Amplitude_slider, Micro_Frequency_slider, Micro_Growth_Factor_slider, Temp_Micro_Value, macro_ampl_slider, macro_freq_slider, macro_growth_factor_slider):
    return ((((macro_ampl_slider * np.sin(macro_freq_slider * t))+(np.sqrt(t*macro_growth_factor_slider))+((Micro_Amplitude_slider * np.sin(2*Micro_Frequency_slider * t))+(np.sqrt(t*Micro_Growth_Factor_slider))))/2) * Temp_Micro_Value)

def Product_Demand_Curve(t, Micro_Amplitude_slider, Micro_Frequency_slider, Micro_Growth_Factor_slider, Temp_Micro_Value, macro_ampl_slider, macro_freq_slider, macro_growth_factor_slider,Product_Amplitude_slider, Product_Frequency_slider, Product_Growth_Factor_slider, Temp_Product_Value):
    return ((((((macro_ampl_slider * np.sin(macro_freq_slider * t))+(np.sqrt(t*macro_growth_factor_slider))+((Micro_Amplitude_slider * np.sin(2*Micro_Frequency_slider * t))+(np.sqrt(t*Micro_Growth_Factor_slider))))/2) * Temp_Micro_Value)+((Product_Amplitude_slider * np.sin(2*Product_Frequency_slider * t))+(np.sqrt(t*Product_Growth_Factor_slider))))/3)

# Define a function that will be called when the slider values are changed
def update(val):
    # Update the values of the sliders
    val1 = macro_ampl_slider.val
    val2 = macro_growth_factor_slider.val
    val3 = macro_freq_slider.val
    val4 = Micro_Amplitude_slider.val
    val5 = Micro_Growth_Factor_slider.val
    val6 = Micro_Frequency_slider.val

    # Update the plots on the axes
    Macro_ax1.clear()
    Macro_ax1.plot(t, Macro_Curve(t, macro_ampl_slider.val, macro_freq_slider.val, macro_growth_factor_slider.val))
    Macro_ax1.set_title('Macro Curve')
    Macro_ax1.set_xlabel('Days')
    Macro_ax1.set_ylabel('y')

    Micro_ax2.clear()
    Micro_ax2.plot(t, Micro_Curve(t, Micro_Amplitude_slider.val, Micro_Frequency_slider.val, Micro_Growth_Factor_slider.val, Temp_Micro_Value, macro_ampl_slider.val, macro_freq_slider.val, macro_growth_factor_slider.val))
    Micro_ax2.set_title('Micro Curve')
    Micro_ax2.set_xlabel('Days')
    Micro_ax2.set_ylabel('y')

    Compa_ax3.clear()
    Compa_ax3.plot(t, Product_Demand_Curve(t, Micro_Amplitude_slider.val, Micro_Frequency_slider.val, Micro_Growth_Factor_slider.val, Temp_Micro_Value, macro_ampl_slider.val, macro_freq_slider.val, macro_growth_factor_slider.val,Product_Amplitude_slider.val, Product_Frequency_slider.val, Product_Growth_Factor_slider.val, Temp_Product_Value))
    Compa_ax3.set_title('Company Curve')
    Compa_ax3.set_xlabel('Days')
    Compa_ax3.set_ylabel('y')

# Call the update function whenever the slider values are changed
macro_ampl_slider.on_changed(update)
macro_growth_factor_slider.on_changed(update)
macro_freq_slider.on_changed(update)
Micro_Amplitude_slider.on_changed(update)
Micro_Growth_Factor_slider.on_changed(update)
Micro_Frequency_slider.on_changed(update)
Product_Amplitude_slider.on_changed(update)
Product_Growth_Factor_slider.on_changed(update)
Product_Frequency_slider.on_changed(update)

plt.show()