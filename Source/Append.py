from Make import Make
from Label import Label
from datetime import datetime

ACTIONS = [0, 127, 255]
COINS = ['BTC', 'ETH', 'BCH', 'BNB', 'EGLD', 'MKR', 'AAVE', 'KSM', 'YFI']


class Append:

    def __init__(self):
        pass

    def actions(self, coins_data, indexes, modulo):
        time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        counter = 0
        for action0 in ACTIONS:
            coins_data[indexes[0]][-1] = action0

            for action1 in ACTIONS:
                coins_data[indexes[1]][-1] = action1

                for action2 in ACTIONS:
                    coins_data[indexes[2]][-1] = action2

                    for action3 in ACTIONS:
                        coins_data[indexes[3]][-1] = action3

                        for action4 in ACTIONS:
                            coins_data[indexes[4]][-1] = action4

                            for action5 in ACTIONS:
                                coins_data[indexes[5]][-1] = action5

                                for action6 in ACTIONS:
                                    coins_data[indexes[6]][-1] = action6

                                    for action7 in ACTIONS:
                                        coins_data[indexes[7]][-1] = action7

                                        for action8 in ACTIONS:
                                            coins_data[indexes[8]][-1] = action8

                                            label = Label.calculate(coins_data)
                                            filename = f"./Data/Images/{modulo}/_{time}_{counter}_{label}"

                                            Make.image(coins_data, filename)

                                            counter += 1
