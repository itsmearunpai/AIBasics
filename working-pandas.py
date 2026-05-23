import pandas as pd

#load my csv file into a dataframe
df = pd.read_csv('dataset/temperature_50_records.csv')
#print(df.head())    


#Print first column of the dataframe
#print(df['EST'][0])
#Access multiple columns
#print(df[['EST', 'Temperature','Humidity']].head())

#Get the max temperature
#print(df['Temperature'].max())

#Get the EST for the event when it Rains
#print(df['EST'][df['Events'] == 'Rain'].head(n=10))

df['Arun'] = df['Temperature'] + 10

#print(df['Arun'].head())

#Get the mean of the wind speed
print(df['WindSpeedMPH'].mean())

#Fill NaN values with 0
df.fillna(0, inplace=True)

print(df.head())
