#! python3
# textMyself.py - Defines the textmyself() function that texts a message
# passed to a string

# Preset Values
accountSID = 'ACe5f90466d6998346a1db34b4eb57a65d'
authToken = '2d5cb4b9d4f0de0bc072b9f4752fda83'
myNumber = '+19047290677'
twilioNumber = '+16176908370'

from twilio.rest import Client

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)

def textOther (number, message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=number)
