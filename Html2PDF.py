import pdfkit


def Html2PDF(HtmlFilePath, PDFFilePath):
    pdfkit.from_file(HtmlFilePath, PDFFilePath)
