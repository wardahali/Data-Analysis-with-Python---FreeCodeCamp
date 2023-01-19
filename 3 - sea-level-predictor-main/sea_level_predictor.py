import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv',float_precision='legacy')

    # Create scatter plot
    fig, axis = plt.subplots(figsize=(15, 7))
    
    plt.scatter(x= 'Year', y='CSIRO Adjusted Sea Level', data=df, color='orange')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    line1_x = np.arange(1880, 2050)
    line1_y = slope*line1_x + intercept
    plt.plot(line1_x, line1_y, color='red')

    # Create second line of best fit
    ax= df['Year'].loc[df['Year']>=2000]
    ay=df['CSIRO Adjusted Sea Level'].loc[df['Year']>=2000]
    slope, intercept, r_value, p_value, std_err = linregress(ax, ay)
    line2_x = np.arange(2000,2050)
    line2_y = slope*line2_x + intercept
    plt.plot(line2_x, line2_y, color='blue')    

    plt.legend()

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()