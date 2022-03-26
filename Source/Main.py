import Ticker
import Globalvar


class Main:

    def __init__(self):
        self.glv = Globalvar.Globalvar()
        self.ticker = Ticker.Ticker(self.glv)

    def start(self):
        self.ticker.ticker()


main = Main()
main.start()

print('Finished')
print('Shutting down')

exit()
