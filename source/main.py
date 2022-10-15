from ticker import Ticker
from globalvar import Globalvar

import sys


class Main:

    def __init__(self, result_time=20, currencies=1):
        self.glv = Globalvar()
        self.glv.set_currencies(currencies)
        self.glv.set_result_time(result_time)
        self.ticker = Ticker(self.glv)

    def start(self):
        return self.ticker.ticker()


error = ''
if __name__ == '__main__':

    if len(sys.argv) == 2:
        main = Main(int(sys.argv[1]))
    elif len(sys.argv) == 3:
        main = Main(int(sys.argv[1]), int(sys.argv[2]))
    else:
        main = Main()
    try:
        main.start()
    except KeyboardInterrupt:
        print('Exception: Keyboard interrupt')
        error = 'with error '


print(f'============= Finished {error}=============')
print('Shutting down')

exit()
