from Make import Make
from datetime import datetime
from Action import Action


class Append:

    def __init__(self, glv):
        self.glv = glv
        self.coins_data = None
        self.time = ''

    def actions(self, coins_data):
        self.coins_data = coins_data
        self.time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        self.label(self.glv.actions)

    def label(self, actions, depth=1):
        if depth == len(self.glv.coins):
            return

        for action in actions:
            self.coins_data[self.glv.indexes[depth]][-1] = action

            label = self.glv.label.calculate(self.coins_data)

            filename = f"./data/temp/{label}/{self.time}_{self.glv.coins[self.glv.indexes[depth]]}"

            Make.image(self.coins_data, filename)

        self.coins_data[self.glv.indexes[depth]][-1] = Action.NONE.value
        self.label(actions, depth+1)

    def add_extra_data(self, coin_data, width, timer, result_time):
        time = "%s-%s" % (datetime.today().weekday(), datetime.now().strftime('%d-%m-%y-%H-%M-%S'))
        extra_data = time.split('-')
        extra_data.append(timer)
        extra_data.append(result_time)

        for i in range(9, width):
            extra_data.append('0')

        coin_data.append(list(map(int, extra_data)))

        coin_data = self.add_filler(coin_data, width)

        return coin_data

    @staticmethod
    def add_filler(coin_data, width):
        filler_height = width - len(coin_data)

        filler = []
        for i in range(width):
            filler.append(0)

        for i in range(filler_height):
            coin_data.append(filler)
        return coin_data
