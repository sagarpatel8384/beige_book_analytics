from io import StringIO
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfdocument import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import TextConverter

class TextParser(object):
    """
    TexParser Class reads a file passed as an argument in the command line
    and converts the pdf to text. The output is saved to a text file.
    """

    def __init__(self, pdf):
        self.output_text = ""
        parser = PDFParser(open(pdf, 'rb'))
        document = PDFDocument(parser)

        if not document.is_extractable:
            raise PDFTextExtractionNotAllowed

        resource_manager = PDFResourceManager()
        return_string = StringIO()
        device = TextConverter(resource_manager, return_string)
        interpreter = PDFPageInterpreter(resource_manager, device)

        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
	
        self.records = []
        lines = return_string.getvalue().splitlines()

        for line in lines:
            self.output_text += line


