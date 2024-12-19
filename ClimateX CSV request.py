# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:29:11 2024

@author: hakan
"""

import requests

headers = {
    'accept': 'application/json',
    'x-api-key': '6f2UpBvpdk21IN1vo9JAoZuLeUFbcywO'
}

files = {
    'file': open('c:\Hakan\Task_Adresses_Normalized.csv'),
}

response = requests.post('https://apis.climate-x.com/main/external-upload-csv/' , headers=headers, files=files)

print(response)
