import pulldata

chosen_columns = ['title','category','source']
url = "https://github.com/BuzzFeedNews/2018-12-fake-news-top-50/raw/master/data/top_2018.csv"

# Run Functions from pulldata.py
print(pulldata.test_create_dataframe(chosen_columns,url))
