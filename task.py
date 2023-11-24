import matplotlib.pyplot as plt
import numpy as np
from read_data import ReadData

plt.style.use('fivethirtyeight') # makes the graph look nicer

class Task:

    global df

    def __init__(self, doc_id):
        data = ReadData() # do not delete - required for line below
        self.df = data.get_df(doc_id) # gets dataframe

    def unique(self):
        unique = self.df['visitor_country'].unique() # find unique y-labels
        unique = np.array(unique) # convert into array
        return unique

    def values(self):
        values = self.df['visitor_country'].value_counts() # find number of occurences for each label
        values = np.array(values) # convert into array
        return values
    
    def show(self):
        print("")
        #data = d.query()
        #xpoints = np.array([0, 6])
        #ypoints = np.array([0, 250])

        #plt.plot(xpoints, data)
        #plt.show()
