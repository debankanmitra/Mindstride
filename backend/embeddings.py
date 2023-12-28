# Do embeddings of textual data in a vector space like Pinecone
# https://youtu.be/ySus5ZS0b94?si=Ml_ExkivVtDLAzKe
# https://colab.research.google.com/github/openai/openai-cookbook/blob/master/examples/vector_databases/pinecone/Semantic_Search.ipynb#scrollTo=Hg0yIGu3tRNo
# https://colab.research.google.com/github/openai/openai-cookbook/blob/master/examples/vector_databases/pinecone/Gen_QA.ipynb#scrollTo=k7ut_DNBwIk1
# https://colab.research.google.com/github/openai/openai-cookbook/blob/master/examples/vector_databases/pinecone/Semantic_Search.ipynb#scrollTo=LI76-BMFhUmS
# https://platform.openai.com/docs/guides/embeddings
# https://docs.pinecone.io/docs/openai

import os
from dotenv import load_dotenv
import pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from text_processing import extract_text_from_pdf, transform_text

load_dotenv()

PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
PINECONE_ENV=os.getenv("PINECONE_ENV")
PINECONE_INDEX=os.getenv("PINECONE_INDEX")
PINECONE_METRIC=os.getenv("PINECONE_METRIC")
PINECONE_DIMENSION=os.getenv("PINECONE_DIMENSION")
TEXT_EMBEDDING_MODEL=os.getenv("TEXT_EMBEDDING_MODEL")

# initialize pinecone Datastore
pinecone.init(
    api_key=PINECONE_API_KEY,  # find at app.pinecone.io
    environment=PINECONE_ENV,  # next to api key in console
)


# First, check if our index already exists. If it doesn't, we create it
if PINECONE_INDEX not in pinecone.list_indexes():
    # we create a new index
    pinecone.create_index(
      name=PINECONE_INDEX,
      metric=PINECONE_METRIC,
      dimension=PINECONE_DIMENSION,
)


# Loading pdf, extracting text ,concatenating and transforming text
pdf_texts = extract_text_from_pdf("cow.pdf")
texts = transform_text(pdf_texts)

# # Text embeddings in vector space
embeddings = OpenAIEmbeddings(model=TEXT_EMBEDDING_MODEL)


# # The from_texts() function in Pinecone's vector store is used to upload both text documents and 
# # their corresponding embedding vectors to a specified Pinecone index.
# # this database works like a sql database there will be two columns (text and embedding)
vectorstore = Pinecone.from_texts(texts,embeddings,index_name=PINECONE_INDEX)
