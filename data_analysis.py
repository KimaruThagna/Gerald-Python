import pandas as pd
import datetime as dt
covid_india_df = pd.read_csv('csv/covid_19_india.csv')
vaccine_df = pd.read_csv('csv/covid_vaccine_statewise.csv')
# preliminary inspection of the data 
# print(covid_india_df.tail(10))
# print(covid_india_df.describe())
# print(vaccine_df.head(10))

# data preprocessing for possible missing values
columns = ["ConfirmedIndianNational", "ConfirmedForeignNational", "Cured", "Deaths", "Confirmed"]
for col in columns:
    covid_india_df.loc[covid_india_df[col] == "-", col] = 0
  
# preprocess date column
covid_india_df['Date'] = pd.to_datetime(covid_india_df['Date'])
        
#q1 monthwise total for confirmed cases per state in 2020
df_2020 = covid_india_df[covid_india_df['Date'].dt.year == 2020]
# extract month
df_2020['Month'] = pd.to_datetime(df_2020['Date']).dt.month
grouped_by_month = df_2020.groupby(['Month']).sum()['Confirmed']
# check grouping
print(grouped_by_month)

#q2 