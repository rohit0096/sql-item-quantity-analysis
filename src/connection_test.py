# src/run_sql_solution.py

from db_connect import get_connection

conn = get_connection()
if conn:
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sys.tables")
    tables = cursor.fetchall()
    print("Tables in the database:")
    for table in tables:
        print("-", table[0])
    conn.close()
