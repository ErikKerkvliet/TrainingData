from Make import Make
from datetime import datetime

class Append:

    def __init__(self, glv):
        self.glv = glv

    def actions(self, coins_data, modulo):
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

                                            Make.image(coins_data, filename)

                                            counter += 1
