import pandas as pd 
import numpy as np 

#need to define data frame
#need to define column names
#have the user define the data source

#Use for running 
#chosen_columns = ['title','category','source']
#url = "https://github.com/BuzzFeedNews/2018-12-fake-news-top-50/raw/master/data/top_2018.csv"

# import data from Buzzfeed Data GitHub on Top 2018 Fake New Articles
def readindata(chosen_columns,url):
    return pd.read_csv(url,usecols=chosen_columns)

# Define Test Funtions
def checkcolumnstest(chosen_columns,df):
    if not all([item in chosen_columns for item in df.columns]):
        raise ValueError('Columns do not match')
    pass

def checktypestest(df):
    for i in df:
        if not df.dtypes[1] == df.dtypes[i]:
            raise ValueError('Types do not match')
        pass

def checkrowstest(df):
    if not df.shape[0] >= 10:
        raise ValueError('Less than 10 rows')
    pass

# Run Test Functions
def test_create_dataframe(chosen_columns, url):
    df = readindata(chosen_columns,url)
    checkcolumnstest(chosen_columns,df)
    checktypestest(df)
    checkrowstest(df)
    return True
    
