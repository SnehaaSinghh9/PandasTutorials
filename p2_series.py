#Video2:- Panda Series is like a column in a table. It is like a 1D array which holds data of any type.
#Let us create a simple Panda series.

#1. 1-D
import pandas as pd 
list1 =["Sneha", 21, "F"]
series1=pd.Series(list1)
print(series1)

#The output is in table form with the first column as an index of each element of the series and the second column as the actual element.
# 0    Sneha
# 1       21
# 2        F

#We can access the elements of the series by using the index which is called "labeling".
#Labeling - label can be used to access a specified value.
import pandas as pd 
list1 =["Sneha", 21, "F"]
series1=pd.Series(list1)
print(series1[0])
print(series1[1])
print(series1[2])

#output:-
# Sneha
# 21
# F

#By default labels are 0,1,2,....
#We can create our own labels by using "create label"
import pandas as pd 
list1 =["Sneha", 21, "F"]
series1=pd.Series(list1,index=["Name","Age","Gender"])
print(series1)
print(series1["Name"])
print(series1["Age"])
print(series1["Gender"])

#output:- 
# Name      Sneha
# Age          21
# Gender        F
# dtype: object
# Sneha
# 21
# F

#We can also use a key-value pair like a dictionary instead of a list to create a series.
import pandas as pd 
calorie={"day1":420,"day2":380,"day3":560}
cal_series = pd.Series(calorie)
print(cal_series)

#Here, the keys of the dictionary become the labels.

# output:-
# day1    420
# day2    380
# day3    560

#We can also create a series using particular values from the given list or dictionary.
#Example:- We want a seies for only day3 and day1. 
#For this use labeling and pass only the required labels in the required order.
import pandas as pd 
calorie={"day1":420,"day2":380,"day3":560}
cal_series = pd.Series(calorie, index=["day3","day1"])
print(cal_series)

# output:-
# day3    560
# day1    420

#----------------------------------------------------------------------------------------------------------------------------------------------------

#2. For multidimensional , we use "DataFrame".
#Data sets in Pandas are usually multidimensional tables, and they are called as DataFrames.

#Series --> Column   and  DataFrames --> Table

#Let us create a DataFrames from 2 Series (1-D Arrays).
import pandas as pd 
diet = {"Fruits":["Apple","Kiwi","Oranges"], "Vegetables":["Spinach","Brocolli","Cabbage"]}
diet_series = pd.DataFrame(diet)
print(diet_series)

#The output is in table form with the first column as an index of each element of the series and the second and third columns with the key as the title and value as the actual element.
#     Fruits  Vegetables
# 0    Apple    Spinach
# 1     Kiwi   Brocolli
# 2  Oranges    Cabbage
