
import nltk
nltk.download('punkt')


import PyPDF2
from nltk.tokenize import sent_tokenize

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    pdf_file.close()
    return text

# Function to summarize text based on sentence extraction
def summarize_text(text, num_sentences=3):
    sentences = sent_tokenize(text)
    summarized_sentences = sentences[:num_sentences]
    summarized_text = ' '.join(summarized_sentences)
    return summarized_text

if __name__ == "__main__":
    pdf_path = r"C:/Users/Sharanbasavaraj.G/Downloads/Text_Summarization.pdf"

    extracted_text = extract_text_from_pdf(pdf_path)
    summarized_text = summarize_text(extracted_text)

    print("Summarized Text:")
    print(summarized_text)
