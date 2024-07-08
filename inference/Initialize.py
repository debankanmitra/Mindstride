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
    co = cohere.Client("R9SEqqMXEvlr6puuLoGOoRWnJ2Hobv1Ci50aqWgI")

    # initialize Groq api
    groq = Groq(
        api_key="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",
    )

    # initialize genai
    genai.configure(api_key="AIzaSyC1cxcQNpntxkFbg-Ka5sy-EAAMErvjAiU")

    # initialize pinecone Datastore
    pc = Pinecone(api_key="d96e1268-d194-4baf-a21e-8439099d741b")

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

    index = pc.Index(index_name)
    return co, index, groq
