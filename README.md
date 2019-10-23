# HW2 - Using Functions

*test_create_dataframe.py* contains URL and selected columns. This module calls the function that turns this data to a dataframe and does the checks

*pulldata.py* houses all of the functions

Create a python module (a file with extension ‘.py’) with the following functions:

1. (1 points) Write a python reads creates a dataframe from a URL that points to a CSV file such as the pronto data or CSVs in data.gov.

1. (6 points) Create the function test_create_dataframe that takes as input: (a) a pandas DataFrame and (b) a list of column names. The function returns True if the following conditions hold:

  - The DataFrame contains only the columns that you specified as the second argument.
  - The values in each column have the same python type
  - There are at least 10 rows in the DataFrame.
