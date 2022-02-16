import math

CURRENCY_PATH = '../Currencies'


class Convert:

    def __init__(self):
        self.old_length = 0

    def convert(self, coins_data):
        training_data = []
        for coin_data in coins_data:
            coin_data = self.handle_coin(coins_data[coin_data])
            training_data.append(coin_data)
        return training_data

    def handle_coin(self, coin_data):
        line_data = []
        for data in coin_data:
            previous_price = data['price'] + data['difference']
            one_percent = previous_price / 100
            difference = data['difference'] / one_percent
            color = difference * 1275

            if color >= 0:
                color = color + 127.5
            elif color < -1:
                color = (255 + color) / 2

            if color > 255:
                color = 255
            elif color < 0:
                color = 0

            color = math.floor(color)
            line_data.append(color)

        length = len(line_data)
        if self.old_length == 0:
            self.old_length = length
        if length != self.old_length:
            return
        return line_data
