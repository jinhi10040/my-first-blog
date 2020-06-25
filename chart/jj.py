import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv',
                     parse_dates=['Date'])
countries = ['Korea, South', 'Japan', 'France', 'Canada', 'Australia']
df = df[df['Country'].isin(countries)]
df['Cases'] = df[['Confirmed', 'Recovered', 'Deaths']].sum(axis=1)
df = df.pivot(index='Date', columns='Country', values='Cases')
countries = list(df.columns)
covid = df.reset_index('Date')
covid.set_index(['Date'], inplace=True)
covid.columns = countries
populations = {'Korea, South':51269185, 'Japan':126476461 , 'France': 65273511, 'Canada':37742154, 'Australia' :25499884}

percapita = covid.copy()
for country in list(percapita.columns):
    percapita[country] = percapita[country] / populations[country] * 1000000



print(percapita["Australia"].values)