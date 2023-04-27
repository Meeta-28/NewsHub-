import pandas as pd
from pandas_profiling import ProfileReport

df=pd.read_csv('articles.csv')
print(df)

#generate a report
profile = ProfileReport(df) #,minimal=True
profile.to_file(output_file="articles.html")


