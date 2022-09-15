import Move
import Make
import Append

import http.client
import json
import time
import Convert

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
        self.append = Append.Append(self.glv)
        self.convert = Convert.Convert(self.glv)
        self.move = Move.Move(self.glv)
        self.make = Make.Make(self.glv)
        self.coins = {}
        self.coin_indexes = []
        self.make.directories(LABELS, RESULT_TIME)

    # Main function for getting data from cryptocurrency data from bitpanda
    def ticker(self):
        connection = http.client.HTTPSConnection("api.bitpanda.com")
        headers = {'Accept': "application/json"}

        counter = 0
        error = False
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
            except Exception as e:
                if error:
                    return False

                error = True
                print(f'Exception: {e}')
                continue

            error = False
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
                coin_dat = {
                    'price': float(coins_data[coin]['EUR']),
                    'difference': self.coins[coin][-1]['price'] - price,
                }
                self.coins[coin].append(coin_dat)

            for modulo in MODULI:
                if counter >= WIDTH and counter % modulo == 0:
                    converted = []
                    for coin in coins_data.keys():
                        delimited = list(self.coins[coin][(counter - WIDTH):counter])
                        converted.append(self.convert.handle_coin(delimited))
                        if not converted[-1]:
                            del(converted[-1])

                    converted = self.append.add_extra_data(converted, IMAGE_WIDTH, TIMER, RESULT_TIME)

                    self.glv.label.set_coin_data(self.get_label_coin_data(counter))

                    print('<<<<<<<<<<<< Generate images >>>>>>>>>>>>')
                    self.append.actions(converted)
                    self.move.move_files(LABELS, RESULT_TIME)

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
