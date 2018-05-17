# -*- coding: utf-8 -*-

from PyPDF2 import PdfFileMerger

pdfs = ['sample.pdf', 'sample2.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")

