import matplotlib.pyplot as plt
import numpy as np
from read_data import ReadData
import pycountry_convert as pc
from itertools import islice
from user_agents import parse
import graphviz

# makes the graph look nicer
plt.style.use('fivethirtyeight')


class Task:
    global data
    global country_df
    global reader_df
    unique_docs = None
    global visitors

    def __init__(self, filename):
        # do not delete - required for line below
        self.data = ReadData(filename)

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

    def task_3_a(self):
        browsers = self.data.get_browsers()
        browser_counts = {}
        for user_agent in browsers:
            ua = parse(user_agent)
            browser = ua.browser.family
            if browser in browser_counts:
                browser_counts[browser] += 1
            else:
                browser_counts[browser] = 1
        browser = []
        views = []
        for key, value in browser_counts.items():
            browser.append(key)
            views.append(value)
        return browser, views

    def task_3_b(self):
        dict = {
            'Chrome': 0,
            'Opera': 0,
            'Firefox': 0,
            'Safari': 0,
            'IE': 0,
            'Facebook': 0,
            'Android': 0,
            'Google': 0,
            'Other': 0
        }
        browser, views = self.task_3_a()
        found = False
        for i, j in enumerate(browser):
            for key in dict:
                if key in j:
                    dict[key] += views[i]
                    found = True
            if not found:
                dict['Other'] += views[i]
        new_browser = []
        new_views = []
        for key, value in dict.items():
            new_browser.append(key)
            new_views.append(value)

        return new_browser, new_views

    def task_4(self):
        self.reader_df = self.data.get_reader_df()
        # list of unique user ids       
        unique_ids_to_match = self.reader_df['visitor_uuid'].unique()
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
        sorted_by_readtime = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        # slice first ten records from dict
        highest_readtime = dict(islice(sorted_by_readtime.items(), 10))
        user_ids = list(highest_readtime.keys())
        readtimes = list(highest_readtime.values())
        return user_ids, readtimes

    def task_5_a(self, doc_id):
        return self.data.get_visitor_df(doc_id)

    def task_5_b(self, visitor_id):
        return self.data.get_visitor_doc_id(visitor_id)

    def task_5_c(self, doc_id, visitor_uuid=None, sorting_function=None):
        add_visitor = self.data.check_visitor_reads_doc(visitor_uuid, doc_id)
        if visitor_uuid and add_visitor:
            readers = self.task_5_a(doc_id)
            self.visitors = []
            for i in readers.unique():
                self.visitors.append(i)
            self.visitors.append(visitor_uuid)
        else:
            print("visitor not read doc")
            self.visitors = self.task_5_a(doc_id)
        self.unique_docs = set()
        # add each document of each visitor to a set ( so no duplicates allowed)
        for visitor in self.visitors:
            docs = self.task_5_b(visitor)
            for doc in docs:
                self.unique_docs.add(doc)

        if sorting_function:
            return sorting_function(self.unique_docs)
        else:
            return self.unique_docs

    def task_5_d(self, doc_id, visitor_id = None): # use 140222104953-4a9c401847f56cbad2cb7376727cb4fe doc_uuid
        docs = self.task_5_c(doc_id=doc_id, visitor_uuid=visitor_id, sorting_function=self.sorting_function)
        return docs

    def sorting_function(self, unique_docs):
        sorted_doc = {}
        # for each doc ID in the unique_docs set get the total number of viewers
        for doc in unique_docs:
            visitor = self.data.get_visitor_df(doc)
            sorted_doc[doc] = len(visitor)
        # sort the doc ID viewers from high to low
        sorted_viewers = {k: v for k, v in sorted(sorted_doc.items(), key=lambda item: item[1], reverse=True)}
        # return the top 10 doc ID's from the sorted list
        top_10_results = dict(list(sorted_viewers.items())[:10])
        documents = []
        viewers = []
        # for each item in top_10_results append the key (doc ID) and value (number of viewers) and to be returned
        # for the graph
        for key, value in top_10_results.items():
            documents.append(key)
            viewers.append(value)
        return documents, viewers

    def task_6(self, doc_id, visitor_uuid):
        sorted_doc = {}
        self.task_5_c(doc_id, visitor_uuid)
        # for each doc ID in the unique_docs set collect all visitors
        for doc in self.unique_docs:
            visitor = self.data.get_visitor_df(doc)
            for vis in visitor:
                if vis in self.visitors:
                    sorted_doc.setdefault(doc, []).append(vis)
        dot_dict = {}
        # for each doc id
        for doc, visitors in sorted_doc.items():
            # assign node to unique doc
            # print("\n")
            # get unique visitor ids for each doc id
            unique_visitors = []
            for v in visitors:
                # print(v)
                if v in unique_visitors:
                    continue
                else:
                    unique_visitors.append(v)
            dot_dict.setdefault(doc, []).append(unique_visitors)
        # print("\nDoc dictionary:", dot_dict, "\n")
        # create nodes for docs and visitors (convert to 4-dig hex first) and link them together using dot tool
        dot = graphviz.Digraph('also_likes', comment='Also Likes Graph')
        # widen space between layers
        dot.attr(ranksep='2')
        # change appearance of arrows
        dot.edge_attr.update(arrowhead='vee', arrowsize='1.5')
        dot.format = 'pdf'
        # get 4-digit hex for doc_id and visitor_uuid
        # color=green
        input_doc_id_hex = doc_id[-4:]
        input_visitor_uuid_hex = visitor_uuid[-4:]
        for doc, visitors in dot_dict.items():
            doc_hex = doc[-4:]
            if doc_hex == input_doc_id_hex:
                dot.node(doc_hex, doc_hex, shape='box', style='filled', fillcolor='green', color='green')
            else:
                dot.node(doc_hex, doc_hex, shape='box')
            visitors = visitors[0]
            for visitor in visitors:
                visitor_hex = visitor[-4:]
                if visitor_hex == input_visitor_uuid_hex:
                    dot.node(visitor_hex, visitor_hex, style='filled', fillcolor='green', color='green')
                else:
                    dot.node(visitor_hex, visitor_hex)
                # link the nodes
                dot.edge(visitor_hex, doc_hex)
        # print("also_likes graph:", dot.source)
        # automatically display png graph in a new window
        dot.render(directory='doctest-output').replace('\\', '/')
        dot.render(directory='doctest-output', view=True) 
