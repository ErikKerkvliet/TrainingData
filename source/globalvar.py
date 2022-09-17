from label import Label
from action import Action


class Globalvar:

    def __init__(self):
        # Coins to which actions are being added
        self.coins = [
            'XAU', 'XAG', 'USDC', 'PAN', 'BTC', 'ETH', 'USDT', 'BNB', 'XRP', 'ADA', 'SOL', 'AVAX',
            'DOT', 'DOGE', 'XPD', 'SHIB', 'MATIC', 'LTC', 'NEAR', 'ATOM', 'XPT', 'LINK', 'UNI', 'BCH',
            'FTT', 'TRX', 'ETC', 'ALGO', 'XLM', 'MANA', 'HBAR', 'AXS', 'ICP', 'EGLD', 'SAND', 'VET',
            'APE', 'FIL', 'WAVES', 'FTM', 'THETA', 'KLAY', 'XTZ', 'ZEC', 'EOS', 'FLOW', 'AAVE', 'MIOTA',
            'GRT', 'CAKE', 'MKR', 'BTT', 'ONE', 'STX', 'GALA', 'NEO', 'ENJ', 'LRC', 'DASH', 'KSM',
            'CELO', 'BAT', 'CHZ', 'CRV', 'MINA', 'AR', 'XEM', 'XYM', 'COMP', 'QTUM', 'YFI', 'OMG', 'RVN',
            '1INCH', 'RNDR', 'ANKR', 'SNX', 'KNC', 'UMA', 'IMX', 'ZRX', 'IOST', 'ONT', 'XDB', 'SUSHI',
            'STORJ', 'SRM', 'REN', 'FLUX', 'DGB', 'OCEAN', 'DYDX', 'LSK', 'BEST', 'COTI', 'ALICE',
            'RSR', 'ANT', 'OXT', 'BICO', 'REP', 'BAND', 'DUSK', 'KMD', 'BCI5', 'BCI10', 'BCI25', 'LUNA'
        ]

        # self.coins = ['BTC', 'ETH', 'BCH', 'BNB', 'EGLD', 'MKR', 'AAVE', 'KSM', 'YFI', 'XDB']

        # Grayscale values for actions        
        self.actions = [Action.SELL.value, Action.BUY.value]

        self.indexes = []
        self.label = Label(self)
        self.result_time = 0

    def set_result_time(self, time):
        self.result_time = time

    def set_indexes(self, indexes):
        self.indexes = indexes
