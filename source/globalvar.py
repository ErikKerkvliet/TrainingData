from label import Label
from action import Action

DEFAULT_CURRENCY = 'EUR'

# Grayscale values for actions
ACTIONS = [Action.SELL.value, Action.BUY.value]


class Globalvar:

    def __init__(self):
        # Coins to which actions are being added
        self.coins = []
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

    def set_currencies(self, currency_function):
        if currency_function == 1:
            self.coins = self.currencies()
        else:
            self.coins = self.currencies_2()

    @staticmethod
    def currencies() -> list:
        # self.coins = ['BTC', 'ETH', 'BCH', 'BNB', 'EGLD', 'MKR', 'AAVE', 'KSM', 'YFI', 'XDB']
        return [
            'XAU',      # 0
            'BTC',      # 1
            'ETH',      # 2
            'USDT',     # 3
            'USDC',     # 4
            'XAG',      # 5
            'BNB',      # 6
            'XRP',      # 7
            'ADA',      # 8
            'XPD',      # 9
            'SOL',      # 10
            'DOGE',     # 11
            'DOT',      # 12
            'XPT',      # 13
            'MATIC',    # 14
            'SHIB',     # 15
            'TRX',      # 16
            'AVAX',     # 17
            'UNI',      # 18
            'LINK',     # 19
            'LTC',      # 20
            'ETC',      # 21
            'ATOM',     # 22
            'FTT',      # 23
            'XLM',      # 24
            'NEAR',     # 25
            'ALGO',     # 26
            'BCH',      # 27
            'FLOW',     # 28
            'LUNC',     # 29
            'FIL',      # 30
            'APE',      # 31
            'QNT',      # 32
            'ICP',      # 33
            'VET',      # 34
            'ETHW',     # 35
            'HBAR',     # 36
            'MANA',     # 37
            'XTZ',      # 38
            'CHZ',      # 39
            'SAND',     # 40
            'EOS',      # 41
            'EGLD',     # 42
            'THETA',    # 43
            'XVS',      # 44
            'AAVE',     # 45
            'AXS',      # 46
            'OKB',      # 47
            'ZEC',      # 48
            'MIOTA',    # 49
            'BTT',      # 50
            'MKR',      # 51
            'CAKE',     # 52
            'HT',       # 53
            'GRT',      # 54
            'HNT',      # 55
            'NEO',      # 56
            'KLAY',     # 57
            'FTM',      # 58
            'SNX',      # 59
            'RUNE',     # 60
            'CRV',      # 61
            'GT',       # 62
            'ENJ',      # 63
            'DASH',     # 64
            'BAT',      # 65
            'COMP',     # 66
            'STX',      # 67
            'KAVA',     # 68
            'WAVES',    # 69
            'RVN',      # 70
            'MINA',     # 71
            'LRC',      # 72
            'GMT',      # 73
            'TWT',      # 74
            'CELO',     # 75
            'XEM',      # 76
            'DCR',      # 77
            'KSM',      # 78
            'ZIL',      # 79
            'RSR',      # 80
            '1INCH',    # 81
            'BNX',      # 82
            'ENS',      # 83
            'LUNA',     # 84
            'GNO',      # 85
            'AR',       # 86
            'ANKR',     # 87
            'YFI',      # 88
            'GALA',     # 89
            'QTUM',     # 90
            'KDA',      # 91
            'IOTX',     # 92
            'GLM',      # 93
            'ONE',      # 94
            'OMG',      # 95
            'POLY',     # 96
            'ZRX',      # 97
            'FLUX',     # 98
            'ICX',      # 99
            'LPT',      # 100
            'JST',      # 101
            'IOST',     # 102
            'WEMIX',    # 103
            'OP',       # 104
            'KNC',      # 105
            'SRM',      # 106
            'XYM',      # 107
            'ONT',      # 108
            'STORJ',    # 109
            'WAXP',     # 110
            'SC',       # 111
            'MXC',      # 112
            'GLMR',     # 113
            'ZEN',      # 114
            'CSPR',     # 115
            'IMX',      # 116
            'SXP',      # 117
            'AUDIO',    # 118
            'UMA',      # 119
            'WOO',      # 120
            'SCRT',     # 121
            'PLA',      # 122
            'DGB',      # 123
            'SKL',      # 124
            'SUSHI',    # 125
            'ASTR',     # 126
            'CVC',      # 127
            'CKB',      # 128
            'PUNDIX',   # 129
            'LSK',      # 130
            'BEST',     # 131
            'COTI',     # 132
            'RNDR',     # 133
            'REN',      # 134
            'ORBS',     # 135
            'SYS',      # 136
            'CELR',     # 137
            'REQ',      # 138
            'XNO',      # 139
            'SNT',      # 140
            'OCEAN',    # 141
            'LOOKS',    # 142
            'POWR',     # 143
            'CTSI',     # 144
            'BNT',      # 145
            'DYDX',     # 146
            'BICO',     # 147
            'SANTOS',   # 148
            'RAY',      # 149
            'C98',      # 150
            'REP',      # 151
            'EUROC',    # 152
            'CTK',      # 153
            'STRAX',    # 154
            'STMX',     # 155
            'MTL',      # 156
            'JOE',      # 157
            'RAD',      # 158
            'STPT',     # 159
            'OXT',      # 160
            'LOOM',     # 161
            'FXS',      # 162
            'ANT',      # 163
            'VTHO',     # 164
            'NKN',      # 165
            'FET',      # 166
            'ACH',      # 167
            'EFI',      # 168
            'ALICE',    # 169
            'SUPER',    # 170
            'AERGO',    # 171
            'UTK',      # 172
            'PERP',     # 173
            'MBL',      # 174
            'DUSK',     # 175
            'TT',       # 176
            'BAKE',     # 177
            'SUN',      # 178
            'PORTO',    # 179
            'BAND',     # 180
            'TOMO',     # 181
            'ARPA',     # 182
            'YGG',      # 183
            'MLN',      # 184
            'SFP',      # 185
            'AVA',      # 186
            'ILV',      # 187
            'WAN',      # 188
            'KMD',      # 189
            'TROY',     # 190
            'LINA',     # 191
            'AKT',      # 192
            'TRU',      # 193
            'TVK',      # 194
            'BLZ',      # 195
            'PSG',      # 196
            'IRIS',     # 197
            'FARM',     # 198
            'GTC',      # 199
            'CHESS',    # 200
            'BAR',      # 201
            'PAN',      # 202
            'CITY',     # 203
            'AGLD',     # 204
            'HIGH',     # 205
            'QUICK',    # 206
            'VOXEL',    # 207
            'DODO',     # 208
            'ATM',      # 209
            'JUV',      # 210
            'XDB',      # 211
            'XRT',      # 212
            'BCI5',     # 213
            'BCI10',    # 214
            'BCI25',    # 215
            'BCISL',    # 216
            'BCIIL',    # 217
            'BCIDL',    # 218
            'BCIML',    # 219
        ]

    @staticmethod
    def currencies_2() -> list:
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
