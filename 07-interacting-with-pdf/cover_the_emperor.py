# Copyright (c) 2016 Ami . All rights reserved

from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def read_pdf_file(input_file_name):
    return PdfFileReader(open(input_file_name, "rb"))

def write_pdf_file(pages, output_file_name):
    os.makedirs(os.path.dirname(output_file_name), exist_ok=True)
    output_file = open(output_file_name, "wb")
    output_pdf = PdfFileWriter()

    for page in pages:
        output_pdf.addPage(page)

    output_pdf.write(output_file)
    output_file.close()

def get_pages(pdf_file):
    pages = []

    for page_num in range(0, pdf_file.getNumPages()):
        pages.append(pdf_file.getPage(page_num))

    return pages

def main():
    script_folder = os.path.dirname(__file__)
    input_file_name = os.path.join(script_folder, "The Emperor.pdf")
    cover_file_name = os.path.join(script_folder, "Emperor cover sheet.pdf")
    output_file_name = os.path.join(script_folder, "Output/The Covered Emperor.pdf")
    input_file = read_pdf_file(input_file_name)
    cover_page = read_pdf_file(cover_file_name).getPage(0)

    pages = get_pages(input_file)
    pages.insert(0, cover_page)
    print("Joining cover with pdf...", end="")
    write_pdf_file(pages, output_file_name)
    print("Done")

if __name__ == "__main__":
    main()
