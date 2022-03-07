from Convert import Convert
from Make import Make
from datetime import datetime
from Append import Append

import http.client
import json
import time

MODULI = [105, 255, 545, 1085, 2165]
RESULT_TIME = 5
ACTIONS = [0, 127, 255]
COINS = ['BTC', 'ETH', 'BCH', 'BNB', 'EGLD', 'MKR', 'AAVE', 'KSM', 'YFI']

class Ticker:

    def __init__(self):
        self.coins = {}
        self.time = ''
        self.timer = 5
        Make.directories(MODULI)

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
                time.sleep(self.timer)
                for coin in coins_data.keys():
                    self.coins[coin] = [{
                        'price': float(coins_data[coin]['EUR']),
                        'difference': 0
                    }]
                continue

            counter += 1
            print(f'Loop: {counter}')

            for coin in coins_data.keys():
                price = float(coins_data[coin]['EUR'])
                coin_dat = {
                    'price': float(coins_data[coin]['EUR']),
                    'difference': self.coins[coin][-1]['price'] - price
                }

                self.coins[coin].append(coin_dat)
            # print(self.coins)
            # exit()
            for modulo in MODULI:
                if counter % modulo == 0:
                    converted = []
                    for coin in coins_data.keys():
                        delimited = list(self.coins[coin][(counter - modulo):counter])
                        converted.append(Convert.handle_coin(delimited))
                        if not converted[-1]:
                            del(converted[-1])
                    self.save_image(converted, modulo)
                    self.save_json(converted, modulo)

            if counter == 2160:
                counter = 0
                self.coins = {}
            time.sleep(self.timer)

    def save_image(self, data, width):
        path = f"./Data/Images/{width}/"
        self.time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        filename = path + self.time

        for coin in data.keys():
            if coin in COINS:
                for action in ACTIONS:
                    data[coin].append(action)

            filename += f'_{coin}'
            data = Append.actions(data)
            Make.image(data[-5], filename)

    def save_json(self, data, width):
        path = f"./Data/Json/{width}/"
        filename = path + self.time
        Make.json(data, filename)
