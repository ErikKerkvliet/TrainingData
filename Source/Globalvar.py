import Label
from Action import Action
from datetime import datetime


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
        24
        # self.coins = ['BTC', 'ETH', 'BCH', 'BNB', 'EGLD', 'MKR', 'AAVE', 'KSM', 'YFI', 'XDB']

        # Grayscale values for actions        
        self.actions = [Action.SELL.value, Action.BUY.value]

        self.indexes = []
        self.label = Label.Label(self)

    def set_indexes(self, indexes):
        self.indexes = indexes

    @staticmethod
    def get_extra_data(width, timer, result_time):
        time = "%s-%s" % (datetime.today().weekday(), datetime.now().strftime('%d-%m-%y-%H-%M-%S'))
        extra_data = time.split('-')
        extra_data.append(timer)
        extra_data.append(result_time)

        for i in range(8, width):
            extra_data.append('255')

        return list(map(int, extra_data))
