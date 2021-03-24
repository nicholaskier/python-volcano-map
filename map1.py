import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

map = folium.Map(location=[30.322016, -97.681918], zoom_start=6, titles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat, lon):
    # zip function distributes items one by one from each list
    fg.add_child(folium.Marker(location=[lt, ln], popup="Hi! I am a volcano!", icon=folium.Icon(color="green")))

map.add_child(fg)
map.save("Map1.html")