import pandas as pd
import locale
import pathlib
from pathlib import Path
import os


class Quiniela:
    def __init__(self):
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        self.__quinielas_path = str(Path(f'{str(pathlib.Path(__file__).parent.absolute())}/sheets'))

    def main(self):
        quinielas_path = f'{self.__quinielas_path}'
        files = os.listdir(quinielas_path)
        for file in files:
            filepath = f'{quinielas_path}/{file}'
            df = pd.read_excel(filepath)
            print()


if __name__ == '__main__':
    client = Quiniela()
    client.main()
