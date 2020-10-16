import mysql.connector

def createDbconnection():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        port="3306",
            database="clubs_inventory_2"
    )
    return mydb