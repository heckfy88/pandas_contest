import pandas as pd
from pandas import DataFrame


def get_dataframe(file_path: str) -> DataFrame:
    input_csv = pd.read_csv(file_path)
    return pd.DataFrame(input_csv)


def output_distinct(df: DataFrame):
    names = df["Имя"].values.tolist()
    distinct_names = list(set(names))
    distinct_names.sort()

    f = open("output.txt", "a")
    for name in distinct_names:
        f.write(name + " ")
    f.close()


if __name__ == '__main__':
    df = get_dataframe("/Users/ruslanagaev/PycharmProjects/pandas contest/pythonProject1/input.csv")
    output_distinct(df)
