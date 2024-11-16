import pandas as pd
from pandas import DataFrame


def get_dataframe(file_path: str) -> DataFrame:
    input_csv = pd.read_csv(file_path)
    return pd.DataFrame(input_csv)


def prepare_shape(df: DataFrame) -> list:
    shape = df.shape
    list_shape = list(shape)
    list_shape[0] = shape[0] + 1
    return list_shape


def output_shape(shape: list):
    f = open("output.txt", "a")
    for i in shape:
        f.write(str(i) + "\n")
    f.close()


if __name__ == '__main__':
    df = get_dataframe("/Users/ruslanagaev/PycharmProjects/pandas contest/pythonProject1/input.csv")
    shape = prepare_shape(df)
    output_shape(shape)
