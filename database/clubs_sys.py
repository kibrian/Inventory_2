from merchants import Merchant
from club_functions import insertMerchantsToDb
from members import Member
from club_functions import insertMembersToDb
from clubcards import Clubcard
from club_functions import insertClubcardsToDb
#from membership import Membership
#from club_functions import insertMembershipToDb
from transactions import Transaction
from club_functions import insertTransactionsToDb
from location import Location
from club_functions import insertLocationToDb
from agents import Agent
from club_functions import insertAgentsToDb





noof_merchants=int(input("Enter number of merchants: "))

Merchants=[]
for x in range(1,noof_merchants+1):
    merchant_name=input("Enter merchant name: ")
    address=input("Enter address: ")
    phone_no=int(input("Enter phone_no: "))

    merchants=Merchant(merchant_name,address,phone_no)
    merchantsline=insertMerchantsToDb(merchants)
    merchants.line=merchantsline

    
noof_members=int(input("Enter noof_members: "))

Members=[]
for x in range(1,noof_members+1):
    member_name=input("Enter member_name: ")
    address=input("Enter address: ")
    id_no=int(input("Enter id_no: "))
    phone_no=int(input("Enter phone_no: "))
    merchant_id=int(input("Enter merchant_id: "))
    membership_id=int(input("Enter membership_id: "))

    members= Member(member_name,address,id_no,phone_no,merchant_id,membership_id)
    membersline=insertMembersToDb(members)
    members.line=membersline

    #member_type=input("Enter member_type: ")
    #membership=Membership(member_type)
    #membershipline=insertMembershipToDb(membership)
    #membership.line=membershipline


    card_no=int(input("Enter card_no: "))
    serial_no=int(input("Enter serial_no: "))
    phone_no=int(input("Enter phone_no: "))
    card_balance=int(input("Enter card_balance: "))
    member_id=int(input("Enter member_id: "))


    clubcards=Clubcard(card_no,serial_no,phone_no,card_balance,member_id)
    clubcardsline=insertClubcardsToDb(clubcards)
    clubcards.line=clubcardsline


#noof_beneficiaries=int(input("Enter noof_beneficiaries: \n"))

#Beneficiaries=[]
#for x in range(1,noof_beneficiaries+1):

noof_transactions=int(input("Enter noof_transactions: "))

Transactions=[]
for x in range(1,noof_transactions+1):
    amount=int(input("Enter amount: \n"))
    balance=int(input("Enter balance: \n"))
    member_id=input("Enter member_id: \n")
    clubcards_id=input("Enter clubcards_id: \n")
    agent_id=input("Enter agent_id: ")

    transactions=Transaction(amount,balance,member_id,clubcards_id,agent_id)
    transactionsline=insertTransactionsToDb(transactions)
    transactions.line=transactionsline

    
    location_name=input("Enter location_name: \n")
    merchant_id=int(input("Enter merchant_id: \n"))

    location=Location(location_name,merchant_id)
    locationline=insertLocationToDb(location)
    location.line=locationline
    

    agent_name=input("Enter agent_name: \n")
    location_id=int(input("Enter location_id: \n"))


    agents=Agent(agent_name,location_id)
    agentsline=insertAgentsToDb(agents)
    agents.line=agentsline







    

