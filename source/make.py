import numpy as np
from PIL import Image as Img
from datetime import datetime
from json import dumps
from os import path, makedirs


class Make:

    def __init__(self, glv):
        self.glv = glv

    def image(self, training_data, filename=None):
        data = np.array(training_data, dtype=np.uint8)

        img = Img.fromarray(data, 'L')

        if filename is None:
            result_time = self.glv.result_time
            image_width = len(training_data[0])
            date = datetime.now().strftime('%d-%m-%Y')

            filename = f"../data/images_{self.glv.result_time}/temp/{result_time}/{image_width}/{date}.png"
        else:
            filename += '.png'

        img.save(filename)

        # print(f'Saved image to {filename}')

    @staticmethod
    def json(training_data, filename):
        filename += '.json'

        json = dumps(training_data)

        f = open(filename, "w")

        f.write(json)

        print(f'Saved file to {filename}')

    def directories(self, folders):
        for folder in folders:
            if not path.isdir(f'../data/images_{self.glv.result_time}/{folder}'):
                makedirs(f'../data/images_{self.glv.result_time}/{folder}')

            if not path.isdir(f'../data/images_{self.glv.result_time}/temp/{folder}'):
                makedirs(f'../data/images_{self.glv.result_time}/temp/{folder}')
