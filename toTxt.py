import pandas as pd

df = pd.io.parsers.read_csv("sample_twitter_data_2019-04-20_to_2019-04-20.csv")
sliceData = df.loc[:, 'text']    # Country 열만 자름
print(sliceData)
sliceData.to_csv('newSliced.txt', index=False)