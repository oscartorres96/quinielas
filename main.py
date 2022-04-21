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
        :return: results: <dict>
        """
        df.rename(columns={'Unnamed: 0': "name",
                           'Unnamed: 1': "game 1",
                           'Unnamed: 2': "game 2",
                           'Unnamed: 3': "game 3",
                           'Unnamed: 4': "game 4",
                           'Unnamed: 5': "game 5",
                           'Unnamed: 6': "game 6",
                           'Unnamed: 7': "game 7",
                           'Unnamed: 8': "game 8",
                           'Unnamed: 9': "game 9"}, inplace=True)
        df.drop([0, 1], axis=0, inplace=True)
        results = df.tail(n=1).to_dict('records')[0]
        # Drop results
        df.drop([df.shape[0] + 1], axis=0, inplace=True)
        return df, results

    def __get_high_score(self, docs_with_points):
        """
        Method that obtains the maximum score value of all competitors
        :param docs_with_points: <dict>
        :return: max(scores): <int>
        """
        scores = []
        for each in docs_with_points:
            scores.append(each['points'])
        return max(scores)

    def __get_winer(self, docs_with_points):
        """
        Method that analyzes the list of users and determines the winners
        :param docs_with_points: <dict>
        :return: winners: <list>
        """
        winners = []
        high_score = self.__get_high_score(docs_with_points)
        for each in docs_with_points:
            if each['points'] == high_score:
                winners.append(each)
        return winners

    def __get_criteria(self, result, game):
        """
        Method that returns a criteria based on the result
        :param result: <dict>
        :param game: <int>
        :return: criteria: <str>
        """
        criteria = None
        results = result[f'{"game"} {game}'].split("-")
        results[0] = int(results[0])
        results[1] = int(results[1])
        if results[0] == results[1]:
            criteria = "E"
        elif results[0] > results[1]:
            criteria = "L"
        elif results[0] < results[1]:
            criteria = "V"
        return criteria

    def __add_points(self, docs, results):
        """
        Method that adds the property points to the dictionary of each user
        based on their score compared to the results of the week
        :param docs: <dict>
        :param results: <dict>
        :return: docs: <dict>
        """
        for each in docs:
            each['points'] = 0
            for game in range(1, 10):
                # print(f'{each["name"]}":" {"game"} {game}', f'"Results: "{"game"} {game}')
                if each[f'{"game"} {game}'] == results[f'{"game"} {game}']:
                    each['points'] += 3
                else:
                    user_criteria = self.__get_criteria(each, game)
                    result_criteria = self.__get_criteria(results, game)
                    if user_criteria == result_criteria:
                        each['points'] += 1
        return docs

    def main(self):
        quinielas_path = f'{self.__quinielas_path}'
        files = os.listdir(quinielas_path)
        for file in files:
            filepath = f'{quinielas_path}/{file}'
            df = pd.read_excel(filepath, skiprows=3)
            new_df, results = self.__dataframe_transformer(df)
            docs = new_df.to_dict('records')
            docs_with_points = self.__add_points(docs, results)
            for each in docs_with_points:
                print(f'{each["name"]} {"made"} {each["points"]} "points."')
            winners = self.__get_winer(docs_with_points)
            for winner in winners:
                print(f'--{"The winner is"} {winner["name"]} {"with"} {winner["points"]} points.--')


if __name__ == '__main__':
    client = Quiniela()
    client.main()
