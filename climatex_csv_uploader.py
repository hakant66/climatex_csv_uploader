
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



import os
import requests

# Securely load API key from environment variable
API_KEY = '6f2UpBvpdk21IN1vo9JAoZuLeUFbcywO'

if not API_KEY:
    raise ValueError("Missing API key! Please set the 'CLIMATE_X_API_KEY' environment variable.")

headers = {
    'accept': 'application/json',
    'x-api-key': API_KEY
}

file_path = 'C:\\apps\\Climate X Data\\Task_Adresses_Normalized.csv'

try:
    with open(file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post('https://apis.climate-x.com/main/external-upload-csv/', headers=headers, files=files)

    # Handle response
    if response.ok:
        print("✅ Upload successful!")
        print("Response:", response.json())
    else:
        print(f"❌ Upload failed with status code {response.status_code}")
        print("Details:", response.text)

except FileNotFoundError:
    print(f"❌ File not found: {file_path}")
except requests.exceptions.RequestException as e:
    print("❌ Request failed:", str(e))
