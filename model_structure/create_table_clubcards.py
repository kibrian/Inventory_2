from function import createDbconnection

dbconnection=createDbconnection()

mycursor=dbconnection.cursor()
mycursor.execute("CREATE TABLE clubcards(id int(11)AUTO_INCREMENT primary key,card_no int(11),serial_no int(11),phone_no int(11),card_ballance int(11),member_id int(11))")