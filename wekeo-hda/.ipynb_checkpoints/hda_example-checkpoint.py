import os,sys, time
import base64
import shutil
import json
import urllib.parse
from hda_api_functions import *

import requests, warnings
warnings.filterwarnings('ignore')

dataset_id = "EO:EUM:DAT:SENTINEL-3:OL_1_EFR___"

username = 'mattaqi'
password = 'masma3991'
api_key = generate_api_key(username, password)
download_dir_path = os.getcwd()

hda_dict = init(dataset_id, api_key, download_dir_path)
hda_dict = get_access_token(hda_dict)
hda_dict = acceptTandC(hda_dict)

data = {
    "datasetId": "EO:EUM:DAT:SENTINEL-3:OL_1_EFR___",
    "stringChoiceValues": [
    {
        "name": "platformname",
        "value": "Sentinel-3"
    },
    {
        "name": "producttype",
        "value": "OL_1_EFR___"
    }
    ],
    "dateRangeSelectValues": [
        {
            "name": "position",
            "start": "2020-08-31T10:10:00.000Z",
            "end": "2020-08-31T10:15:00.000Z"
        }
    ],
    "boundingBoxValues": [
        {
            "name": "bbox",
            "bbox": [
                0.88,
                38.08,
                4.15,
                40.05
            ]
        }
    ]
}

hda_dict = get_job_id(hda_dict, data)

hda_dict = get_results_list(hda_dict)

hda_dict = get_order_ids(hda_dict)

hda_dict = download_data(hda_dict, file_extension='.zip')
