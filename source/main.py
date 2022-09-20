from ticker import Ticker
from globalvar import Globalvar

import sys


class Main:

    def __init__(self, result_time=20):
        self.glv = Globalvar()
        self.glv.set_result_time(result_time)
        self.ticker = Ticker(self.glv)

    def start(self):
        return self.ticker.ticker()


error = ''
if __name__ == '__main__':

    if len(sys.argv) == 2:
        main = Main(int(sys.argv[1]))
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
