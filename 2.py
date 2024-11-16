import pandas as pd
from pandas import DataFrame


def get_dataframe(file_path: str) -> DataFrame:
    input_csv = pd.read_csv(file_path)
    return pd.DataFrame(input_csv)


def get_duplicates(df: DataFrame) -> list:
    result = (df.groupby('Имя')
              .size()
              .reset_index(name='Count')
              .sort_values(by='Count', ascending=False)
              )

    max_count = result['Count'].max()
    max_duplicates = result[result['Count'] == max_count]

    f = open("output.txt", "a")

    for name, count in max_duplicates.iterrows():
        f.write(f"{count['Имя']} {count['Count']}" "\n")
    f.close()


if __name__ == '__main__':
    df = get_dataframe("/Users/ruslanagaev/PycharmProjects/pandas contest/pythonProject1/input.csv")
    get_duplicates(df)
