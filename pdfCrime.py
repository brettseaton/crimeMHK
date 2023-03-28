import PyPDF2
import pdfplumber
import os
import json
def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Save the extracted text to a new file
def save_text_to_json(prompt, completion, file_name):
    data = {
            'prompt': prompt,
            'completion': completion
            }
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

# Choose a file name for the output text file
output_file_name = '/Users/BrettSeaton/Desktop/jsonCrime'

pathCrime = '/Users/BrettSeaton/Desktop/pdfCrime/'
pathCitations = '/Users/BrettSeaton/Desktop/pdfCrimeCitations/'
fileFirstCrime = 'DailyArrest_Media.pdf'
fileFirstCitation = 'DailyCitationMedia.pdf'
crime_path = os.path.join(pathCrime, fileFirstCrime)
citations_path = os.path.join(pathCitations, fileFirstCitation)
# Save the extracted text to the output file
crime_text = extract_text_from_pdf(crime_path)
citation_text = extract_text_from_pdf(citations_path)
total_text = crime_text + citation_text
save_text_to_json(total_text,  output_file_name + '.json')

i = 2
while i <= 25:
    fileCrime = 'DailyArrest_Media' + str(i) + '.pdf'
    fileCitation = 'DailyCitationMedia' + str(i) + '.pdf'
    crime_path = os.path.join(pathCrime, fileCrime)
    citations_path = os.path.join(pathCitations, fileCitation)
# Save the extracted text to the output file
    crime_text = extract_text_from_pdf(crime_path)
    citation_text = extract_text_from_pdf(citations_path)
    total_text = crime_text + citation_text
    save_text_to_json(crime_text, citation_text, output_file_name + str(i) + '.txt')
    i += 1

print(f"Text saved to '{output_file_name}'")

