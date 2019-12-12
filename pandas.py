
'''What is Pandas?
Pandas is an opensource library that allows to you perform data manipulation in Python. 
Pandas library is built on top of Numpy, meaning Pandas needs Numpy to operate.
Pandas provide an easy way to create, manipulate and wrangle the data.
Pandas is also an elegant solution for time series data.'''
'''
Easily handles missing data
It uses Series for one-dimensional data structure and DataFrame for multi-dimensional data structure
It provides an efficient way to slice the data
It provides a flexible way to merge, concatenate or reshape the data
It includes a powerful time series tool to work with'''
'''
in a nutshell, Pandas is a useful library in data analysis.
It can be used to perform data manipulation and analysis.
Pandas provide powerful and easy-to-use data structures, as well as the means to quickly perform operations on these structures.'''

'''
What is a data frame?
A data frame is a two-dimensional array, with labeled axes (rows and columns). A data frame is a standard way to store data.

Data frame is well-known by statistician and other data practitioners. A data frame is a tabular data, 
with rows to store the information and columns to name the information.
For instance, the price can be the name of a column and 2,3,4 the price values.'''

dic = {'Name': ["John", "Smith"], 'Age': [30, 40]}
pd.DataFrame(data=dic)				
  Age	Name
0	30	John
1	40	Smith


#Date ranges(gives date swquence)
dates_d = pd.date_range('20300101', periods=6, freq='D')
print('Day:', dates_d)
Day: DatetimeIndex(['2030-01-01', '2030-01-02', '2030-01-03', '2030-01-04', '2030-01-05', '2030-01-06'], dtype='datetime64[ns]', freq='D')

  # Months(date range by month wise)
dates_m = pd.date_range('20300101', periods=6, freq='M')
print('Month:', dates_m)
Output

Month: DatetimeIndex(['2030-01-31', '2030-02-28', '2030-03-31', '2030-04-30','2030-05-31', '2030-06-30'], dtype='datetime64[ns]', freq='M')
