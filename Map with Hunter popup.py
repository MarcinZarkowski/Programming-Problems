#Marcin Zarkowski
#24225410
#makes map with marker on Hunter College

import folium

Map=folium.Map(location=[40.75, -74.125],zoom_start=2)
folium.Marker(location=[40.768731, -73.964915], popup= "Hunter College").add_to(Map)
Map.save(outfile="nycMap.html")
