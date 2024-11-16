import pandas as pd
from pandas import DataFrame


def get_dataframe(file_path: str) -> DataFrame:
    input_csv = pd.read_csv(file_path)
    return pd.DataFrame(input_csv)


def output_by_filter(df: DataFrame):
    names = df.loc[df['Возраст'] > 35]
    print(" ".join(names['Имя'].to_list()))


if __name__ == '__main__':
    df = get_dataframe("/Users/ruslanagaev/PycharmProjects/pandas contest/pythonProject1/input.csv")
    output_by_filter(df)
