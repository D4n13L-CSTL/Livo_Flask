
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
""" 
def conexion_db():
    connection = psycopg2.connect(
            user=os.getenv("user"),
            password=os.getenv("password"),
            host=os.getenv("host"),
            port=os.getenv("port"),
            dbname=os.getenv("dbname"))
    return connection


"""
<<<<<<< HEAD

=======
>>>>>>> 5124b06e02c988f71adf3840f0f1e7bada6c089a
def conexion_db():
    connection = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DBNAME)
    return connection
""" 


#////////////////////////////////////
