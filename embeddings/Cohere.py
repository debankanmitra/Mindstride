import os
import time
import uuid
import cohere
from pinecone import Pinecone, ServerlessSpec
from text_processing import extract_text_from_pdf, transform_text


# initialize cohere
co = cohere.Client("eiHcU0xKgplwRKQXyVveuqhFqITcuMrM2BUapyyz")


# initialize pinecone Datastore
pc = Pinecone(api_key="d96e1268-d194-4baf-a21e-8439099d741b")

index_name = "mindstride"
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,
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
pdf_texts = extract_text_from_pdf("Don't Believe Everything You Think.pdf")
texts = transform_text(pdf_texts)

# The from_texts() function in Pinecone's vector store is used to upload both text documents and 
# their corresponding embedding vectors to a specified Pinecone index.
# this database works like a sql database there will be two columns (text and embedding)
print("Uploading to Pinecone")


for text in texts:
    embedding = co.embed(texts=[text],model="embed-english-light-v3.0", input_type="search_document").embeddings[0]
    unique_id = str(uuid.uuid4())
    # create list of (id, vector, metadata) tuples to be upserted
    to_upsert = [(unique_id, embedding, {'text': text})]
    index.upsert(vectors=to_upsert)
    time.sleep(20)

# let's view the index statistics
# print(index.describe_index_stats())