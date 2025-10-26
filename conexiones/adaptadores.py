
import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

USER = os.getenv("user_supabase")
PASSWORD = os.getenv("password_supabase")
HOST = os.getenv("host_supabase")
PORT = os.getenv("port_supabase")
DBNAME = os.getenv("dbname_supabase")

def conexion_db():
    connection = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DBNAME)
    return connection



#////////////////////////////////////
