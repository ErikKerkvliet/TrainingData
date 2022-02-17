import numpy as np
from PIL import Image as Img
from datetime import datetime
from json import dumps
from os import path, makedirs


class Make:

    def __init__(self):
        self.count = 0
        self.directories()

    def image(self, training_data):
        data = np.array(training_data, dtype=np.uint8)

        img = Img.fromarray(data, 'L')

        filename = f"./Data/Images/{datetime.now().strftime('%d-%m-%Y')}_{self.count}.png"

        img.save(filename)

        print(f'Saved image to {filename}')

    def json(self, training_data):
        json = dumps(training_data)

        filename = f"./Data/Json/{datetime.now().strftime('%d-%m-%Y')}_{self.count}"

        f = open(filename, "w")

        f.write(json)

        print(f'Saved file to {filename}')

    def switch_count(self):
        self.count = 2 if self.count == 1 else 1

    @staticmethod
    def directories():
        if not path.isdir('./Data'):
            makedirs('./Data')

        if not path.isdir('./Data/Images'):
            makedirs('./Data/Images')

        if not path.isdir('./Data/Json'):
            makedirs('./Data/Json')
