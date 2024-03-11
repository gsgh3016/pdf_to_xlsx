import pandas as pd


def read_excel(file_path: str) -> pd.DataFrame:
    print(f"{file_path}의 정보를 읽고 있습니다.")
    excel = pd.read_excel(file_path)
    print(excel)