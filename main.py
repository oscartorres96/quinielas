import pandas as pd
import locale
import pathlib
from pathlib import Path
import os


class Quiniela:
    def __init__(self):
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        self.__quinielas_path = str(Path(f'{str(pathlib.Path(__file__).parent.absolute())}/sheets'))

    def __dataframe_transformer(self, df):
        """
        Method that receives a data frame and processes it in order to facilitate data analysis
        :param df: <pandas Dataframe>
        :return: df: <pandas Dataframe>
        """
        # df.rename(columns={'Unnamed: 0': df.iloc[1][0], 'Unnamed: 1': f'{df.iloc[0][1]} vs {df.iloc[1][1]}',
        #                    'Unnamed: 2': f'{df.iloc[0][2]} vs {df.iloc[1][2]}',
        #                    'Unnamed: 3': f'{df.iloc[0][3]} vs {df.iloc[1][3]}',
        #                    'Unnamed: 4': f'{df.iloc[0][4]} vs {df.iloc[1][4]}',
        #                    'Unnamed: 5': f'{df.iloc[0][5]} vs {df.iloc[1][5]}',
        #                    'Unnamed: 6': f'{df.iloc[0][6]} vs {df.iloc[1][6]}',
        #                    'Unnamed: 7': f'{df.iloc[0][7]} vs {df.iloc[1][7]}',
        #                    'Unnamed: 8': f'{df.iloc[0][8]} vs {df.iloc[1][8]}',
        #                    'Unnamed: 9': f'{df.iloc[0][9]} vs {df.iloc[1][9]}'}, inplace=True)
        df.rename(columns={'Unnamed: 0': "name", 'Unnamed: 1': "game 1",
                           'Unnamed: 2': "game 2",
                           'Unnamed: 3': "game 3",
                           'Unnamed: 4': "game 4",
                           'Unnamed: 5': "game 5",
                           'Unnamed: 6': "game 6",
                           'Unnamed: 7': "game 7",
                           'Unnamed: 8': "game 8",
                           'Unnamed: 9': "game 10"}, inplace=True)
        df.drop([0, 1], axis=0, inplace=True)
        results = df.tail(n=1)
        return df, results

    def main(self):
        quinielas_path = f'{self.__quinielas_path}'
        files = os.listdir(quinielas_path)
        for file in files:
            filepath = f'{quinielas_path}/{file}'
            df = pd.read_excel(filepath, skiprows=3)
            new_df, results = self.__dataframe_transformer(df)
            docs = new_df.to_dict('records')
            print()


if __name__ == '__main__':
    client = Quiniela()
    client.main()
