# Video3:-A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
import pandas as pd
diet = {"Fruits":["Apple","Kiwi","Oranges"], "Vegetables":["Spinach","Brocolli","Cabbage"]}
diet_series = pd.DataFrame(diet)
print(diet_series)

#output:-
#     Fruits  Vegetables
# 0    Apple    Spinach
# 1     Kiwi   Brocolli
# 2  Oranges    Cabbage

#----------------------------------------------------------------------------------------------------------------------------------------------------

#Pandas use the loc attribute to return one or more specified row(s) and pass the index.
print(diet_series.loc[0])
#This example returns a Pandas Series.
# Fruits          Apple
# Vegetables    Spinach

#This example when using [], the result is a Pandas DataFrame.
print(diet_series.loc[[0]])
#   Fruits  Vegetables
# 0  Apple    Spinach

#We can also return more than one row by passing a list of index.
print(diet_series.loc[[0,1]])
#   Fruits  Vegetables
# 0  Apple    Spinach
# 1   Kiwi   Brocolli

#----------------------------------------------------------------------------------------------------------------------------------------------------

#Named Index:- With the index argument, you can name your own indexes.
import pandas as pd
diet = {"Fruits":["Apple","Kiwi","Oranges"], "Vegetables":["Spinach","Brocolli","Cabbage"]}
diet_series = pd.DataFrame(diet, index=["Day1","Day2","Day3"])
print(diet_series)

# output:-
#        Fruits  Vegetables
# Day1    Apple    Spinach
# Day2     Kiwi   Brocolli
# Day3  Oranges    Cabbage

#----------------------------------------------------------------------------------------------------------------------------------------------------

#Locate Named Indexes:- Use the named index in the loc attribute to return the specified rows.

print(diet_series.loc["Day1"])
#Output in Series.
# Fruits          Apple
# Vegetables    Spinach

print(diet_series.loc[["Day1"]])
#Output in DataFrame.
#      Fruits  Vegetables
# Day1  Apple    Spinach

#----------------------------------------------------------------------------------------------------------------------------------------------------

#Load Files Into a DataFrame:- If your data sets are stored in a file, Pandas can load them into a DataFrame.
#Let us load the data from csv file into dataframe with filename = data.csv
import pandas as pd
load_file = pd.read_csv('data.csv')  #when file is in local path/folder
print(load_file)
