import PyPDF2
from sys import argv

inputs = argv[1:]


with open(inputs[0], "rb") as fileInfo:
    pdfInfo = PyPDF2.PdfFileReader(fileInfo)
    with open(inputs[1], "rb") as fileWtr:
        pdfWtr = PyPDF2.PdfFileReader(fileWtr)

        pdfFinal = PyPDF2.PdfFileWriter()
        for i in range(pdfInfo.getNumPages()):
            page = pdfInfo.getPage(i)
            page.mergePage(pdfWtr.getPage(0))
            pdfFinal.addPage(page)

        with open("wattered.pdf", "wb") as fileWattered:
            pdfFinal.write(fileWattered)
