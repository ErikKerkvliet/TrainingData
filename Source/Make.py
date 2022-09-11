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
            filename = f"./Data/temp/{len(training_data[0])}/{datetime.now().strftime('%d-%m-%Y')}.png"
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
        if not path.isdir('./Data'):
            makedirs('./Data')

        width = len(self.glv.coins) + 1
        if not path.isdir(f'./Data/Images_{width}'):
            makedirs(f'./Data/Images_{width}')

        for folder in folders:
            if not path.isdir(f'./Data/Images_{width}/{folder}'):
                makedirs(f'./Data/Images_{width}/{folder}')

            if not path.isdir(f'./Data/temp/{folder}'):
                makedirs(f'./Data/temp/{folder}')
