dates_m = pd.date_range('20300101', periods=6, freq='M')
print('Month:', dates_m)
Output

Month: DatetimeIndex(['2030-01-31', '2030-02-28', '2030-03-31', '2030-04-30','2030-05-31', '2030-06-30'], dtype='datetime64[ns]', freq='M')  


df = pd.DataFrame(random,
                  index=dates_m,
                  columns=list('ABCD'))
3) Using head function
df.head(3)
              A          	B	         C       	D
2030-01-31	1.139433	1.318510	-0.181334	1.615822
2030-02-28	-0.081995	-0.063582	0.857751	-0.527374
2030-03-31	-0.519179	0.080984	-1.454334	1.314947


4) Using tail function
df.tail(3)

df.describe()
         A	       B	      C       	D
count	6.000000	6.000000	6.000000	6.000000
mean	0.002317	0.256928	-0.151896	0.467601
std	0.908145	0.746939	0.834664	0.908910
min	-0.935888	-0.731787	-1.454334	-0.527374
25%	-0.643880	-0.050621	-0.468272	-0.327419
50%	-0.300587	0.034624	-0.189118	0.436883
75%	0.802237	0.732131	0.421296	1.178404
max	1.139433	1.318510	0.857751	1.615822


df['A']

2030-01-31   -0.168655
2030-02-28    0.689585
2030-03-31    0.767534
2030-04-30    0.557299
2030-05-31   -1.547836
2030-06-30    0.511551
Freq: M, Name: A, dtype: float64
      
df[['A', 'B']]. 				
A	B
2030-01-31	-0.168655	0.587590
2030-02-28	0.689585	0.998266
2030-03-31	0.767534	-0.940617
2030-04-30	0.557299	0.507350
2030-05-31	-1.547836	1.276558
2030-06-30	0.511551

The code below returns the first three rows
### using a slice for row
df[0:3]	
A	B	C	D
2030-01-31	-0.168655	0.587590	0.572301	-0.031827
2030-02-28	0.689585	0.998266	1.164690	0.475975
2030-03-31	0.767534	-0.940617	0.227255	-0.341532


The loc function is used to select columns by names. 
As usual, the values before the coma stand for the rows and after refer to the column. 
You need to use the brackets to select more than one column.

## Multi col
df.loc[:,['A','B']]	
A	B
2030-01-31	-0.168655	0.587590
2030-02-28	0.689585	0.998266
2030-03-31	0.767534	-0.940617
2030-04-30	0.557299	0.507350
2030-05-31	-1.547836	1.276558
2030-06-30	0.511551	1.572085
  
  
There is another method to select multiple rows and columns in Pandas. You can use iloc[]. 
This method uses the index instead of the columns name. The code below returns the same data frame as above

df.iloc[:, :2]
  
  
 
Drop a column
You can drop columns using pd.drop()

df.drop(columns=['A', 'C'])								


import numpy as np
df1 = pd.DataFrame({'name': ['John', 'Smith','Paul'],
                     'Age': ['25', '30', '50']},
                    index=[0, 1, 2])
df2 = pd.DataFrame({'name': ['Adam', 'Smith' ],
                     'Age': ['26', '11']},
                    index=[3, 4])  
Finally, you concatenate the two DataFrame

df_concat = pd.concat([df1,df2]) 
df_concat
Age	name
0	25	John
1	30	Smith
2	50	Paul
3	26	Adam
4	11	Smith

df_concat.drop_duplicates('name')
You can sort value with sort_values
df_concat.sort_values('Age')
df_concat.rename(columns={"name": "Surname", "Age": "Age_ppl"})
