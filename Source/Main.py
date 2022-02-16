import Convert
import RequestData
import Image


class Main:

    def __init__(self):
        self.convert = Convert.Convert()
        self.request = RequestData.RequestData()
        self.image = Image.Image()

    def start(self):
        while True:
            response = self.request.ticker()
            training_data = self.convert.convert(response)
            self.image.make(training_data)
            self.request.reset()


main = Main()
main.start()

print('Finished')
print('Shutting down')

exit()

