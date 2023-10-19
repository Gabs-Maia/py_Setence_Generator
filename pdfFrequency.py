from PyPDF2 import PdfReader, PdfWriter
from collections import Counter
import re

# Open the PDF file
pdf_file = input_path
pdf = PdfReader(open(pdf_file, 'rb'))

# Extract text from the PDF file
text = ''
for page in pdf.pages:
    text += page.extract_text()
      
# Create a frequency list of German words
words = re.findall(r'\b\w+\b', text)
word_counts = Counter(words)
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
convert_to_string = ''.join(str(x) for x in sorted_word_counts)

with open('frequency_list.txt', 'a') as frequency_list:
    frequency_list.write(convert_to_string)










