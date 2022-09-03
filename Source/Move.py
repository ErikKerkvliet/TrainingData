from Make import Make
import random
import os
import shutil

TEMP_DIRS = ['_yes', '_no']


class Move:

    def __init__(self, glv):
        self.g = glv

    def move_files(self):
        yes_files_plus = os.listdir('./Data/Images/_yes_plus')
        yes_files_minus = os.listdir('./Data/Images/_yes_minus')
        yes_files = yes_files_plus if len(yes_files_plus) < len(yes_files_minus) else yes_files_minus
        folder_type = 'plus' if len(yes_files_plus) < len(yes_files_minus) else 'minus'

        no_files = os.listdir('./Data/Images/_no')
        for yes_file in yes_files:
            shutil.move(f'./Data/Images/_yes/{yes_file}', f'./Data/Images/yes/{yes_file}')

        random_numbers = random.sample(range(len(yes_files)), len(yes_files))
        for number in random_numbers:
            shutil.move(f'./Data/Images/_no/{no_files[number]}', f'./Data/Images/no/{no_files[number]}')
            shutil.move(f'./Data/Images/_yes_{folder_type}/{no_files[number]}', f'./Data/Images/no/{no_files[number]}')

        self.empty_folder('./Data/Images/_no')

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
