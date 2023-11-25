import matplotlib.pyplot as plt
import numpy as np
from read_data import ReadData
import pycountry_convert as pc
from itertools import islice

# makes the graph look nicer
plt.style.use('fivethirtyeight')  

class Task:
    global data
    global country_df
    global reader_df

    def __init__(self):
        # do not delete - required for line below
        self.data = ReadData()

    def task_2_a(self, doc_id):
        self.country_df = self.data.get_country_df(doc_id)
        # find unique y-labels
        unique = self.country_df['visitor_country'].unique()  
        # find number of occurrences for each label
        values = self.country_df['visitor_country'].value_counts() 
        return unique, values

    def task_2_b(self, doc_id):
        unique, values = self.task_2_a(doc_id)
        # the different continent names and codes
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
        continent_temp = {}
        # loop over each value in unique (country codes) and add the number of viewers to the temp dictionary
        for i, j in enumerate(unique):
            continent_code = pc.country_alpha2_to_continent_code(j)
            if continent_code in continent_temp:
                continent_temp[continent_code] += values[i]
            else:
                continent_temp[continent_code] = values[i]
        # return the continents as full names and viewers in the temp dictionary
        for key, value in continent_temp.items():
            continent_name = continent_names.get(key)
            continents.append(continent_name)
            continents_values.append(value)
            # print(f"Key: {key}, Value: {value}")
        return continents, continents_values
    
    def task_4(self):
        self.reader_df = self.data.get_reader_df()
        # list of unique user ids       
        unique_ids_to_match= self.reader_df['visitor_uuid'].unique()
        # list of user ids and read time
        userid_readtime_dict = self.reader_df.to_dict(orient='records')
        # loop through dictionary and get all read times for each user id
        d = {}
        for id in unique_ids_to_match:
            for record in userid_readtime_dict:
                if record['visitor_uuid'] == id:
                    d.setdefault(id, []).append(record['event_readtime'])
        # sum readtimes for each user id
        for user_id, readtime in d.items():
            d[user_id] = sum(readtime)
        # sort dictionary by highest readtime
        sorted_by_readtime = dict(sorted(d.items(), key=lambda item:item[1], reverse=True)) 
        # slice first ten records from dict
        highest_readtime = dict(islice(sorted_by_readtime.items(), 10))
        user_ids = list(highest_readtime.keys())
        readtimes = list(highest_readtime.values())
        return user_ids, readtimes




        
