# 📄 Project Documentation: SQL Item Quantity Analysis

## 🧩 Project Overview

This Python-based project connects to a Microsoft SQL Server database to analyze customer purchase data. The main goal is to extract the total quantity of each item purchased by customers aged 18 to 35, and export the results to a CSV file. The script supports both a SQL-based and a Pandas-based solution.

## 🎯 Objectives

1. **Connect to a SQL Server database** using Windows Authentication.
2. **Extract total quantities of each item per customer (aged 18–35)**:
   - Sum of each item bought per customer.
   - Exclude any item with total quantity = 0.
   - Ensure the quantity has no decimal points (whole items only).
3. **Implement dual solutions**:
   - One using a SQL query.
   - One using Pandas after data extraction.
4. **Store the results in a CSV file**:
   - Use semicolon (`;`) as the delimiter.

## 🗂️ Project Structure

```
sql_item_quantity_project/
│
├── src/
│   ├── config.py                 # Database connection configuration
│   ├── db_connection.py          # SQL Server connection logic
│   ├── analysis_query.sql           # SQL-based solution
│   ├── run_panads_analysis.py        # Pandas-based solution
│
│
├── sql/
│   ├── create_tables.sql        # SQL script to create necessary tables
│   └── insert_data.sql       # Final SQL query for objective
│
├── tests/
│   └── test_cases.sql           # Test data for verification
│
├── output/
│   └── customer_item_quantities.csv         # Output file
│
└── README.md                    # Project summary and instructions
```


## 🛠️ Technologies Used

- **Python 3.x**
- **Microsoft SQL Server (LocalDB)**
- **ODBC Driver 19 for SQL Server**
- **pandas**
- **pyodbc**

## 🚀 Run Instructions

1. Ensure SQL Server is running and test tables are created (`sql/create_tables.sql`).
2. Configure your `config.py` with the correct server and database details.
3. Run `analysis_query.sql` to generate the output using SQL logic.
4. Run `run_panads_analysis.py` to generate the same output using Pandas.
5. Check the CSV output in `src/customer_item_quantities.csv`.