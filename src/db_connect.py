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


# # src/db_connect.py

# import pyodbc
# from config import config

# def get_connection():
#     try:
#         conn_str = (
#             f"DRIVER={{{config['driver']}}};"
#             f"SERVER={config['server']};"
#             f"DATABASE={config['database']};"
#             "Trusted_Connection=yes;"  # Use this for Windows Auth
#         )
#         connection = pyodbc.connect(conn_str)
#         print("✅ Connection successful!")
#         return connection
#     except Exception as e:
#         print("❌ Connection failed:")
#         print(e)
#         return None

