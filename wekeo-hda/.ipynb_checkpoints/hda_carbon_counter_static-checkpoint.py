import os,sys, time
import base64
import shutil
import json
import urllib.parse
from hda_api_functions import *
import netCDF4
import numpy as np

# Initialisation
fn = './ressources/cams73_latest_co2_flux_satellite_mm_201912.nc'
ds = netCDF4.Dataset(fn)
print(ds)
print ("------------------------------------------------------------")
print ("variables are: =>")
#for i in ds.variables:
#    print (i, ds.variables[i].units, ds.variables[i].shape)
print ("------------------------------------------------------------")
#for i in ds.variables:
#   print (ds.variables[i])
#"npor"    
long = ds['longitude'][:]
lat = ds['latitude'][:]

long_max = 10
long_min = 0
index_long_max = np.where(long_max <= long)[0]
print("index_long_max")
print(index_long_max)
print("stat")
print(index_long_max[0], long[index_long_max[0]])


area = ds['area'][0:10, 0:10]
lsf = ds['lsf'][3:6,3:4]
flux_foss = ds['flux_foss'][:]
print ("------------------------------------------------------------")
print ("flux_foss is: =>")
print (flux_foss)
print ("------------------------------------------------------------")
print ("lsf is: =>")
print (lsf)
print ("------------------------------------------------------------")
print ("area is: =>")
print (area)
print ("------------------------------------------------------------")
print ("long is: =>")
print (long)
print ("------------------------------------------------------------")
print ("lat is: =>")
print (lat)

