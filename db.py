import mysql.connector
from mysql.connector import Error
import config

def get_connection():
    try:
        conn = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"MySQL connection error: {e}")
        return None
