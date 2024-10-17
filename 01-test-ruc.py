import os
import requests
from dotenv import load_dotenv

load_dotenv()


token = os.getenv("APPIPERU_TOKEN")

url_ruc = "https://apiperu.dev/api/ruc"

ruc = {
  "ruc" : "20509783625"
}

headers = {
  
  "Authorization" : "Bearer " + token,
  "Content-Type" : "application/json"
}

response = requests.post(url_ruc, json=ruc, headers=headers)

if response.status_code == 200:
  print(response.json())
else:
  print("error: ", response.status_code)