# Do embeddings of textual data in a vector space like Pinecone

import os
import pinecone
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone

PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
PINECONE_ENV=os.getenv("PINECONE_ENV")
PINECONE_INDEX=os.getenv("PINECONE_INDEX")

# initialize pinecone Datastore
pinecone.init(
    api_key=PINECONE_API_KEY,  # find at app.pinecone.io
    environment=PINECONE_ENV,  # next to api key in console
)

# First, check if our index already exists. If it doesn't, we create it
if "langchain-demo" not in pinecone.list_indexes():
    # we create a new index
    pinecone.create_index(
      name="langchain-demo",
      metric='cosine',
      dimension=1536  
)

# Loading pdf
loader = PdfReader("cow.pdf")

# Reading all the pages and extracting the text and concatenate 
text = ''
for i,page in enumerate (loader.pages):
    content = page.extract_text()
    if content:
        text += content

#  Text splitters break Documents into splits of specified size
text_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " "],
    chunk_size = 500,
    chunk_overlap  = 200,
    length_function = len,
)

texts = text_splitter.split_text(text)


# Text embeddings in vector space
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

# The from_texts() function in Pinecone's vector store is used to upload both text documents and 
#their corresponding embedding vectors to a specified Pinecone index.
vectorstore = Pinecone.from_texts(texts,embeddings,index_name=PINECONE_INDEX)
