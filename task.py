import matplotlib.pyplot as plt
import numpy as np
from read_data import ReadData
import pandas as pd

plt.style.use('fivethirtyeight') # makes the graph look nicer

class Task:
    def __init__(self):
        print("hi")

    def show(self):
        data = ReadData() # do not delete. line required for code below.

        countries_df = ReadData.countries_df() # data frame for countries

        countries_unique = countries_df['visitor_country'].unique() # find unique countries
        countries_unique = np.array(countries_unique) # convert into array

        countries_values = countries_df['visitor_country'].value_counts() # find number of occurances for each country
        countries_values = np.array(countries_values) # convert into array

        plt.bar(countries_unique, countries_values, color='#444444', label='Viewers') # creates bar chart (len of args 0 and 1 must be equal)

        plt.title('Histogram of Countries') # name of graph
        plt.xlabel('Countries') # x axis label
        plt.ylabel('Total Viewers') # y axis label

        plt.tight_layout()
        plt.legend()
        plt.show()
        
        #data = d.query()
        #xpoints = np.array([0, 6])
        #ypoints = np.array([0, 250])

        #plt.plot(xpoints, data)
        #plt.show()