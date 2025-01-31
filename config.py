from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='.env')

DB_PORT = os.getenv("DB_PROD_PORT")  
DB_HOST = os.getenv("DB_PROD_HOST")
DB_NAME = os.getenv("DB_PROD_NAME")
DB_USER = os.getenv("DB_PROD_USER")
DB_PASS = os.getenv("DB_PROD_PASS")