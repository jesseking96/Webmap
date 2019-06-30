#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 09:36:23 2019

@author: skyking
"""

import folium
map = folium.Map(location = [38.58, -99.09], zoom_start = 6)
map.save("Map.html")