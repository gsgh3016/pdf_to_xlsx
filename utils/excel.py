import pandas as pd


COL_NAMES = []
    
def read_excel(file_path: str) -> pd.DataFrame:
    print(f"{file_path}의 정보를 읽고 있습니다.")
    excel = pd.read_excel(file_path)
    for col_name in excel.columns:
        COL_NAMES.append(col_name)
    print(COL_NAMES)
    return excel

def make_excel_content(pdf_df: pd.DataFrame, excel_df: pd.DataFrame) -> pd.DataFrame:
    no = len(excel_df) + 1
    for index, row in pdf_df.iterrows():
        data = {
            'NO': no,
            '전공명': '정보컴퓨터공학(부산대-학사-부전공)' if row['교과구분'] == '부전공' else '전자공학(부산대-학사-주전공)',
            '수강연도': row['학년도'],
            '학기': row['학기'][0] if row['학기'].endswith('학기') else row['학기'] + '계절',
            '과목명': row['교과목명'],
            '과목유형': '교양기타' if '교양' in row['교과구분'] else '전공',
            '취득학점': int(round(float(row['학점']))),
            '성적': row['성적등급'],
            '재수강여부': 'Y' if len(pdf_df.loc[pdf_df['교과목명'] == row['교과목명']]) > 1 else 'N'
        }
        # 데이터 프레임 생성 시, 리스트 안에 사전을 넣어서 바로 여러 열을 가진 DataFrame 생성
        new_row_df = pd.DataFrame([data])

        excel_df = pd.concat([excel_df, new_row_df], ignore_index=True)
        no += 1

    return excel_df

