import pandas as pd
import pdfplumber


def read_pdf(pdf_path: str) -> pd.DataFrame:
    contents = pd.DataFrame()
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            df = pd.DataFrame(table[1:], columns=table[0])
            contents = pd.concat([contents, df], ignore_index=True)
    
    contents = contents[pd.notnull(contents['학기'])]
    contents = contents[contents['학기'].str.endswith('학기')]
    
    return contents