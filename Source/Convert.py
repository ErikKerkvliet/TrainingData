import math
from Action import Action


class Convert:

    def __init__(self, glv):
        self.old_length = 0
        self.glv = glv

    def image(self, coins_data):
        training_data = []
        for coin_data in coins_data:
            coin_data = self.handle_coin(coins_data[coin_data])
            training_data.append(coin_data)
        return training_data

    @staticmethod
    def handle_coin(coin_data):
        line_data = []
        old_length = 0
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
                color = Action.BUY.value
            elif color < 0:
                color = Action.SELL.value

            color = math.floor(color)
            line_data.append(color)

        # Add action value
        line_data.append(Action.NONE.value)

        length = len(line_data)
        if old_length == 0:
            old_length = length
        if length != old_length:
            return False
        return line_data

    @staticmethod
    def json(coins_data):
        line_data = {}
        for coin_data in coins_data:
            line_data[coin_data] = []

            for data in coins_data[coin_data]:
                line_data[coin_data].append(data['price'])

        return line_data

    def coin_order(self, coins_data):
        coins = {}
        for coin in self.glv.coins:
            if coin in self.glv.coins:
                coins[coin] = coins_data[coin]
            else:
                coins[coin] = {'EUR': 1.0}

        return coins
