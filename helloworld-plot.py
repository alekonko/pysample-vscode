import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px  ### for plotting the data on world map
from urllib.request import urlopen
import json

path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/05-25-2020.csv'
df = pd.read_csv(path)
df.info()
df.head()

df.drop(['FIPS', 'Admin2','Last_Update','Province_State', 'Combined_Key'], axis=1, inplace=True)
df.rename(columns={'Country_Region': "Country"}, inplace=True)
df.info()
df.head()

world = df.groupby("Country")['Confirmed','Active','Recovered','Deaths'].sum().reset_index()
world.info()
world.head()

### Find top 20 countries with maximum number of confirmed cases
top_20 = world.sort_values(by=['Confirmed'], ascending=False).head(20)
### Generate a Barplot
plt.figure(figsize=(12,10))
plot = sns.barplot(top_20['Confirmed'], top_20['Country'])

for i,(value,name) in enumerate(zip(top_20['Confirmed'],top_20['Country'])):
    plot.text(value,i-0.05,f'{value:,.0f}',size=10)
plt.show()

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
fig = px.choropleth(world, geojson=counties, locations="Country", locationmode="country names",
                    color="Confirmed", hover_name="Country", color_continuous_scale="tealgrn",
                    range_color=[1,1000000], title="Countries with Confirmed cases" )

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#
#fig.to_image("conco.png")


fig.show()
