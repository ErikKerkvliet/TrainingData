import Convert
import RequestData
import Make


class Main:

    def __init__(self):
        self.convert = Convert.Convert()
        self.request = RequestData.RequestData()
        self.make = Make.Make()

    def start(self):
        while True:
            response = self.request.ticker()
            training_data = self.convert.convert(response)

            self.make.switch_count()
            self.make.image(training_data)
            self.make.json(training_data)

            self.request.reset()


main = Main()
main.start()

print('Finished')
print('Shutting down')

exit()
