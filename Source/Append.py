from Make import Make
from datetime import datetime

class Append:

    def __init__(self, glv):
        self.glv = glv
        self.coins_data = None
        self.counter = 0
        self.modulo = 0
        self.time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    def actions(self, coins_data, modulo):
        self.coins_data = coins_data
        self.modulo = modulo
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
            filename = f"./Data/Images/{self.modulo}/{self.time}_{self.counter}_{label}"

            Make.image(self.coins_data, filename)

            self.label(actions, depth+1)

    def actions2(self, coins_data, modulo):
        time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        counter = 0
        for action0 in self.glv.actions:
            coins_data[self.glv.indexes[0]][-1] = action0

            for action1 in self.glv.actions:
                coins_data[self.glv.indexes[1]][-1] = action1

                for action2 in self.glv.actions:
                    coins_data[self.glv.indexes[2]][-1] = action2

                    for action3 in self.glv.actions:
                        coins_data[self.glv.indexes[3]][-1] = action3

                        for action4 in self.glv.actions:
                            coins_data[self.glv.indexes[4]][-1] = action4

                            for action5 in self.glv.actions:
                                coins_data[self.glv.indexes[5]][-1] = action5

                                for action6 in self.glv.actions:
                                    coins_data[self.glv.indexes[6]][-1] = action6

                                    for action7 in self.glv.actions:
                                        coins_data[self.glv.indexes[7]][-1] = action7

                                        for action8 in self.glv.actions:
                                            coins_data[self.glv.indexes[8]][-1] = action8

                                            label = self.glv.label.calculate(coins_data)
                                            filename = f"./Data/Images/{modulo}/{time}_{counter}_{label}"

                                            # Make.image(coins_data, filename)

                                            counter += 1
