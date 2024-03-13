PDF_FILE_DIR = "pdf/"
EXCEL_FILE_DIR = "excel/"


from utils import *


if __name__ == "__main__":
    check_dir(PDF_FILE_DIR)
    pdf_files = scan_files(PDF_FILE_DIR, "pdf")
    pdf_contents = pd.DataFrame()
    for pdf in pdf_files:
        pdf_contents = pd.concat(
            [pdf_contents, read_pdf(pdf)],
            ignore_index=True
        )
            
    excel_files = scan_files(EXCEL_FILE_DIR, "xlsx")
    excel_contents = pd.DataFrame()
    for excel in excel_files:
        excel_contents = pd.concat(
            [excel_contents, read_excel(excel)], 
            ignore_index=True
        )
        
    excel_final_contents = make_excel_content(pdf_contents, excel_contents)
    print(excel_final_contents.columns)
    for _, row in excel_final_contents.iterrows():
        row_str = ''
        for v in row.values:
            row_str += str(v) + '\t'
        print(row_str)
        
    excel_final_contents.to_excel(os.path.join(EXCEL_FILE_DIR, '성적데이터.xlsx'), index=False)