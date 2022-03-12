from Convert import Convert
from Make import Make
from datetime import datetime
import Append
import Label

import http.client
import json
import time

MODULI = [20, 255, 545, 1085, 2165]

# How many steps to wait before calculating labels
RESULT_TIME = 2

# Grayscale values for actions
ACTIONS = [0, 127, 255]

# Coins to which actions are being added
COINS = ['BTC', 'ETH', 'BCH', 'BNB', 'EGLD', 'MKR', 'AAVE', 'KSM', 'YFI']

# Time to wait in loop for getting data
TIMER = 80

class Ticker:

    def __init__(self):
        self.append = Append.Append()
        self.label = Label.Label()
        self.coins = {}
        self.time = ''
        self.coin_indexes = []
        Make.directories(MODULI)

    # Main function for getting data from cryptocurrency data from bitpanda
    def ticker(self):
        connection = http.client.HTTPSConnection("api.bitpanda.com")
        headers = {'Accept': "application/json"}

        counter = 0
        while True:
            try:
                connection.request("GET", "/v1/ticker", headers=headers)

                response = connection.getresponse()
                data = response.read()
            except http.client.NotConnected:
                print('Exception: disconnected. \n Reconnect')
                connection = http.client.HTTPSConnection("api.bitpanda.com")
                continue

            coins_data = json.loads(data.decode("utf-8"))
            if counter == 0:
                counter += 1
                print(f'Loop: {counter}')
                time.sleep(TIMER)
                for coin in coins_data.keys():
                    self.coins[coin] = [{
                        'price': float(coins_data[coin]['EUR']),
                        'difference': 0
                    }]

                self.set_coin_key_indexes()
                continue

            counter += 1
            print(f'Loop: {counter}')

            for coin in coins_data.keys():
                price = float(coins_data[coin]['EUR'])
                coin_dat = {
                    'price': float(coins_data[coin]['EUR']),
                    'difference': self.coins[coin][-1]['price'] - price,
                }
                self.coins[coin].append(coin_dat)

            self.time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            for modulo in MODULI:
                if counter % modulo == 0:
                    converted = []
                    for coin in coins_data.keys():
                        delimited = list(self.coins[coin][(counter - modulo):counter])
                        converted.append(Convert.handle_coin(delimited))
                        if not converted[-1]:
                            del(converted[-1])

                    self.label.set_coin_data(self.coins)
                    self.append.actions(converted, self.coin_indexes, modulo)
                    exit()

            if counter == 2160:
                counter = 0
                self.coins = {}
            time.sleep(TIMER)

    def set_coin_key_indexes(self):
        for index, coin in enumerate(self.coins.keys()):
            if coin in COINS:
                self.coin_indexes.append(index)
