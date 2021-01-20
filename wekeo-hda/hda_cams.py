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
#fn = './ressources/cams73_latest_co2_conc_satellite_inst_202008.nc'
fn = './ressources/cams73_latest_co2_flux_satellite_mm_201912.nc'
ds = netCDF4.Dataset(fn)

print(ds)
print ("------------------------------------------------------------")
print ("variables are: =>")
#for i in ds.variables:
#    print (i, ds.variables[i].units, ds.variables[i].shape)
print ("------------------------------------------------------------")
for i in ds.variables:   
    print ("------------------------------start of variable----------------------------")
    print (i)
    print (ds.variables[i])
    print (ds.variables[i][:])
    print ("------------------------------end of variable----------------------------")  
