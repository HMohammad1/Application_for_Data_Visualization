import pandas as pd


class ReadData:
    global data

    def __init__(self):
        self.data = pd.read_json('sample_600k_lines.json', lines=True)

    def get_country_df(self, doc_id):
        dataframe = pd.DataFrame(self.data, columns=['env_doc_id', 'visitor_country'])
        rslt_df = dataframe[(dataframe['env_doc_id'] == doc_id)]
        return rslt_df

    def get_reader_df(self):
        dataframe = pd.DataFrame(self.data, columns=['visitor_uuid', 'event_readtime'])
        rslt_df = dataframe[pd.notna(dataframe['event_readtime'])]
        return rslt_df

    def get_visitor_df(self, doc_id):
        # return all viewer ID's of the doc ID given
        return self.data.loc[self.data['env_doc_id'] == doc_id, 'visitor_uuid'].astype(str)

    def get_visitor_doc_id(self, visitor):
        # return all the doc ID's for the given viewer but get rid of duplicates
        doc = self.data[self.data['visitor_uuid'] == visitor]['env_doc_id'].astype(str)
        return set(doc.unique())

