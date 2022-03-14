class Label:

    def __init__(self, glv):
        self.coin_data = []
        self.glv = glv

    def set_coin_data(self, coin_data):
        self.coin_data = coin_data

    def calculate(self, data):
        base_total = 0
        final_total = 0
        for index, action in enumerate(self.coin_data):
            if index in self.glv.indexes:
                base_total += self.coin_data[action][0]['price']
                final_total += self.coin_data[action][-1]['price']
                    # exit()
                # if data[-1] == 255:
        print(final_total - base_total)
        # exit()
