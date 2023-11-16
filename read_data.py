import pandas as pd


class ReadData:
    global df

    def __init__(self):
        global df
        df = pd.read_json('sample_small.json', lines=True)
        dataframe = pd.DataFrame(df, columns=['env_doc_id', 'visitor_country'])
        rslt_df = dataframe[(dataframe['env_doc_id'] == '130603065734-ceaa7b2404edf4a85e5563d0860e9b65')]
        cool = len(dataframe[(dataframe['env_doc_id'] == '140223031538-3e15e64ec39fbe82dabe39ac43dc4a63')])
        x = rslt_df['visitor_country'].value_counts()
        # print(dataframe.to_string())
        print(rslt_df.to_string())

    def query(self):
        df1 = df[['env_doc_id']]
        # item = df1.split('-')[0]
        print(df1)
        return df1
