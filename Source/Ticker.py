from Convert import Convert
from Make import Make

import http.client
import json
import time
from datetime import datetime


class Ticker:

    def __init__(self):
        self.coins = {}
        self.time = ''
        self.timer = 80
        self.moduli = [100, 250, 540, 1080, 2160]
        Make.directories(self.moduli)

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

            for modulo in self.moduli:
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
                converted = []
            time.sleep(self.timer)

    def save_image(self, data, width):
        path = f"./Data/Images/{width}/"
        self.time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        filename = path + self.time
        Make.image(data, filename)

    def save_json(self, data, width):
        path = f"./Data/Json/{width}/"
        filename = path + self.time
        Make.json(data, filename)
