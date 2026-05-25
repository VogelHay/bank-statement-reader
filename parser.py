#!/usr/bin/python3

from pypdf import PdfReader
import csv
#import PyPDF2

statement = PdfReader('Statement_2026-05-13.pdf')
page_count = statement.get_num_pages()

def get_all():
    p = 0
    if p < page_count:
        page = statement.pages[0]
        print(page.extract_text())

def get_page(num):
    page = statement.pages[num]
    print(page.extract_text())



def main():
    #get_page(2)
    get_all()


main()
