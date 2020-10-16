from function import createDbconnection

dbconnection=createDbconnection()

mycursor=dbconnection.cursor()
mycursor.execute("CREATE TABLE members(id int(11)AUTO_INCREMENT primary key,member_name varchar(255),address varchar(255),id_no int(11),phone_no int(11),merchant_id int(11),membership_id int(11))")