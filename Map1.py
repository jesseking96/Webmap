#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 09:36:23 2019

@author: skyking
"""

import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elev):
    if elev < 1000:
        return 'green'
    elif 1000 <= elev < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location = [38.58, -99.09], zoom_start = 6)

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius = 6, popup=str(el) + " m", fill_color=color_producer(el), color = "grey", fill_opacity = 0.7))

fg.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(),
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))   
    
map.add_child(fg)

map.save("Map.html")

