import csv
from prefect import task
from config import config
import requests
from .utils import handle_invalid_ruc


@task(name="Extraer data de csv")
def task_extract_csv(filename):
  data = []
  with open(filename, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
      tmp_data = (row["ruc"], row["razon_social"])
      data.append(tmp_data)
  
  return data

@task(name="Extraer data de ruc (api)")
def task_extract_ruc(ruc):
  token = config.API_TOKEN
  headers = {
    "Authorization" : "Bearer " + token,
    "Content-Type"  : "application/json"
  }

  data = {
    "ruc" : ruc
  }
  url_dni = config.ENDPOINTS["ruc"]
  response = requests.post(url_dni, json=data, headers=headers)

  if response.status_code == 200:
    if response.json()["success"]:
      data = response.json()["data"]
      razon_social = data["nombre_o_razon_social"]
      direccion = data["direccion_completa"] 
      return (razon_social, direccion)
    else:
      handle_invalid_ruc(ruc)
      
  else:
    print("error: ", response.status_code)