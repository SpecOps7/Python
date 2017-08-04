#! python2
import PyPDF2
pdfFileObj = open('Devopsfordummies.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages

pageObj = pdfReader.getPage(12)
pageObj.extractText()
