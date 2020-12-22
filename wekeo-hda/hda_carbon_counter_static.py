import os,sys, time
import base64
import shutil
import json
import urllib.parse
from hda_api_functions import *
import netCDF4
import numpy as np

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

# Initialisation
fn = './ressources/cams73_latest_co2_flux_satellite_mm_201912.nc'
ds = netCDF4.Dataset(fn)

print(ds)
print ("------------------------------------------------------------")
print ("variables are: =>")
#for i in ds.variables:
#    print (i, ds.variables[i].units, ds.variables[i].shape)
print ("------------------------------------------------------------")
for i in ds.variables:
   print (i, ds.variables[i])
print ("------------------------------------------------------------")
#"npor"    
long = ds['longitude'][:]
print ("list of  longitude is: =>")
print(long)
lat = ds['latitude'][:]
print ("list of  latitude is: =>")
print(lat)

print ("----------------------port strasbourg--------------------------------------")

# port strasbourg
# 48.5384° N, 7.7944° E
long_str_max = 11.25
long_str_min = 7.5

lat_str_max = 50.21052632
lat_str_min = 48.31578947

index_long_min_str = np.where(long_str_min <= long)[0]
index_long_max_str = np.where(long <= long_str_max)[0]
index_long_str = intersection(index_long_min_str, index_long_max_str)

print("index_long_min_str")
print(index_long_min_str)

print("index_long_max_str")
print(index_long_max_str)

print("index_long_str")
print(index_long_str)

index_lat_min_str = np.where(lat_str_min <= lat)[0]
index_lat_max_str = np.where(lat <= lat_str_max)[0]
index_lat_str = intersection(index_lat_min_str, index_lat_max_str)

print("index_lat_min_str")
print(index_lat_min_str)

print("index_lat_max_str")
print(index_lat_max_str)

print("index_lat_str")
print(index_lat_str)

print ("---------------------end --------------------------------------")

# print ("----------------------port klaipeda--------------------------------------")

#port klaipeda
# 55.7063° N, 21.1251° E
long_kla_max = 22.5
long_kla_min = 18.75
lat_kla_max = 55.89473684
lat_kla_min = 54.


# print ("---------------------end --------------------------------------")


'''
long_max = 10
long_min = 0
index_long_max = np.where(long_max <= long)[0]
print("index_long_max")
print(index_long_max)
print("stat")
print(index_long_max[0], long[index_long_max[0]])
'''

area = ds['area'][:]
lsf = ds['lsf'][:]
flux_foss = ds['flux_foss'][:]


