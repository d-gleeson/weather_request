#Inititialise database of weather data
import json
import os
import pandas as pd

from sqlalchemy import create_engine
engine = create_engine('sqlite:///metweatherdata.db')

with open(os.path.join('json_files','sample.json'),'r') as file:
	data = json.load(file)

df = pd.DataFrame(data['SiteRep']['Wx']['Param'])
cols = list(df.columns)
cols[0] = 'weather_variable'
df.columns = cols

#df.to_sql('units', engine, index=False)

records = data['SiteRep']['DV']['Location']
periods = [record['Period'] for record in records]

site_list = [location for location in records]

df = pd.DataFrame(site_list)
df.drop('Period', axis=1, inplace = True)
df.to_sql('sites', engine, index=False)

