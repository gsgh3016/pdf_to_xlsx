PDF_FILE_DIR = "pdf/"
EXCEL_FILE_DIR = "excel/"


from utils import *
import pdfplumber


if __name__ == "__main__":
    check_dir(PDF_FILE_DIR)
    pdf_files = scan_files(PDF_FILE_DIR, "pdf")
    for pdf in pdf_files:
        with pdfplumber.open(pdf) as p:
            for page in p.pages:
                table = page.extract_table()
                df = pd.DataFrame(table[1:], columns=table[0])
                print(df)
            
    excel_files = scan_files(EXCEL_FILE_DIR, "xlsx")
    for excel_file in excel_files:
        excel_file_content = read_excel(excel_file)