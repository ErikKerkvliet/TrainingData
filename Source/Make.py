import numpy as np
from PIL import Image as Img
from datetime import datetime
from json import dumps
from os import path, makedirs


class Make:

    def __init__(self, glv):
        self.count = 0
        self.glv = glv

    @staticmethod
    def image(training_data, filename=None):
        data = np.array(training_data, dtype=np.uint8)

        img = Img.fromarray(data, 'L')

        if filename is None:
            filename = f"./data/temp/{len(training_data[0])}/{datetime.now().strftime('%d-%m-%Y')}.png"
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

    def directories(self, folders, width):
        for folder in folders:
            if not path.isdir(f'./data/images_{width}/{folder}'):
                makedirs(f'./data/images_{width}/{folder}')

            if not path.isdir(f'./data/temp/{folder}'):
                makedirs(f'./data/temp/{folder}')
