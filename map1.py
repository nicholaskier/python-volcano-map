import folium
map = folium.Map(location=[30.322016, -97.681918], zoom_start=6, titles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi! I am a marker!", icon=folium.Icon(color="green")))
map.add_child(fg)
map.save("Map1.html")