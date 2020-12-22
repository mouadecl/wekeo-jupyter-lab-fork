import os,sys, time
import base64
import shutil
import json
import urllib.parse
from hda_api_functions import *
import netCDF4


import requests, warnings
warnings.filterwarnings('ignore')

dataset_id = "EO:ECMWF:DAT:CAMS_GREENHOUSE_GAS_FLUXES"

username = 'mattaqi'
password = 'masma3991'
api_key = generate_api_key(username, password)
download_dir_path = os.getcwd()

# Initialisation
fn = './ressources/cams73_latest_co2_flux_satellite_mm_201910.nc'
ds = netCDF4.Dataset(fn)
long = ds['longitude']
lat = ds['latitude']

print (long)
print (lat)
for i in ds.variables:
    print (i, ds.variables[i].units, ds.variables[i].shape)