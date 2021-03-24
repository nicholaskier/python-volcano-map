import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_producer(elevation):
    if elevation < 1500:
        return 'green'
    elif 1500 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


html = """
<h2><a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a></h2>
Height = %s m
"""

map = folium.Map(location=[30.322016, -97.681918], zoom_start=6, titles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, name in zip(lat, lon, elev, name):
    # zip function distributes items one by one from each list
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=color_producer(el))))

map.add_child(fg)
map.save("Map1.html")
