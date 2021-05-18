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
#print(grouped_by_month)
# save to CSV
#grouped_by_month.to_csv('output/monthwise_total_confirmed.csv')


#q2 total death per state and whole country in 2020
grouped_by_state = df_2020.groupby(['State/UnionTerritory']).sum()['Deaths']
total_death_at_country_level = grouped_by_state.sum()

deaths = pd.DataFrame([['Sum_Total_for_Country',total_death_at_country_level]],
                        columns=['State/UnionTerritory','Deaths'])


# check results
print(grouped_by_state)
print(deaths)
grouped_by_state.to_csv('output/grouped_by_state_q2.csv')

#q3 average covid cases for all states in april 2020 and 2021
df_2021 = covid_india_df[covid_india_df['Date'].dt.year == 2021]
df_2021['Month'] = pd.to_datetime(df_2021['Date']).dt.month

grouped_by_month_2020 = df_2020.groupby(['Month','State/UnionTerritory']).mean()
grouped_by_month_2021 = df_2021.groupby(['Month','State/UnionTerritory']).mean()
grouped_by_month_2020.reset_index(inplace=True)
grouped_by_month_2021.reset_index(inplace=True)


april_averages  = grouped_by_month_2020.loc[grouped_by_month_2020['Month'] == "4"]
april_averages_2021  = grouped_by_month_2021.loc[grouped_by_month_2021['Month'] == "4"]

print(april_averages_2021)

#q4 date with highest covid cases in 2020 and 2021
#set date to be the index
df_2020.set_index('Date',drop=False)
df_2021.set_index('Date',drop=False)
# highest confirmed cases
highest_confirmed_2020 = df_2020['Confirmed']
highest_confirmed_2021 = df_2021['Confirmed']

print(highest_confirmed_2020)
print("Highest confirmed 2021 >>>>>>>>>>>>>>>>>>>>>>>>>>>")
#q5 monthwise total male vaccinated in every state and also total covid cases per state for 2021
# covid cases per state per month
grouped_by_month_2021_cases = df_2021.groupby(['Month','State/UnionTerritory']).sum()['Confirmed']
# vaccine data
df_2021 = vaccine_df[vaccine_df['Updated On'].dt.year == 2021]
df_2021['Month'] = pd.to_datetime(df_2021['Date']).dt.month
grouped_by_month_state_2021_maleVaccinated = df_2021.groupby(['Month','State']).sum()['Male(Individuals Vaccinated)']

# preview results
print(grouped_by_month_state_2021_maleVaccinated)
grouped_by_month_2021_cases.to_csv('output/total_confirmed_cases_2021_by_month_and_state.csv')
grouped_by_month_state_2021_maleVaccinated.to_csv('output/males_vaccinated_by_month_and_state.csv')