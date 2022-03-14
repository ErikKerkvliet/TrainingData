from Convert import Convert
from Make import Make
from datetime import datetime
import Append

import http.client
import json
import time

MODULI = [7, 255, 545, 1085, 2165]

# How many steps to wait before calculating labels
RESULT_TIME = 5

# Time to wait in loop for getting data
TIMER = 80

class Ticker:

    def __init__(self, glv):
        self.glv = glv
        self.append = Append.Append(self.glv)
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

                    self.glv.label.set_coin_data(self.get_label_coin_data(counter))
                    self.append.actions(converted, modulo)
                    exit()

            if counter == 2160:
                counter = 0
                self.coins = {}
            time.sleep(TIMER)

    def set_coin_key_indexes(self):
        indexes = []
        for index, coin in enumerate(self.coins.keys()):
            if coin in self.glv.coins:
                indexes.append(index)

        self.glv.set_indexes(indexes)

    def get_label_coin_data(self, length):
        label_coin_data = {}
        from_index = length - RESULT_TIME
        for coin in self.coins.keys():
            label_coin_data[coin] = self.coins[coin][from_index:]

        return label_coin_data
