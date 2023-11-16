import pandas as pd


class ReadData:
    global df

    def __init__(self):
        global df
        df = pd.read_json('sample_small.json', lines=True)
        dataframe = pd.DataFrame(df, columns=['env_doc_id', 'visitor_country'])
        rslt_df = dataframe[(dataframe['env_doc_id'] == '100528230144-02f68abad20e46449b72482dce6a06a4')]
        print(dataframe.to_string())

    def query(self):
        df1 = df[['env_doc_id']]
        # item = df1.split('-')[0]
        print(df1)
        return df1
