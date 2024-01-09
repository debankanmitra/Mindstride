# https://cookbook.openai.com/examples/deterministic_outputs_with_the_seed_parameter

import os
import pinecone
import openai
from langchain.chains import RetrievalQA
from langchain.vectorstores import Pinecone
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings



# APIS
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
PINECONE_ENV = os.environ["PINECONE_ENV"]
PINECONE_INDEX = os.environ["PINECONE_INDEX"]
TEXT_EMBEDDING_MODEL = os.environ["TEXT_EMBEDDING_MODEL"]
HF_MODEL = os.environ["HF_MODEL"]
HF_API = os.environ["HF_API"]


def query_from_model(query):

    # initialize pinecone Datastore
    pinecone.init(
        api_key=PINECONE_API_KEY,  # find at app.pinecone.io
        environment=PINECONE_ENV,  # next to api key in console
    )

    # Text embeddings in vector space
    embeddings = HuggingFaceInferenceAPIEmbeddings(api_key=HF_API, model_name=HF_MODEL)
    vectorstore = Pinecone.from_existing_index(PINECONE_INDEX, embeddings)

    # Similarity search (retrieval)
    vectorstore.similarity_search(
        query, k=5
    )  # k = 5  => number of documents to retrieve

    # LLM produced answer using Generation (Method 1)
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0.76,
        max_tokens=100,
        model_kwargs={"seed": 235, "top_p": 0.01},
        streaming=True,
    )

    # We can also include the sources of information that the LLM is using to answer our question.
    # We can do this using a slightly different version of RetrievalQA called RetrievalQAWithSourcesChain
    chain = RetrievalQA.from_chain_type(
        llm, chain_type="stuff", retriever=vectorstore.as_retriever()
    )
    answer = chain.run(
        {
            "query": query
            + "you are a therapist who help people with personal development and self improvement"
            + "You can only make conversations related to the provided context. If a response cannot be formed strictly using the context, politely say you don’t have knowledge about that topic."
            + "[strictly within 75 words]"
        }
    )
    return answer


# You can only make conversations related to the provided context. If a response cannot be formed strictly using the context, politely say you don’t have knowledge about that topic."


# print(query_from_model("who is swami vivekenanda?"))


# LLM produced answer using Generation (Method: 2 )
# chain=load_qa_chain(OpenAI(),chain_type="stuff")
# answer=chain.run(input_documents=docs,question=query)
# print(answer)
