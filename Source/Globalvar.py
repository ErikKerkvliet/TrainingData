import Label

class Globalvar:

    def __init__(self):
        # Coins to which actions are being added
        self.coins = ['BTC', 'ETH', 'BCH', 'BNB', 'EGLD', 'MKR', 'AAVE', 'KSM', 'YFI']

        # Grayscale values for actions
        self.actions = [0, 127, 255]

        self.indexes = []
        self.label = Label.Label(self)

    def set_indexes(self, indexes):
        self.indexes = indexes
