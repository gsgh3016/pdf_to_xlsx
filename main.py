PDF_FILE_DIR = "pdf/"
EXCEL_FILE_DIR = "excel/"


from utils import *
import fitz


if __name__ == "__main__":
    check_dir(PDF_FILE_DIR)
    pdf_files = scan_files(PDF_FILE_DIR, "pdf")
    text = ""
    for pdf_file in pdf_files:
        doc = fitz.open(pdf_file)
        for page in doc:
            text += page.get_text()
            
    excel_files = scan_files(EXCEL_FILE_DIR, "xlsx")
    for excel_file in excel_files:
        excel_file_content = read_excel(excel_file)