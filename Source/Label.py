class Label:

    def __init__(self, glv):
        self.coin_data = {}
        self.glv = glv

    def set_coin_data(self, coin_data):
        self.coin_data = coin_data

    def calculate(self, data):
        total = 0.0
        coins1 = []
        coins2 = []
        for index, coin in enumerate(self.coin_data.keys()):
            if index in self.glv.indexes:
                final = self.coin_data[coin]['end'] - self.coin_data[coin]['start']

                if data[index][-1] == 255 and final > 0.05:
                    total += final
                    coins1.append(coin)
                elif data[index][-1] == 0 and final < -0.05:
                    total += final
                    coins2.append(coin)
                elif data[index][-1] != 127:
                    total -= -final if final < 0 else final

        if total > 3:
            return 'yes'
        else:
            return 'no'

