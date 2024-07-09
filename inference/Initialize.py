import os
import time
import cohere
from pinecone import Pinecone, ServerlessSpec
from groq import Groq
import google.generativeai as genai
import asyncio

async def initialize_co():
    return cohere.Client(os.environ.get("COHERE_API_KEY"))

async def initialize_groq():
    return Groq(api_key=os.environ.get("GROQ_API_KEY"))

async def initialize_genai():
    genai.configure(api_key=os.environ.get("GENAI_API_KEY"))

async def initialize_pinecone():
    pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
    index_name = "mindstride"
    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )
        while not pc.describe_index(index_name).status["ready"]:
            time.sleep(1)
    return pc.Index(index_name)

async def Intialize():
    co, groq, _, index = await asyncio.gather(
        initialize_co(), 
        initialize_groq(), 
        initialize_genai(), 
        initialize_pinecone()
    )
    return co, index, groq
