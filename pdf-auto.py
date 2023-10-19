from PyPDF2 import PdfReader, PdfWriter
from collections import Counter
import re

input_path = input("Enter the file path: ")

reader = PdfReader(input_path)

def modify_pdf(input_path, output_path):
    # Open the input PDF file in read binary mode
    with open(input_path, "rb") as input_file:
        # Create a PDF reader object
        pdf_reader = PdfReader(input_file)
        
        # Get the number of pages in the input PDF
        num_pages = len(pdf_reader.pages)
        print(f"Number of pages: {num_pages}")
        
        # Create a PDF writer object
        pdf_writer = PdfWriter()
        
        # Add all pages from the input PDF to the output PDF
        for page in range(num_pages):
            pdf_writer.add_page(pdf_reader.pages[page])
        
        # Add a blank page to the output PDF
        pdf_writer.add_blank_page()
        
    try:
    # Open the output PDF file in write binary mode
        with open(output_path, "wb") as output_file:
        # Write the output PDF to the file
            pdf_writer.write(output_file)
    except PermissionError:
    
        print(f"Permission error: Unable to write to {output_path}")


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

output_path = input_path

modify_pdf(input_path, output_path)


# Example usage
#input_path = r"C:\Users\gabri\OneDrive\Área de Trabalho\Conhecimento\Romance and Fiction\German\Ali-Hazelwood-Die-theoretische-Unwahrscheinlichkeit-von-Liebe-–-Die-deutsche-Ausgabe-von-»The-Love-H.pdf"





