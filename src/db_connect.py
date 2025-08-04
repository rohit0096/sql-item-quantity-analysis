import pyodbc
from config import config

def get_connection():
    conn_str = (
        f"DRIVER={{{config['driver']}}};"
        f"SERVER={config['server']};"
        f"DATABASE={config['database']};"
        "Trusted_Connection=yes;"
    )
    return pyodbc.connect(conn_str)


