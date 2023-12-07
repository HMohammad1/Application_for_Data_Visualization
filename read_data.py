import pandas as pd


class ReadData:
    # initialise the variable that will store the data from the input file
    def __init__(self, filename, filepath=None):
        if filepath is not None:
            self.data = pd.read_json(filepath, lines=True)
        else:
            try:
                self.data = pd.read_json(filename, lines=True)
            # check for no files inputted
            except ValueError:
                self.data = None

    # return the countries that match the doc uuid inserted
    def get_country_df(self, doc_id):
        dataframe = pd.DataFrame(self.data, columns=['env_doc_id', 'visitor_country'])
        return dataframe[(dataframe['env_doc_id'] == doc_id)]

    # return the event read time for all users
    def get_reader_df(self):
        dataframe = pd.DataFrame(self.data, columns=['visitor_uuid', 'event_readtime'])
        return dataframe[pd.notna(dataframe['event_readtime'])]

    # return all viewer ID's of the doc ID given
    def get_visitor_df(self, doc_id):
        return self.data.loc[self.data['env_doc_id'] == doc_id, 'visitor_uuid'].astype(str)

    # return all the doc ID's for the given viewer but get rid of duplicates
    def get_visitor_doc_id(self, visitor):
        doc = self.data[self.data['visitor_uuid'] == visitor]['env_doc_id'].astype(str)
        return set(doc.unique())

    # check if a visitor uuid reads a given doc ID and return
    def check_visitor_reads_doc(self, visitor_uuid, doc_id):
        matching_rows = self.data[(self.data['visitor_uuid'] == visitor_uuid) & (self.data['env_doc_id'] == doc_id)]
        if not matching_rows.empty:
            return True
        else:
            return False

    # return all the browsers used in the entire file
    def get_browsers(self):
        return self.data['visitor_useragent']
