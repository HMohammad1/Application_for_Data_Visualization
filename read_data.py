import pandas as pd


class ReadData:
    global df

    def __init__(self):
        global df
        df = pd.read_json('sample_small.json', lines=True)
        dataframe = pd.DataFrame(df, columns=['env_doc_id', 'visitor_country'])
        rslt_df = dataframe[(dataframe['env_doc_id'] == '140224132818-2a89379e80cb7340d8504ad002fab76d')]
        cool = len(dataframe[(dataframe['env_doc_id'] == '140224132818-2a89379e80cb7340d8504ad002fab76d') & (dataframe['visitor_country']== 'TH')])
        x = rslt_df['visitor_country'].value_counts()
        # print(dataframe.to_string())
        print(x)

    def query(self):
        df1 = df[['env_doc_id']]
        # item = df1.split('-')[0]
        print(df1)
        return df1
