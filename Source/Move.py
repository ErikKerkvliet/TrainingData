import random
import os
import shutil


class Move:

    def __init__(self, glv):
        self.glv = glv

    def move_files(self, labels):
        length = len(self.glv.coins) + 1
        for label in labels:
            files = os.listdir(f'./data/temp/{label}')

            random.shuffle(files)

            moves = 0
            for file in files:
                if moves < 20:
                    shutil.move(f'./data/temp/{label}/{file}', f'./data/images_{length}/{label}/{file}')
                    moves += 1

            self.empty_folder(f'./data/temp/{label}')

    @staticmethod
    def count_files(directory):
        files = os.listdir(directory)

        return len(files) - 2

    @staticmethod
    def empty_folder(folder):
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
