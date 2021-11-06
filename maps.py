import folium
#map=folium.Map(location=[28.5011226,77.4099794],zoom_start=12)
map2=folium.Map(location=[27.2046,77.4977],zoom_start=12)
#folium.Marker([28.704059,77.102490],popup='Delhi').add_to(map)
folium.Marker([27.2046,77.4977],popup='Delhi').add_to(map2)
#folium.Marker([28.5011226,77.4099794],popup='Python.Hub').add_to(map)
folium.Marker([27.2046,77.4977],popup='Python.Hub').add_to(map2)
folium.PolyLine(locations=[(27.2046,77.4977),(27.2046,77.4977)],line_opacity=0.5).add_to(map2)
map2.save("map2.html")
map2