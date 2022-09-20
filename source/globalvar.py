from label import Label
from action import Action


class Globalvar:

    def __init__(self):
        # Coins to which actions are being added
        self.coins = self.currencies()

        # Grayscale values for actions        
        self.actions = [Action.SELL.value, Action.BUY.value]

        self.indexes = []
        self.label = Label(self)
        self.result_time = 0
        self.extra_data = {}
        self.prices = []

    def set_result_time(self, result_time) -> None:
        self.result_time = result_time

    def get_result_time(self) -> int:
        return self.result_time

    def set_extra_data(self, extra_data):
        self.extra_data = extra_data

    def get_price(self, nr) -> float:
        return self.prices[nr]

    def add_price(self, price):
        self.prices.append(price)

    def set_indexes(self, indexes):
        self.indexes = indexes

    @staticmethod
    def currencies() -> list:
        # self.coins = ['BTC', 'ETH', 'BCH', 'BNB', 'EGLD', 'MKR', 'AAVE', 'KSM', 'YFI', 'XDB']
        return [
            'XAU',     # 0
            'XAG',     # 1
            'USDC',    # 2
            'PAN',     # 3
            'BTC',     # 4
            'ETH',     # 5
            'USDT',    # 6
            'BNB',     # 7
            'XRP',     # 8
            'ADA',     # 9
            'SOL',     # 10
            'AVAX',    # 11
            'DOT',     # 12
            'DOGE',    # 13
            'XPD',     # 14
            'SHIB',    # 15
            'MATIC',   # 16
            'LTC',     # 17
            'NEAR',    # 18
            'ATOM',    # 19
            'XPT',     # 20
            'LINK',    # 21
            'UNI',     # 22
            'BCH',     # 23
            'FTT',     # 24
            'TRX',     # 25
            'ETC',     # 26
            'ALGO',    # 27
            'XLM',     # 28
            'MANA',    # 29
            'HBAR',    # 30
            'AXS',     # 31
            'ICP',     # 32
            'EGLD',    # 33
            'SAND',    # 34
            'VET',     # 35
            'APE',     # 36
            'FIL',     # 37
            'WAVES',   # 38
            'FTM',     # 39
            'THETA',   # 40
            'KLAY',    # 41
            'XTZ',     # 42
            'ZEC',     # 43
            'EOS',     # 44
            'FLOW',    # 45
            'AAVE',    # 46
            'MIOTA',   # 47
            'GRT',     # 48
            'CAKE',    # 49
            'MKR',     # 50
            'BTT',     # 51
            'ONE',     # 52
            'STX',     # 53
            'GALA',    # 54
            'NEO',     # 55
            'ENJ',     # 56
            'LRC',     # 57
            'DASH',    # 58
            'KSM',     # 59
            'CELO',    # 60
            'BAT',     # 61
            'CHZ',     # 62
            'CRV',     # 63
            'MINA',    # 64
            'AR',      # 65
            'XEM',     # 66
            'XYM',     # 67
            'COMP',    # 68
            'QTUM',    # 69
            'YFI',     # 70
            'OMG',     # 71
            'RVN',     # 72
            '1INCH',   # 73
            'RNDR',    # 74
            'ANKR',    # 75
            'SNX',     # 76
            'KNC',     # 77
            'UMA',     # 78
            'IMX',     # 79
            'ZRX',     # 80
            'IOST',    # 81
            'ONT',     # 82
            'XDB',     # 83
            'SUSHI',   # 84
            'STORJ',   # 85
            'SRM',     # 86
            'REN',     # 87
            'FLUX',    # 88
            'DGB',     # 89
            'OCEAN',   # 90
            'DYDX',    # 91
            'LSK',     # 92
            'BEST',    # 93
            'COTI',    # 94
            'ALICE',   # 95
            'RSR',     # 96
            'ANT',     # 97
            'OXT',     # 98
            'BICO',    # 99
            'REP',     # 100
            'BAND',    # 101
            'DUSK',    # 102
            'KMD',     # 103
            'BCI5',    # 104
            'BCI10',   # 105
            'BCI25',   # 106
            'LUNA',    # 107
        ]
