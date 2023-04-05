from PyPDF2 import PdfReader
from main import text_per_page_in_file


def extractext(filename):
    reader = PdfReader(filename)
    number_of_pages = len(reader.pages)
    for x in range(number_of_pages):
        page = reader.pages[x]
        text = page.extract_text()
        text_per_page_in_file.append(text)
        print(text)