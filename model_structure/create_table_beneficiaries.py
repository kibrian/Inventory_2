from function import createDbconnection

dbconnection=createDbconnection()

mycursor=dbconnection.cursor()
mycursor.execute("CREATE TABLE beneficiaries(id int(11)AUTO_INCREMENT primary key,name varchar(255),age int(11),id_no int(11),phone_no int(11),member_id int(11))")