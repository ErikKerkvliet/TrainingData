from move import Move
from make import Make
from append import Append
from convert import Convert

import http.client
import json
import time

# Time to wait in loop for getting data
TIMER = 80

LABELS = ['yes_plus', 'yes_minus', 'no']
MODULI = [10]
IMAGE_WIDTH = 224  # Image width. 224 X 224
WIDTH = 223  # Image width without action columns. 223 X 223
RESULT_TIME = 20  # After how many iterations to look back to calculate the labels


class Ticker:

    def __init__(self, glv):
        self.glv = glv
        self.append = Append(self.glv)
        self.convert = Convert(self.glv)
        self.move = Move(self.glv)
        self.make = Make(self.glv)
        self.coins = {}
        self.coin_indexes = []
        self.glv.set_result_time(RESULT_TIME)
        self.make.directories(LABELS)

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
            except http.client.HTTPException:
                print('Exception: HTTP Exception. \n Reconnect')
                connection = http.client.HTTPSConnection("api.bitpanda.com")
                continue

            response = json.loads(data.decode("utf-8"))
            coins_data = self.convert.coin_order(response)
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
                data = {
                    'price': float(coins_data[coin]['EUR']),
                    'difference': self.coins[coin][-1]['price'] - price,
                }
                self.coins[coin].append(data)

            for modulo in MODULI:
                if counter >= WIDTH and counter % modulo == 0:
                    converted = []
                    for coin in coins_data.keys():
                        delimited = list(self.coins[coin][(counter - WIDTH):counter])
                        converted.append(self.convert.handle_coin(delimited))
                        if not converted[-1]:
                            self.glv.set_price(self.coins[coin][-1]['price'])
                            del(converted[-1])

                    extra_data = {
                        'image_width': IMAGE_WIDTH,
                        'timer': TIMER,
                        'result_time': RESULT_TIME,
                    }

                    converted = self.append.add_extra_data(converted, extra_data)

                    self.glv.label.set_coin_data(self.get_label_coin_data(counter))

                    print('<<<<<<<<<<<< Generate images >>>>>>>>>>>>')
                    self.append.actions(converted)
                    self.move.move_files(LABELS)

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
            label_coin_data[coin] = {
                'start': self.coins[coin][from_index]['price'],
                'end': self.coins[coin][-1]['price'],
            }

        return label_coin_data
