import os
from dotenv import load_dotenv
import pinecone
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain.vectorstores import Pinecone

from embeddings.text_processing import extract_text_from_pdf, transform_text

load_dotenv()
PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
PINECONE_ENV=os.getenv("PINECONE_ENV")
PINECONE_INDEX=os.getenv("PINECONE_INDEX")
PINECONE_METRIC= os.getenv("PINECONE_METRIC")
PINECONE_DIMENSION= os.getenv("PINECONE_DIMENSION")
HF_API=os.getenv("HF_API")
HF_MODEL=os.getenv("HF_MODEL")

pinecone.init(
    api_key=PINECONE_API_KEY, 
    environment=PINECONE_ENV,  
)


# First, check if our index already exists. If it doesn't, we create it
if PINECONE_INDEX not in pinecone.list_indexes():
    pinecone.create_index(
      name=PINECONE_INDEX,
      metric=PINECONE_METRIC,
      dimension=PINECONE_DIMENSION,
)
    

pdf_texts = extract_text_from_pdf("Atomic Habits.pdf")
texts = transform_text(pdf_texts)

embeddings = HuggingFaceInferenceAPIEmbeddings(api_key=HF_API, model_name=HF_MODEL)

for text in texts:
    vectorstore = Pinecone.from_texts([text], embeddings, index_name=PINECONE_INDEX)

