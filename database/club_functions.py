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

def insertMerchantsToDb(merchants):
    mydbconnection=createDbconnection()
    sql="INSERT INTO merchants(merchant_name,address,phone_no)VALUES(%s,%s,%s)"
    val=(merchants.merchant_name,merchants.address,merchants.phone_no)
    mycursor=mydbconnection.cursor()
    mycursor.execute(sql,val)
    mydbconnection.commit()
    print(mycursor.rowcount,"Record inserted")

    sqlselect="select * from merchants WHERE phone_no='%s'"
    val=(merchants.phone_no)
    mycursor.execute(sqlselect,val)
    insertedmerchants=mycursor.fetchone()
    print(insertedmerchants)

    if insertedmerchants is not None:
        for merchant in insertedmerchants:
            print(merchant)
    

    return insertedmerchants 


def insertMembersToDb(members):
    mydbconnection=createDbconnection()
    sql="INSERT INTO members(member_name,address,id_no,phone_no,merchant_id,membership_id)VALUES(%s,%s,%s,%s,%s,%s)"
    val=(members.member_name,members.address,members.id_no,members.phone_no,members.merchant_id,members.membership_id)
    mycursor=mydbconnection.cursor()
    mycursor.execute(sql,val)
    mydbconnection.commit()
    print(mycursor.rowcount,"Record inserted")

    sqlselect="select * from members WHERE merchant_id='%s'"
    val=(members.merchant_id)
    mycursor.execute(sqlselect,val)
    insertedmembers=mycursor.fetchone()
    print(insertedmembers)


    if insertedmembers is not None:
        for member in insertedmembers:
            print(member)
    

    return insertedmembers

def insertClubcardsToDb(clubcards):
    mydbconnection=createDbconnection()
    sql="INSERT INTO clubcards(card_no,serial_no,phone_no,card_balance,member_id)VALUES(%s,%s,%s,%s,%s)"
    val=(clubcards.card_no,clubcards.serial_no,clubcards.phone_no,clubcards.card_balance,clubcards.member_id)
    mycursor=mydbconnection.cursor()
    mycursor.execute(sql,val)
    mydbconnection.commit()
    print(mycursor.rowcount,"Record inserted")

    sqlselect="select * from clubcards WHERE card_no='%s'"
    val=(clubcards.card_no)
    mycursor.execute(sqlselect,val)
    insertedclubcards=mycursor.fetchone()
    print(insertedclubcards)

    if insertedclubcards is not None:
        for clubcard in insertedclubcards:
            print(clubcard)


    return insertedclubcards


#def insertMembershipToDb(membership):
    #mydbconnection=createDbconnection()
    #sql="INSERT INTO membership(member_type)VALUE(%s)"
    #val=(membership.member_type)
    #mycursor=mydbconnection.cursor()
    #mycursor.execute(sql,val)
    #mydbconnection.commit()
    #print(mycursor.rowcount,"Record inserted")

    #sqlselect="select * FROM membership WHERE member_type='%s'"
    #val=(membership.member_type)
    #mycursor.execute(sqlselect,val)
    #insertedmembership=mycursor.fetchone()
    #print(insertedmembership)

    #if insertedmembership is not None:
        #for membership in insertedmembership:
            #print(membership)

    
    #return insertedmembership

def insertTransactionsToDb(transactions):
    mydbconnection=createDbconnection()
    sql="INSERT INTO transactions(amount,balance,member_id,clubcards_id,agent_id)VALUE(%s,%s,%s,%s,%s)"
    val=(transactions.amount,transactions.balance,transactions.member_id,transactions.clubcards_id,transactions.agent_id)
    mycursor=mydbconnection.cursor()
    mycursor.execute(sql,val)
    mydbconnection.commit()
    print(mycursor.rowcount,"Record inserted")

    sqlselect="select *from transactions WHERE balance='%s'"
    val=(transactions.balance)
    mycursor.execute(sqlselect,val)
    insertedtransactions=mycursor.fetchone()
    print(insertedtransactions)

    if insertedtransactions is not None:
        for transaction in insertedtransactions:
            print(transaction)

    return insertedtransactions

def insertLocationToDb(location):
    mydbconnection=createDbconnection()
    sql="INSERT INTO location(location_name,merchant_id),VALUES(%s,%s)"
    val=(location.location_name,location.merchant_id)
    mycursor=mydbconnection.cursor()
    mycursor.execute(sql)
    mydbconnection.commit()
    print(mycursor.rowcount,"Record inserted")
    
    sqlselect="select *from location WHERE merchant_id='%s'"
    val=(location.merchant_id)
    mycursor.execute(sqlselect,val)
    insertedlocation=mycursor.fetchone()
    print(insertedlocation)

    if insertedlocation is not None:
        for location in insertedlocation:
            print(location)

    return  insertedlocation

def insertAgentsToDb(agents):
    mydbconnection=createDbconnection()
    sql="INSERT INTO agents(agent_name,location_id),VALUES(%s,%s)"
    val=(agents.agent_name,agents.location_id)
    mycursor=mydbconnection.cursor()
    mycursor.execute(sql,val)
    mydbconnection.commit()
    print(mycursor.rowcount,"Record inserted")


    sqlselect="select * from agents WHERE location_id='%s'"
    val=(agents.location_id)
    mycursor.execute(sqlselect,val)
    insertedagents=mycursor.fetchone()
    print(insertedagents)

    if insertedagents is not None:
        for agent in insertedagents:
            print(agent)

    return insertedagents