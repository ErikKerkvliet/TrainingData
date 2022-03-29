from Make import Make
from datetime import datetime
from Action import Action


class Append:

    def __init__(self, glv):
        self.glv = glv
        self.coins_data = None
        self.counter = 0
        self.time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    def actions(self, coins_data):
        self.coins_data = coins_data
        self.counter = 0
        self.time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        self.label(self.glv.actions)

    def label(self, actions, depth=1):
        if depth == len(self.glv.coins):
            return

        for action in actions:
            self.coins_data[self.glv.indexes[depth]][-1] = action

            self.counter += 1
            label = self.glv.label.calculate(self.coins_data)
            filename = f"./Data/Images/{label}/{self.time}_{self.counter}"

            Make.image(self.coins_data, filename)

        self.coins_data[self.glv.indexes[depth]][-1] = Action.NONE.value
        self.label(actions, depth+1)
