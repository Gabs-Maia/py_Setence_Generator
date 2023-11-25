import requests as re
import json 
from bs4 import BeautifulSoup as bs
from PyPDF2 import PdfFileReader, PdfFileWriter


def get_text():
    # Download HTML content
    url = input("Enter the desired url -: ")
    fetch_data = re.get(url)
    html = fetch_data.content

    #Parse fetched HTML 
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()
    
    #Create PDF
    output = PdfFileWriter()

    #Convert to PDF :D 

    onvert = output.addPage(PdfFileReader(BytesIO(text.encode("utf-8"))))

