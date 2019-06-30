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

map = folium.Map(location = [38.58, -99.09], zoom_start = 6)

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt,ln], popup=str(el) + " m", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map.html")