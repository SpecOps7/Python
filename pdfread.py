import PyPDF2
pdfFileObj = open("Devopsfordummies.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages

pageObj = pdfReader.getPage(o)
pageObj.extractText()
