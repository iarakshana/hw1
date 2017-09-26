#!/usr/bin/env python 


import requests
import pandas as pd
import numpy as np
import scipy
import geopandas as gpd
import shapely
import fiona
import folium
from shapely.geometry import Point
import os, sys
import psycopg2
import json


import matplotlib 
# matplotlib.use('Agg')

os.system('curl https://www2.census.gov/geo/tiger/TIGER2016/TRACT/tl_2016_17_tract.zip -o il_tracts.zip')

if not os.path.exists("il_tracts.zip"):
    print("Tract file is missing! curl failed! abort!")
    sys.exit()


import zipfile
with zipfile.ZipFile("il_tracts.zip", 'r') as z:
    z.extractall("il_tracts")


gdf = gpd.read_file("il_tracts/tl_2016_17_tract.shp")
gdf = gdf.loc[gdf["ALAND"] > 0].copy()



gdf.rename(columns = {"COUNTYFP" : "county", "TRACTCE" : "tract"}, inplace = True)
gdf["tract"] = gdf.tract.astype(int)
gdf["county"] = gdf.county.astype(int)
gdf["density"] = gdf.county.astype(int)


il_ba = requests.get("http://api.census.gov/data/2014/acs5/profile?for=tract:*&in=state:17+county:*&get=NAME,DP02_0067PE,DP02_0122E").json()
il_ba_df = pd.DataFrame(data = il_ba[1:], columns = ["name", "ba", "pop", "state", "county", "tract"])#[["county", "tract", "ba", "pop"]]
il_ba_df["county"] = il_ba_df.county.astype(int)
il_ba_df["tract"] = il_ba_df.tract.astype(int)
il_ba_df["ba"] = il_ba_df.ba.str.replace("-", "0").astype(float)
il_ba_df["pop"] = il_ba_df["pop"].str.replace("-", "0").astype(float)


gdf = gdf.merge(il_ba_df, on = ["county", "tract"])
gdf["density"] = gdf["pop"] / gdf.area



ax = gdf["ba"].plot(kind = "hist", weights = gdf["pop"], normed = True)
ax.set_xlabel("BA Fraction")
ax.get_figure().savefig('ba_frac.pdf', bbox_inches='tight', pad_inches=0.1)


pt = Point(-87.6298, 41.8781)
circ = pt.buffer(1.25)
ax = gdf[gdf.intersects(circ)].plot(column = "density", linewidth = 0, scheme = "quantiles", k = 9, cmap = "nipy_spectral")
ax.set_axis_off()
ax.get_figure().savefig('density.pdf', bbox_inches='tight', pad_inches=0.1)



colormap = folium.LinearColormap(("orange", "white", "purple"), vmin = 0, vmax = 50, caption = "Percent Bachelors")

m = folium.Map([41.7943,-87.5907], zoom_start = 13, tiles = "cartodbpositron", max_zoom = 14, min_zoom = 6, attr = "")

folium.GeoJson(gdf,
               style_function = lambda feature: { 
                  'fillColor': colormap(feature['properties']["ba"]) if feature["properties"]["ba"] else "k",
                  "color" : "k", "weight" : 0.3, "fillOpacity" : 0.4 if feature["properties"]["ba"] else 0,
               }).add_to(m)

colormap.add_to(m)
# m.save('ba_folium.html')


good = ["{:<12} :: {:10}".format("python",    sys.version         ),  
        "{:<12} :: {:10}".format("requests",  requests.__version__),  
        "{:<12} :: {:10}".format("pandas",    pd.__version__      ), 
        "{:<12} :: {:10}".format("geopandas", gpd.__version__     ), 
        "{:<12} :: {:10}".format("psycopg2",  psycopg2.__version__), 
        "{:<12} :: {:10}".format("json",      json.__version__    ), 
        "{:<12} :: {:10}".format("shapely",   shapely.__version__ ), 
        "{:<12} :: {:10}".format("fiona",     fiona.__version__   ), 
        "{:<12} :: {:10}".format("numpy",     np.__version__      ), 
        "{:<12} :: {:10}".format("scipy",     scipy.__version__   )
        ]

print("\n".join(good))
print ("Congrats! Check-out looks great!")
with open("test-suite.txt", "w") as out: out.write("\n".join(good))


