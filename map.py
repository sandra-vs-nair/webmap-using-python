# -----------------------------------------------------------
# Creating a web map using python.
#
# (C) 2020 Sandra VS Nair, Trivandrum
# email sandravsnair@gmail.com
# -----------------------------------------------------------
import folium
import pandas

data = pandas.read_csv("data/city.csv") #opening the csv file containing geographical data.
latitude=list(data["latitude"])
longitude=list(data["longitude"])
cities=list(data["city"])

#Creating a map object.
map = folium.Map(location=[latitude[0], longitude[0]],zoom_start=6,tiles="Stamen Terrain")

#Creating two feature groups.
group1 = folium.FeatureGroup(name="City names") 
group2 = folium.FeatureGroup(name="Population")

#Adding popups for cities in USA.
for lat,lon,city in zip(latitude,longitude,cities):
    group1.add_child(folium.Marker(location=[lat, lon],popup="Welcome to "+city+" !",icon=folium.Icon(color='red')))

#Adding polygons as country boundaries and color code according to population.
group2.add_child(folium.GeoJson(data=open("data/polygons.json",'r',encoding='utf-8-sig').read(),style_function=lambda x :{'fillColor':'yellow' if x['properties']['POP2005']<10000000 else 'green' if 10000000 <x['properties']['POP2005']>20000000 else 'red'}))

map.add_child(group1)
map.add_child(group2)

#Adding layer control.
map.add_child(folium.LayerControl())

#Saving as html file.
map.save("webmap.html")
