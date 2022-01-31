import PyPDF2
from sys import argv

inputs = argv[1:]


def myRotate(page):
    page.rotateCounterClockwise(90)
    return page


def createPDFonePage(page, name):
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open(name, "wb") as newFile:
        writer.write(newFile)

def combinePDF(pdfList):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdfList:
        merger.append(pdf)
    merger.write("superFile.pdf")

with open("dummy.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    print(reader.getPage(0))

    # rotar pdf
    rotatedPage = myRotate(reader.getPage(0))
    createPDFonePage(rotatedPage, "tilt.pdf")

    combinePDF(inputs)
