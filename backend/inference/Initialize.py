import os
import time
import cohere
from pinecone import Pinecone, ServerlessSpec
from groq import Groq
import google.generativeai as genai


async def Intialize():

    # using the global keyword we can modify global variables inside functions
    # Also tells Python to use the global variables from the global scope
    # global co, groq, index

    # initialize cohere
    co = cohere.Client(os.environ.get("COHERE_API_KEY"))

    # initialize Groq api
    groq = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    # initialize genai
    genai.configure(api_key=os.environ.get("GENAI_API_KEY"))

    # initialize pinecone Datastore
    pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))

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
    return co, index, groq