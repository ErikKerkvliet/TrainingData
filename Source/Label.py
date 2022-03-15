class Label:

    def __init__(self, glv):
        self.coin_data = {}
        self.glv = glv

    def set_coin_data(self, coin_data):
        self.coin_data = coin_data

    def calculate(self, data):
        score = 0
        total = 0.0
        coins1 = []
        coins2 = []
        for index, coin in enumerate(self.coin_data.keys()):
            if index in self.glv.indexes:
                final = self.coin_data[coin]['end'] - self.coin_data[coin]['start']

                if data[index][-1] == 255 and final > 0.05:
                    score += 1
                    total += final
                    coins1.append(coin)
                elif data[index][-1] == 0 and final < -0.05:
                    score += 1
                    total += final
                    coins2.append(coin)
                elif data[index][-1] != 127:
                    score -= 1
                    total -= final

        print(score, total, coins1, coins2)
        if total > 5:
            return 'yes'
        else:
            return 'no'

