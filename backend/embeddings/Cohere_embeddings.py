import os
import time
# from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from langchain_cohere import CohereEmbeddings
# from langchain.vectorstores import Pinecone
from langchain_pinecone import PineconeVectorStore


from text_processing import extract_text_from_pdf, transform_text


PINECONE_API_KEY="d96e1268-d194-4baf-a21e-8439099d741b"
COHERE_API_KEY="qFJX4khcWaZNcRzOdmcHRQTlwfU1tfmRTmzvCGP6"

# initialize pinecone Datastore
pc = Pinecone(api_key="d96e1268-d194-4baf-a21e-8439099d741b")

index_name = "mindstride"
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1024,
        metric="cosine",
        spec=ServerlessSpec(
            cloud='aws', 
            region='us-east-1'
        ) 
    )
    while not pc.describe_index(index_name).status["ready"]:
        time.sleep(1) 

index = pc.Index(index_name)


# Loading pdf, extracting text ,concatenating and transforming text
pdf_texts = extract_text_from_pdf("chatgpt.pdf")
texts = transform_text(pdf_texts)


os.environ["COHERE_API_KEY"] = COHERE_API_KEY
embeddings = CohereEmbeddings(model="embed-english-v3.0")


# The from_texts() function in Pinecone's vector store is used to upload both text documents and 
# their corresponding embedding vectors to a specified Pinecone index.
# this database works like a sql database there will be two columns (text and embedding)
print("Uploading to Pinecone")
for text in texts:
    # PineconeVectorStore.from_texts([text], embeddings, index_name=index_name,api_key=PINECONE_API_KEY)
    # index.upsert([(text, embeddings.embed_query(text))])
    print(text)
    print(embeddings.embed_query(text))
    break

