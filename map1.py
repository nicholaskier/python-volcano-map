import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[30.322016, -97.681918], zoom_start=6, titles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    # zip function distributes items one by one from each list
    fg.add_child(folium.Marker(location=[lt, ln], popup="Elevation: " + str(el) + "m", icon=folium.Icon(color="green")))

map.add_child(fg)
map.save("Map1.html")