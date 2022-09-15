import Ticker
import Globalvar
from Move import Move


class Main:

    def __init__(self):
        self.glv = Globalvar.Globalvar()
        self.ticker = Ticker.Ticker(self.glv)

    def start(self):
        return self.ticker.ticker()


error = ''
if __name__ == '__main__':
    main = Main()
    try:
        if not main.start():
            error = 'with error '
        Move.empty_folder(f'./data/temp/')
    except KeyboardInterrupt:
        print('Exception: Keyboard interrupt')
    except BaseException as e:
        print(f'Exception: {e}')

print(f'============= Finished {error}=============')
print('Shutting down')

exit()
