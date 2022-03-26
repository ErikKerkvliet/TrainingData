import numpy as np
from PIL import Image as Img
from datetime import datetime
from json import dumps
from os import path, makedirs


class Make:

    def __init__(self):
        self.count = 0

    @staticmethod
    def image(training_data, filename=None):
        data = np.array(training_data, dtype=np.uint8)

        img = Img.fromarray(data, 'L')

        if filename is None:
            filename = f"./Data/Images/{datetime.now().strftime('%d-%m-%Y')}.png"
        else:
            filename += '.png'

        img.save(filename)

        print(f'Saved image to {filename}')

    @staticmethod
    def json(training_data, filename):
        filename += '.json'

        json = dumps(training_data)

        f = open(filename, "w")

        f.write(json)

        print(f'Saved file to {filename}')

    @staticmethod
    def directories(folders):
        if not path.isdir('./Data'):
            makedirs('./Data')

        if not path.isdir('./Data/Images'):
            makedirs('./Data/Images')

        if not path.isdir('./Data/Json'):
            makedirs('./Data/Json')

        for folder in folders:
            if not path.isdir(f'./Data/Images/{folder}'):
                makedirs(f'./Data/Images/{folder}')

            if not path.isdir(f'./Data/Json/{folder}'):
                makedirs(f'./Data/Json/{folder}')
