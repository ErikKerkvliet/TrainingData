from Action import Action


class Label:

    def __init__(self, glv):
        self.coin_data = {}
        self.glv = glv

    def set_coin_data(self, coin_data):
        self.coin_data = coin_data

    def calculate(self, data):
        for index, coin in enumerate(self.coin_data.keys()):
            if index in self.glv.indexes:
                final = float(self.coin_data[coin]['end']) / float(self.coin_data[coin]['start'])
                if data[index][-1] == Action.BUY.value and final > 1.03:
                    print(f'    {final} - {coin} - yes_plus')
                    return 'yes_plus'
                if data[index][-1] == Action.SELL.value and final < 0.97:
                    print(f'    {final} - {coin} - yes_minus')
                    return 'yes_minus'
        return 'no'
