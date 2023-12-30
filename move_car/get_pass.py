#Importing Client API
from onepasswordconnectsdk.client import (
    Client,
    new_client_from_environment,
    new_client
)
import os
from dotenv import load_dotenv

def mysql_login():
    load_dotenv()
    TOKEN_1_PASSWORD = os.getenv('TOKEN_1_PASSWORD')
    ITEM_ID_MYSQL = os.getenv('ITEM_ID_MYSQL')
    VAULT_ID_CITY = os.getenv('VAULT_ID_CITY')

    #Inserting your 1Password Token and 1Password Connect Server Host
    OP_CONNECT_TOKEN = TOKEN_1_PASSWORD #Inserting Credential
    OP_CONNECT_HOST = "http://docker.for.mac.host.internal:8085" #Inserting your connection server port

    Client = new_client(OP_CONNECT_HOST,OP_CONNECT_TOKEN) # Generating instances
    #Now we are going to get list of items in our vault
    credentials = Client.get_item(ITEM_ID_MYSQL,VAULT_ID_CITY)
    username = credentials.fields[0].value
    password = credentials.fields[1].value
    return username, password




