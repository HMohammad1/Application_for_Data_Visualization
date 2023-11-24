import matplotlib.pyplot as plt
import numpy as np
from read_data import ReadData
import pycountry_convert as pc

plt.style.use('fivethirtyeight')  # makes the graph look nicer


class Task:
    global df

    def __init__(self, doc_id):
        data = ReadData()  # do not delete - required for line below
        self.df = data.get_df(doc_id)  # gets dataframe

    def task_2_a(self):
        unique = self.df['visitor_country'].unique()  # find unique y-labels
        values = self.df['visitor_country'].value_counts()  # find number of occurrences for each label
        return unique, values

    def task_2_b(self):
        unique, values = self.task_2_a()
        continent = {
            'NA': 0,
            'SA': 0,
            'EU': 0,
            'AF': 0,
            'AS': 0,
            'OC': 0,
            'AN': 0
        }
        continent_names = {
            'NA': 'North America',
            'SA': 'South America',
            'EU': 'Europe',
            'AF': 'Africa',
            'AS': 'Asia',
            'OC': 'Oceania',
            'AN': 'Antarctica'
        }
        continents = []
        continents_values = []
        for i, j in enumerate(unique):
            continent_code = pc.country_alpha2_to_continent_code(j)
            if continent_code in continent:
                continent[continent_code] += values[i]
        for key, value in continent.items():
            if value != 0:
                continent_name = continent_names.get(key)
                continents.append(continent_name)
                continents_values.append(value)
                # print(f"Key: {key}, Value: {value}")
        return continents, continents_values
