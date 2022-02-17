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
            image_data = self.convert.image(response)
            json_data = self.convert.json(response)

            self.make.switch_count()
            self.make.image(image_data)
            self.make.json(json_data)

            self.request.reset()


main = Main()
main.start()

print('Finished')
print('Shutting down')

exit()
