from ast import parse
import pandas as pd
import pyodbc
import configparser

parser = configparser.ConfigParser()
with open('C:\Aduanasoft\ServiceManager_CTI\myodbfm3.ini', mode='r') as file:
    parser.read_file(file)
# print(parser.sections())


cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            f"Server={parser['FM3ODB']['MSSQLServer']};"
            f"Database={parser['FM3ODB']['MSSQLDatabaseName']};"
            f"UID={parser['FM3ODB']['MSSQLUserName']};"
            f"PWD={parser['FM3ODB']['MSSQLPassword']};")
cnxn = pyodbc.connect(cnxn_str)

data = pd.read_sql_query("SELECT TOP(100) * FROM factfactura", cnxn)

for i in data.index:
    print( f"{data.columns[0]}={data['CONSECUTIVO'][i]}, {data.columns[1]}={data['FACTURA'][i]}")