#!/usr/bin/env python
# coding: utf-8

'''
#To make 3D house
Run
get_address()
fast_overlap()
calculate_dem()
fast_plot()

make_house()

'''

import os
import fnmatch
import requests
import numpy as np
import pandas as pd
import geopandas as gpd
import rasterio
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html

from geopandas import GeoSeries
from shapely.geometry import Polygon
from rasterio.windows import Window
from rasterio.mask import mask
from codetiming import Timer

# Retrieve building coordinates

@Timer(name="decorator")
def get_address(nb='110', street='Thonetlaan', city='Antwerpen', pc='2050'):
    
    import requests
    import geopandas
    from geopandas import GeoSeries
    from shapely.geometry import Polygon
    
    #Ask for user to input address
    #nb = input("Enter house number:")
    #street = input("Enter street:")
    #city = input("Enter city:")
    #pc = input("Enter postcode:")
    #Example address
    #Eugeen de Bocklaan 14, 2900 Schoten
    
    global building_address
    building_address = (street, str(nb), city, str(pc))
    building_address = " ".join(building_address)
    
    #Check user adddress match using api
    req = requests.get(f"https://api.basisregisters.dev-vlaanderen.be/v1/adresmatch?gemeentenaam={city}&straatnaam={street}&huisnummer={nb}&postcode={pc}").json()
    
    #Retrieve objectID for users address
    objectId = req["adresMatches"][0]["adresseerbareObjecten"][0]["objectId"]
    
    #Get building geometry
    req = requests.get(f"https://api.basisregisters.dev-vlaanderen.be/v1/gebouweenheden/{objectId}").json()

    objectId = req["gebouw"]["objectId"]

    req = requests.get(f"https://api.basisregisters.dev-vlaanderen.be/v1/gebouwen/{objectId}").json()

    #Get building polygon coordinates
    global polygon
    polygon = [req["geometriePolygoon"]["polygon"]]
    
    #Convert polygon to more useful geopanda series
    t = []
    
    #Get coordinates
    for i in polygon[0]['coordinates'][0]:
        t.append(tuple(i))
    
    #Convert coordinates to Polygon format
    global house_polygon
    house_polygon = Polygon(t)
    
    #Save Polygon in geopanda series
    global gpd_df
    gpd_df = GeoSeries([house_polygon])
    
    #Get area of building
    global house_area
    #Area of the building
    house_area = gpd_df.area


# Fast overlap checker

@Timer(name="decorator")
def fast_overlap():
        
    #Set path to folder with rasters
    path = os.path.abspath('/media/becode/GOPRO2/1GEOTIFF')
    
    #Get file list
    filelist=[]
    
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".tif"):
                 filelist.append(file)
    
    global dsmfile
    global dtmfile
    
    for f in filelist:
        filepath = os.path.join(path, f)
        #Open raster and check overlap
        with rasterio.open(filepath) as src:
            #src is raster, polygon is user address
            if rasterio.coords.disjoint_bounds(src.bounds, house_polygon.bounds) == False:
                if "DSM" in src.name: dsmfile = src.name
                elif "DTM" in src.name: dtmfile = src.name


# Calculate Digital Elevation Model for building

@Timer(name="decorator")
def calculate_dem():
    
    #File paths required
    path = os.path.abspath('/media/becode/GOPRO2/1GEOTIFF')
    dsmpath = os.path.join(path, str(dsmfile))
    dtmpath = os.path.join(path, str(dtmfile))

    #Open DSM raster with mask of building shape
    with rasterio.open(dsmpath) as src:
        mask, out_transform, win = rasterio.mask.raster_geometry_mask(dataset=src, shapes=gpd_df, invert=False, crop=True, pad=False)
        #Read only pixels within the window/bounds of the building shape
        dsm = src.read(1, window = win)

    #Open DTM raster with mask of building shape
    with rasterio.open(dtmpath) as src:
        mask, out_transform, win = rasterio.mask.raster_geometry_mask(dataset=src, shapes=gpd_df, invert=False, crop=True, pad=False)
        #Read only pixels within the window/bounds of the building shape
        dtm = src.read(1, window = win)

    #Calculates raw digital elevation model (no resampling)
    global dem
    dem = dsm - dtm

# Get the height and floor area of the building

def get_height():
    #Show building height and floor area
    height = round(dem.max(), 1)
    print('The building height is:', height, 'meters')

def get_area():
    area = round(int(house_area), 1)
    print('The building floor area is:', area, 'sq meters')

# Fast 3D plot

@Timer(name="decorator")
def fast_plot():
    import plotly.graph_objects as go

    #Plot xyz of building
    fig = go.Figure(data=[go.Surface(z=dem)])

    fig.update_layout(title=str(building_address), autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))

    fig.show()

#All-in-one function to make house

@Timer(name="decorator")   
def make_house():

    get_address()
    fast_overlap()
    calculate_dem()
    fast_plot()
