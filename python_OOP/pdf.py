import PyPDF2
pdf_file = open('sample.pdf')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
print page_content
#
# from PyPDF2 import PdfFileWriter, PdfFileReader
# import os
# import StringIO
#
# fileName = "Rukia_Resume.pdf"
# try:
#     if fileName.lower()[-3:] == "pdf":
#             input1 = PdfFileReader(file(fileName, "rb"))
#
#             # print the title of document1.pdf
#             print fileName, input1.getDocumentInfo().title
#
#             content = input1.getPage(0).extractText()
#             buf = StringIO.StringIO(content)
#             buf.readline()
#             buf.readline()
#
# except:
#         print "this is working,",
#         # print fileName, input1.getDocumentInfo().title

# import PyPDF2
# import re
#
# pdfFileObj = open(r'C:\Users\Craig\RomeoAndJuliet.pdf', mode='rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# number_of_pages = pdfReader.numPages
#
# pages_text = []
# words_start_pos = {}
# words = {}
#
# searchwords = ['romeo', 'juliet']
#
# with open('FoundWordsList.csv', 'w') as f:
#     f.write('{0},{1}\n'.format("Sheet Number", "Search Word"))
#     for word in searchwords:
#         for page in range(number_of_pages):
#             print(page)
#             pages_text.append(pdfReader.getPage(page).extractText())
#             words_start_pos[page] = [dwg.start() for dwg in re.finditer(word, pages_text[page].lower())]
#             words[page] = [pages_text[page][value:value + len(word)] for value in words_start_pos[page]]
#         for page in words:
#             for i in range(0, len(words[page])):
#                 if str(words[page][i]) != 'nan':
#                     f.write('{0},{1}\n'.format(page + 1, words[page][i]))
#                     print(page, words[page][i])

# import PyPDF2
# file = open('sample.pdf', 'rb')
# reader = PyPDF2.PdfFileReader(file)
# page = reader.getPage(0)
# print(page.extractText())
