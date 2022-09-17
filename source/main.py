from ticker import Ticker
from globalvar import Globalvar


class Main:

    def __init__(self):
        self.glv = Globalvar()
        self.ticker = Ticker(self.glv)

    def start(self):
        return self.ticker.ticker()


error = ''
if __name__ == '__main__':
    main = Main()
    try:
        main.start()
    except KeyboardInterrupt:
        print('Exception: Keyboard interrupt')
        error = 'with error '


print(f'============= Finished {error}=============')
print('Shutting down')

exit()
