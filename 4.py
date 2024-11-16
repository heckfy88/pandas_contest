import pandas as pd
from pandas import DataFrame


def get_dataframe(file_path: str) -> DataFrame:
    input_csv = pd.read_csv(file_path)
    return pd.DataFrame(input_csv)


def output_null_count_by_column(df: DataFrame):
    null_values_count = df.isna().sum()

    # на Яндекс.Контесте баг с выводом
    # f = open("output.txt", "a")
    # f.write("Название_колонки,Количество_NaN\n")
    # for i in range(len(null_values_count)):
    #    f.write(f"{df.columns[i]},{str(null_values_count.iloc[i])}\n")
    # f.close()
    print("Название_колонки,Количество_NaN")
    for i in range(len(null_values_count)):
        print(f"{df.columns[i]},{str(null_values_count.iloc[i])}")


if __name__ == '__main__':
    df = get_dataframe("input.csv")
    output_null_count_by_column(df)
