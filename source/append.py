from make import Make
from datetime import datetime
from action import Action


class Append:

    def __init__(self, glv):
        self.glv = glv
        self.make = Make(glv)
        self.coins_data = None
        self.time = ''

    def actions(self, coins_data):
        self.coins_data = coins_data
        self.time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        self.label(self.glv.actions)

    def label(self, actions, depth=1):
        if depth == len(self.glv.coins):
            return

        coin_index = depth - 1
        self.coins_data.append(self.get_extra_data(coin_index))

        for action in actions:
            self.coins_data[self.glv.indexes[coin_index]][-1] = action

            label = self.glv.label.calculate(self.coins_data)
            coin = self.glv.coins[self.glv.indexes[coin_index]]
            filename = f"../data/images_{self.glv.result_time}/temp/{label}/{self.time}_{coin}"

            self.make.image(self.coins_data, filename)

        self.coins_data[self.glv.indexes[coin_index]][-1] = Action.NONE.value
        del(self.coins_data[-1])
        self.label(actions, depth+1)

    def get_extra_data(self, coin_index):
        time = "%s-%s" % (datetime.today().weekday(), datetime.now().strftime('%d-%m-%y-%H-%M-%S'))
        extra_data = time.split('-')
        extra_data.append(self.glv.extra_data['timer'])
        extra_data.append(self.glv.extra_data['result_time'])
        extra_data.append('255')

        price_string = str(self.glv.get_price(coin_index))
        for char in price_string:
            if char == '.':
                char = '255'
            if char == 'e':
                char = '254'
            if char == '-':
                char = '253'
            extra_data.append(char)

        for i in range(len(extra_data), self.glv.extra_data['image_width']):
            extra_data.append(Action.NONE.value)
        return list(map(int, extra_data))

    @staticmethod
    def add_filler(coin_data, width):
        filler_height = (width - 1) - len(coin_data)

        filler = []
        for i in range(width):
            filler.append(0)

        for i in range(filler_height):
            coin_data.append(filler)
        return coin_data
