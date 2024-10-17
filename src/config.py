import os
from dotenv import load_dotenv

load_dotenv()

class Config:
  MYSQL_CONFIG = {
    "host" : "localhost",
    "user" : "root",
    "password" : os.getenv("DB_PASSWORD"),
    "database" : "db_reto"
  }

  ENDPOINTS = {
    "ruc" : "https://apiperu.dev/api/ruc"
  }

  API_TOKEN = os.getenv("APPIPERU_TOKEN")

config = Config()