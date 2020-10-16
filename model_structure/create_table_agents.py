from function import createDbconnection

dbconnection=createDbconnection()

mycursor=dbconnection.cursor()
mycursor.execute("CREATE TABLE agents(id int(11)AUTO_INCREMENT primary key,agent_name varchar(255),location_id int(11))")