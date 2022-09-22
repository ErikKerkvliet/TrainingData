from move import Move
from make import Make
from append import Append
from convert import Convert
from globalvar import DEFAULT_CURRENCY

import http.client
import json
import time

TIMER = 80  # Time to wait in loop for getting data
LABELS = ['yes_plus', 'yes_minus', 'no']
IMAGE_WIDTH = 224  # Image width. 224 X 224
WIDTH = 223  # Image width without action columns. 223 X 223


class Ticker:

    def __init__(self, glv):
        self.glv = glv
        self.append = Append(self.glv)
        self.convert = Convert(self.glv)
        self.move = Move(self.glv)
        self.make = Make(self.glv)
        self.coins = {}
        self.coin_indexes = []
        self.result_time = self.glv.get_result_time()
        self.make.directories(LABELS)

        self.glv.set_extra_data({
            'image_width': IMAGE_WIDTH,
            'timer': TIMER,
            'result_time': self.result_time,
        })

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
                        'price': float(coins_data[coin][DEFAULT_CURRENCY]),
                        'difference': 0
                    }]

                self.set_coin_key_indexes()
                continue

            counter += 1
            print(f'Loop: {counter}')

            for coin in coins_data.keys():
                price = float(coins_data[coin][DEFAULT_CURRENCY])
                data = {
                    'price': float(coins_data[coin][DEFAULT_CURRENCY]),
                    'difference': self.coins[coin][-1]['price'] - price,
                }
                self.coins[coin].append(data)

            if counter >= WIDTH and counter % self.result_time == 0:
                converted = []
                for coin_key in coins_data.keys():
                    delimited = list(self.coins[coin_key][(counter - WIDTH):counter])
                    converted.append(self.convert.handle_coin(delimited))
                    self.glv.add_price(self.coins[coin_key][-1]['price'])
                    if not converted[-1]:
                        del(converted[-1])

                converted = self.append.add_filler(converted, IMAGE_WIDTH)

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
        from_index = length - self.result_time
        for coin in self.coins.keys():
            label_coin_data[coin] = {
                'start': self.coins[coin][from_index]['price'],
                'end': self.coins[coin][-1]['price'],
            }

        return label_coin_data
