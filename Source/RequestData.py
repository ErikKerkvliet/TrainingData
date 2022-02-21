import http.client
import json
import time


class RequestData:

    def __init__(self):
        self.coins = {}

    def ticker(self):
        connection = http.client.HTTPSConnection("api.bitpanda.com")
        headers = {'Accept': "application/json"}

        times = 0
        error = False
        while times < 1080:
            try:
                if times % 30 == 0 and times != 0:
                    connection.close()
                    connection = http.client.HTTPSConnection("api.bitpanda.com")
                    headers = {'Accept': "application/json"}
                connection.request("GET", "/v1/ticker", headers=headers)
                response = connection.getresponse()
                data = response.read()

                coins_data = json.loads(data.decode("utf-8"))
                if times == 0:
                    for coin in coins_data.keys():
                        if times == 0:
                            self.coins[coin] = [{
                                'price': float(coins_data[coin]['EUR']),
                                'difference': 0
                            }]
                    times += 1
                    print(f'Loop: {times}')
                    time.sleep(80)
                    continue

                for coin in coins_data.keys():
                    price = float(coins_data[coin]['EUR'])
                    self.coins[coin].append({
                        'price': price,
                        'difference': self.coins[coin][-1]['price'] - price
                    })
                times += 1
                print(f'Loop: {times}')
                time.sleep(80)
            except http.client.NotConnected:
                print('Exception: disconnected')
                connection = http.client.HTTPSConnection("api.bitpanda.com")
            except KeyboardInterrupt:
                print('Keyboard interrupt')
                return self.coins
            except BaseException as e:
                if error:
                    print(e)
                    exit()
                error = True
                print(e)

        return self.coins

    def reset(self):
        self.coins = {}
