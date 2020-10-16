from function import createDbconnection

dbconnection=createDbconnection()

mycursur=dbconnection.cursor()

mycursur.execute("CREATE TABLE transactions(id int(11)AUTO_INCREMENT primary key,amount int(11),balance int(11),member_id int(11),clubcards_id int(11),agent_id int(11))")