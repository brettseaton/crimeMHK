import PyPDF2
import pdfplumber
import os
def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Save the extracted text to a new file
def save_text_to_file(text, file_name):
    with open(file_name, 'w', encoding='utf-8') as text_file:
        text_file.write(text)

# Choose a file name for the output text file
output_file_name = '/Users/BrettSeaton/Desktop/pdfCrime/arrests'

path = '/Users/BrettSeaton/Desktop/pdfCrime/'
i = 0
for file in os.listdir(path):
    i += 1
    pdf_path = os.path.join(path, file)
# Save the extracted text to the output file
    pdf_text = extract_text_from_pdf(pdf_path)
    save_text_to_file(pdf_text, output_file_name + str(i) + '.txt')

print(f"Text saved to '{output_file_name}'")

