'''
    python -m pip install mysql-connector

'''
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    port="3306",
)

'''
    connect to database

'''

mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE clubs_inventory_2")
