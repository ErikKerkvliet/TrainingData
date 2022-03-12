import Convert
import RequestData
import Make
import Ticker


class Main:

    def __init__(self):
        self.convert = Convert.Convert()
        self.request = RequestData.RequestData()
        self.make = Make.Make()
        self.ticker = Ticker.Ticker()
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

        # count = 0
        # for action1 in range(3):
        #     coinA = action1
        #     for action2 in range(3):
        #         coinB = action2
        #         for action3 in range(3):
        #             coinC = action3
        #             for action4 in range(3):
        #                 coinD = action4
        #                 for action5 in range(3):
        #                     coinE = action5
        #                     for action6 in range(3):
        #                         coinF = action6
        #                         for action7 in range(3):
        #                             coinG = action7
        #                             for action8 in range(3):
        #                                 coinH = action8
        #                                 for action9 in range(3):
        #                                     coinI = action9
        #                                     for action in range(3):
        #                                         coinJ = action
        #                                         count += 1













        self.ticker.ticker()


main = Main()
main.start()

print('Finished')
print('Shutting down')

exit()
