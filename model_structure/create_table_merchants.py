from function import createDbconnection

dbconnection=createDbconnection()

mycursor=dbconnection.cursor()

mycursor.execute("CREATE TABLE merchants(id int(11)AUTO_INCREMENT primary key,merchant_name varchar(255),address varchar(255),phone_no int(11))")