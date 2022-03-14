import Convert
import RequestData
import Make
import Ticker
import Globalvar


class Main:

    def __init__(self):
        self.glv = Globalvar.Globalvar()
        self.ticker = Ticker.Ticker(self.glv)
        self.convert = Convert.Convert()
        self.request = RequestData.RequestData()
        self.make = Make.Make()
        self.count = 0

    def start(self):
        # while True:
        # response = self.request.ticker()
        # image_data = self.convert.image(response)
        # json_data = self.convert.json(response)
        #
        # self.make.switch_count()
        # self.make.image(image_data, 'img.png')
        # self.make.json(json_data)
        #
        # self.request.reset()

        self.ticker.ticker()


main = Main()
main.start()

print('Finished')
print('Shutting down')

exit()
