import numpy as np
from PIL import Image as Img
from datetime import datetime


class Image:

    def __init__(self):
        self.count = 0

    def make(self, training_data):
        data = np.array(training_data, dtype=np.uint8)

        img = Img.fromarray(data, 'L')

        self.count = 2 if self.count == 1 else 1
        filename = f"../Currencies/Coins_{datetime.now().strftime('%d-%m-%Y')}_{self.count}.png"

        img.save(filename)
        img.show()
