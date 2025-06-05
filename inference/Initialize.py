import os
import time
import cohere
from pinecone import Pinecone, ServerlessSpec
from groq import Groq
import google.generativeai as genai
import asyncio

async def initialize_co():
    return cohere.Client('R9SEqqMXEvlr6puuLoGOoRWnJ2Hobv1Ci50aqWgI')

async def initialize_groq():
    return Groq(api_key='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')

async def initialize_genai():
    genai.configure(api_key='AIzaSyC1cxcQNpntxkFbg-Ka5sy-EAAMErvjAiU')

async def initialize_pinecone():
    pc = Pinecone(api_key='d96e1268-d194-4baf-a21e-8439099d741b')
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
