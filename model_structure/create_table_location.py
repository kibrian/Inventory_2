from function import createDbconnection

dbconnection=createDbconnection()

mycursor=dbconnection.cursor()
mycursor.execute("CREATE TABLE location(id int(11)AUTO_INCREMENT primary key,location_name varchar(255),merchant_id int(11))")