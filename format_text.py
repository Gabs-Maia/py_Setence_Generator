from PyPDF2 import PdfReader, PdfWriter
from collections import Counter
import re

def modify_pdf(pdf_path, output_path):
    # Open the PDF file
    pdf = PdfReader(open(pdf_path, 'rb'))

    # Extract text from the PDF file
    text = ''
    for page in range(len(pdf.pages)):
        text += pdf.pages[page].extract_text()

    # Find all words in the text
    words = re.findall(r'\b\w+\b', text)

    # Count the frequency of each word
    word_counts = Counter(words)

    # Sort the word counts by frequency
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Convert the sorted word counts to a string
    output_string = '\n'.join([f'{word}: {count}' for word, count in sorted_word_counts])

    try:

    # Write the output string to a text file
        with open(output_path, 'w') as f:
            f.write(output_string)

    except PermissionError:
        print(f'A permission error occurred: Unable to write to {output_path}')


def words_freq(text):
    words = re.findall(r'\b\w+\b', text)
    word_counts = Counter(words)

    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    convert_to_string = ''.join(str(x) for x in sorted_word_counts)

    return convert_to_string    
