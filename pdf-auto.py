from format_text import modify_pdf, words_freq
from PyPDF2 import PdfReader, PdfWriter
from collections import Counter
import re

input_path = input("Enter the file path: ")

# Open the PDF file
pdf = PdfReader(input_path)

text = ''
for page in pdf.pages:
    text += page.extract_text()

convert_to_string = words_freq(text)
      
with open('frequency_list.txt', 'a') as frequency_list:
    frequency_list.write(convert_to_string)

output_path = "output.pdf"

modify_pdf(input_path, output_path)
