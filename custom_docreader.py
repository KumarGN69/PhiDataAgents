from pypdf import PdfReader
from pprint import pprint

reader = PdfReader("./documents/MosaicSOW.pdf")
contents = [page.extract_text()for page in reader.pages]

pprint(contents)