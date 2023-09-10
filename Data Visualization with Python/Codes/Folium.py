import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
from pywaffle import Waffle
import seaborn as sns

#Reading Dataframe
df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')

#Show first five rows of the data
des=df_can.describe(include = "all")
print(df_can)
print(df_can.columns)


#Folium
import folium
from folium.plugins import MarkerCluster

world_map = folium.Map(location=[56.130,-106.35],
                       zoom_start=4,
                       tiles='Stamen Terrain') #Stamen Toner)

#Feature group(circle on locaton)


location=[
    {"location":[45.4215, -75.6989],"popup":"Ottawa"},
    {"location":[53.5461, -113.4938],"popup":"Edmonton"},
    {"location":[49.2827, -123.1207],"popup":"Vancouver"},
    {"location":[51.253,-85.3232],"popup":"Ontario"}]

for loc in location:
    folium.Marker(location=loc["location"],popup=loc["popup"]).add_to(world_map)
    

#Feature group(circle on locaton)
ontario=folium.map.FeatureGroup()
ontario.add_child(folium.features.CircleMarker([51.253,-85.3232],radius=5,
                                               color='red',fill_color="red"))

#Adding feature group to world map
world_map.add_child(ontario)

#Marker
folium.Marker(location=[51.253,-85.3232],popup='Ontario').add_to(world_map)
world_map.save("worldmap.html")

marker_cluster=MarkerCluster().add_to(world_map)

for loc in location:
    folium.Marker(location=loc["location"],popup=loc["popup"]).add_to(marker_cluster)
marker_cluster.save("canada.html")


#Chloropleth Map
world_geo = r'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/world_countries.json' # geojson file

# create a plain world map
world_map1 = folium.Map(location=[0, 0], zoom_start=2)
world_map1.choropleth(
    geo_data=world_geo,
    data=df_can,
    columns=['Country', 'Total'],
    key_on='feature.properties.name',
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Immigration to Canada'
)
world_map1.save("worldmap1.html")

