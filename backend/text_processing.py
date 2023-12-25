## extract and Processes text from pdf
## to get systematic pdf output: https://burdoc.readthedocs.io/en/latest/getting_started.html

import os
import re
from dotenv import load_dotenv
import openai
from PyPDF2 import PdfReader
from text_encoding import tiktoken_len
from langchain.text_splitter import RecursiveCharacterTextSplitter


load_dotenv()

TEXT_EMBEDDING_MODEL=os.getenv("TEXT_EMBEDDING_MODEL")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

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
    # remove newlines that occur in the middle of sentences
    # removed_extraline_texts = re.compile(r"\n(?=[a-z])").sub("", text)

    # Removing hyphens that are at the end of lines
    cleaned_text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', text)

    # Remove extra whitespaces
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

    # Remove repeated characters (e.g., "helloooo" becomes "hello")
    cleaned_text = re.sub(r'(.)\1{2,}', r'\1', cleaned_text)

    # Remove leading and trailing spaces
    cleaned_text = cleaned_text.strip()

    # Remove special characters and punctuation
    text = re.sub(r'[^a-zA-Z0-9\s]', '', cleaned_text)

    # Convert to lowercase
    text = text.lower()
    
    return text

def text_replace(texts):
    cleaned_texts = [text.replace("\n", " ") for text in texts]
    cleaned_texts = [re.sub(r'\s+', ' ', text) for text in cleaned_texts]
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

# experimental
def get_embeddings(texts):
    openai.api_key = OPENAI_API_KEY
    embeddings = openai.Embedding.create(input=texts, engine=TEXT_EMBEDDING_MODEL).data[0].embedding
    return embeddings