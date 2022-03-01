import pandas
import folium

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
ele = list(data["ELEV"])

def col(op):
    if op < 1000:
        return 'green'
    elif op >= 1000 and op <= 2000:
        return 'orange'
    elif op > 2000:
        return 'red'
    


map = folium.Map(location= [38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Valcanoes")

#for lt, ln, el in zip(lat, lon, ele):
    #map.add_child(folium.Marker(location=[lt, ln], popup=str(object=el), icon=folium.Icon(color=col(el))))

for lt, ln, el in zip(lat, lon, ele):
    fgv.add_child(folium.Circle(location=[lt, ln], radius= 6, popup=str(object=el), fill_color=col(el), color=col(el), fill_opacity=0.7))      

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] <10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))



map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())
map.save("Map1.html")