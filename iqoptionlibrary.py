from iqoptionapi.stable_api import IQ_Option
import time
from configparser import ConfigParser
import sys

connection = None

file = "config.ini"
config = ConfigParser()
config.read(file)

def connect():
    global connection

    connectfactor = IQ_Option(config['appstate']['email'], config['appstate']['password'])

    check, reason = connectfactor.connect()

    if check:
        print("connected")
        connection = connectfactor
    else:
        print("Invalid credentials.... Try again")
        sys.exit()

def getbalance():
    print("retrieving balance")
    print(connection.get_balance())

def resetbalance():
    connection.reset_practice_balance()

def liveorpaper():
    connection.change_balance(str(config['appstate']['mode']))

    print(f"account mode is : {str(config['appstate']['mode'])}")

def getassets():
    print("printing all assets on the account")
    print(connection.get_all_open_time())

def buy():
    price = int(config['appstate']['quantity'])
    ticker = str(config['appstate']['ticker'].replace("/", ""))
    action = "call"
    exmode = int(config['appstate']['exmode'])

    check,id = connection.buy(price,ticker,action,exmode)

    if check:
        print(f"Option bought: Quantity: {price}, ticker: {ticker}, action: {action}, expiration: {exmode}")
        return True
    else:
        return False

def sell():
    price = int(config['appstate']['quantity'])
    ticker = str(config['appstate']['ticker'].replace("/", ""))
    action = "put"
    exmode = int(config['appstate']['exmode'])

    check,id = connection.buy(price,ticker,action,exmode)

    if check:
        print(f"Option sold: Quantity: {price}, ticker: {ticker}, action: {action}, expiration: {exmode}")
        return True
    else:
        return False
