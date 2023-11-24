import pandas as pd


class ReadData:
    global data

    def __init__(self):
        self.data = pd.read_json('sample_small.json', lines=True)

    def get_df(self, doc_id):
        dataframe = pd.DataFrame(self.data, columns=['env_doc_id', 'visitor_country'])
        rslt_df = dataframe[(dataframe['env_doc_id'] == doc_id)]
        return rslt_df

    def query(self):
        df1 = self.data[['env_doc_id']]
        # item = df1.split('-')[0]
        print(df1.to_string())
        return df1
