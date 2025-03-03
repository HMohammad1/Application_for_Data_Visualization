import matplotlib.pyplot as plt
from read_data import ReadData
import pycountry_convert as pc
from itertools import islice
from user_agents import parse
import graphviz

# makes the graph look nicer
plt.style.use('fivethirtyeight')


class Task:
    # initialise the global class variables
    def __init__(self, filename, new_file_path=None):
        if new_file_path is not None:
            self.data = ReadData(filename, new_file_path)
        else:
            self.data = ReadData(filename)
        self.unique_docs = None
        self.visitors = None

    # check if the loaded data is not empty, used in other method to check before processing
    def check_pd_data(self):
        if self.data.data is None:
            return False

    # get the countries a doc has been read in and the number of viewers
    def task_2_a(self, doc_id):
        # check file is valid
        if self.check_pd_data() is not False:
            country_df = self.data.get_country_df(doc_id)
        else:
            return False, "Incorrect filename or no filename specified."
        # check doc id is valid
        if len(country_df) == 0:
            return False, "Incorrect doc UUID specified"
        # find unique y-labels
        unique = country_df['visitor_country'].unique()
        # find number of occurrences for each label
        values = country_df['visitor_country'].value_counts()
        return unique, values

    # get the continents from task 2a and return this instead with the total user counts for each
    def task_2_b(self, doc_id):
        # check file is valid
        param1, param2 = self.task_2_a(doc_id)
        if param1 is not False:
            unique, values = self.task_2_a(doc_id)
        else:
            return False, param2
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
                continent_temp[continent_code] += values.iloc[i]
            else:
                continent_temp[continent_code] = values.iloc[i]
        # return the continents as full names and viewers in the temp dictionary
        for key, value in continent_temp.items():
            continent_name = continent_names.get(key)
            continents.append(continent_name)
            continents_values.append(value)
        return continents, continents_values

    # get all the browsers used and the number of times they are used
    def task_3_a(self):
        # check file is valid
        if self.check_pd_data() is not False:
            browsers = self.data.get_browsers()
        else:
            return False, "Incorrect filename or no filename specified."
        browser_counts = {}
        # getting the actual browsers using the parse class imported
        for user_agent in browsers:
            ua = parse(user_agent)
            browser = ua.browser.family
            if browser in browser_counts:
                browser_counts[browser] += 1
            else:
                browser_counts[browser] = 1
        browser = []
        views = []
        # return the data for the relevant axes, x or y
        for key, value in browser_counts.items():
            browser.append(key)
            views.append(value)
        return browser, views

    # simplify task 3a by only showing the most important browsers
    def task_3_b(self):
        # a dictionary of what browsers to display
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
        # check if file is valid based on the data from 3a
        browser, views = self.task_3_a()
        if browser is False:
            return False, views
        found = False
        # count the occurrences of each browser and update the dictionary
        for i, j in enumerate(browser):
            for key in dict:
                if key in j:
                    dict[key] += views[i]
                    found = True
            if not found:
                dict['Other'] += views[i]
        new_browser = []
        new_views = []
        # return the relevant data for the axes
        for key, value in dict.items():
            if value != 0:
                new_browser.append(key)
                new_views.append(value)
        return new_browser, new_views

    # get the most avid readers and how much time spent reading
    def task_4(self):
        # check file is valid
        if self.check_pd_data() is not False:
            reader_df = self.data.get_reader_df()
        else:
            return False, "Incorrect filename or no filename specified."
        # list of unique user ids       
        unique_ids_to_match = reader_df['visitor_uuid'].unique()
        # list of user ids and read time
        userid_readtime_dict = reader_df.to_dict(orient='records')
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

    # get the all the visitors from the doc id specified
    def task_5_a(self, doc_id):
        return self.data.get_visitor_df(doc_id)

    # get the doc ids from the visitor id specified
    def task_5_b(self, visitor_id):
        return self.data.get_visitor_doc_id(visitor_id)

    # return the also likes docs, return sorted if a sorting function is used otherwise unsorted
    def task_5_c(self, doc_id, visitor_uuid=None, sorting_function=None):
        # check if the added visitor has read the document
        add_visitor = self.data.check_visitor_reads_doc(visitor_uuid, doc_id)
        # if visitor has then add them to the list of visitors
        if visitor_uuid and add_visitor:
            readers = self.task_5_a(doc_id)
            self.visitors = []
            for i in readers.unique():
                self.visitors.append(i)
            self.visitors.append(visitor_uuid)
            has_read = True
        else:
            has_read = False
            self.visitors = self.task_5_a(doc_id)
        self.unique_docs = set()
        # add each document of each visitor to a set ( so no duplicates allowed)
        for visitor in self.visitors:
            docs = self.task_5_b(visitor)
            for doc in docs:
                self.unique_docs.add(doc)
        # return the docs sorted by viewers if a sorting function is used
        if sorting_function:
            docs, viewers = sorting_function(self.unique_docs)
            return docs, viewers, has_read
        else:
            return self.unique_docs

    # method to call task 5c
    def task_5_d(self, doc_id, visitor_id=None):
        # check both incorrect doc or file specified
        if self.check_pd_data() is not False:
            docs, viewers, has_read = self.task_5_c(doc_id=doc_id, visitor_uuid=visitor_id, sorting_function=self.sorting_function)
            # if the returned doc is empty then wrong doc uuid specified
            if len(docs) == 0:
                return False, "Incorrect doc UUID specified", None
            else:
                return docs, viewers, has_read
        else:
            return False, "Incorrect filename or no filename specified.", None

    # the sorting function to use for task 5c to get the top 10 docs only
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

    # display task 5c in a graphical way
    def task_6(self, doc_id, visitor_uuid):
        # check file is valid
        if self.check_pd_data() is False:
            return False, "Incorrect filename or no filename specified"
        # has read to check if the user has read the doc or not
        has_read = True
        if not self.data.check_visitor_reads_doc(visitor_uuid, doc_id):
            has_read = False
        sorted_doc = {}
        self.task_5_c(doc_id, visitor_uuid)
        # if sixe of docs is 0 then wrong doc id used
        if len(self.unique_docs) == 0:
            return False, "Incorrect doc UUID specified"
        # for each doc ID in the unique_docs set collect all visitors
        for doc in self.unique_docs:
            visitor = self.data.get_visitor_df(doc)
            for vis in visitor:
                for v in self.visitors:
                    if vis == v:
                        sorted_doc.setdefault(doc, []).append(vis)
        dot_dict = {}
        # for each doc id
        for doc, visitors in sorted_doc.items():
            # assign node to unique doc
            # get unique visitor ids for each doc id
            unique_visitors = []
            for v in visitors:
                # print(v)
                if v in unique_visitors:
                    continue
                else:
                    unique_visitors.append(v)
            dot_dict.setdefault(doc, []).append(unique_visitors)
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
        if visitor_uuid is not None:
            input_visitor_uuid_hex = visitor_uuid[-4:]
        else:
            input_visitor_uuid_hex = None
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
        return True, has_read
