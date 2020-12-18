import os,sys, time
import base64
import shutil
import json
import urllib.parse
from hda_api_functions import *

import requests, warnings
warnings.filterwarnings('ignore')

dataset_id = "EO:ECMWF:DAT:CAMS_GREENHOUSE_GAS_FLUXES"

username = 'mattaqi'
password = 'masma3991'
api_key = generate_api_key(username, password)
download_dir_path = os.getcwd()

hda_dict = init(dataset_id, api_key, download_dir_path)
hda_dict = get_access_token(hda_dict)
hda_dict = acceptTandC(hda_dict)

data = {
  "datasetId": "EO:ECMWF:DAT:CAMS_GREENHOUSE_GAS_FLUXES",
  "multiStringSelectValues": [
    {
      "name": "variable",
      "value": [
        "carbon_dioxide"
      ]
    },
    {
      "name": "year",
      "value": [
        "2019"
      ]
    },
    {
      "name": "month",
      "value": [
        "12"
      ]
    },
    {
      "name": "quantity",
      "value": [
        "surface_flux"
      ]
    },
    {
      "name": "version",
      "value": [
        "latest"
      ]
    },
    {
      "name": "input_observations",
      "value": [
        "satellite"
      ]
    },
    {
      "name": "time_aggregation",
      "value": [
        "daily_mean"
      ]
    }
  ],
  "stringChoiceValues": [
    {
      "name": "format",
      "value": "tgz"
    }
  ]
}

hda_dict = get_job_id(hda_dict, data)

hda_dict = get_results_list(hda_dict)

hda_dict = get_order_ids(hda_dict)

hda_dict = download_data(hda_dict, file_extension='.zip')
