## extract and Processes text from pdf

import re
from PyPDF2 import PdfReader
from text_encoding import tiktoken_len
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Text Extraction
def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content
    texts = clean_text(text)
    return texts

# Cleaning and Normalization
def clean_text(text):
    # Remove special characters and punctuation
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    return text

def text_replace(texts):
    cleaned_texts = [text.replace("\n", " ") for text in texts]
    return cleaned_texts


# Document transformation 
# Text splitting
# When you want to deal with long pieces of text, it is necessary to split up that text into chunks. 
# As simple as this sounds, there is a lot of potential complexity here. 
# Ideally, you want to keep the semantically related pieces of text together

def transform_text(text):
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=20,
    length_function=tiktoken_len,
    separators=["\n\n", "\n", " ", ""]
    )

    chunks= text_splitter.split_text(text)

    return text_replace(chunks)