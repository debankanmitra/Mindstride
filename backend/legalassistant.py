# https://cookbook.openai.com/examples/deterministic_outputs_with_the_seed_parameter

import os
import pinecone
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.vectorstores import Pinecone
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain.chains.question_answering import load_qa_chain

load_dotenv()


# APIS
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
PINECONE_ENV=os.getenv("PINECONE_ENV")
PINECONE_INDEX=os.getenv("PINECONE_INDEX")
TEXT_EMBEDDING_MODEL=os.getenv("TEXT_EMBEDDING_MODEL")
HF_MODEL=os.getenv("HF_MODEL")
HF_API=os.getenv("HF_API")
# initialize pinecone Datastore
pinecone.init(
    api_key=PINECONE_API_KEY,  # find at app.pinecone.io
    environment=PINECONE_ENV,  # next to api key in console
)




# Text embeddings in vector space
embeddings = HuggingFaceInferenceAPIEmbeddings(api_key=HF_API ,model_name=HF_MODEL)

vectorstore = Pinecone.from_existing_index(PINECONE_INDEX, embeddings)

# Similarity search (retrieval)
query = "how to break bad habits?"
docs = vectorstore.similarity_search(query,k=5) # k = 5  => number of documents to retrieve

# LLM produced answer using Generation (Method 1)
llm = ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0.76, max_tokens=100, model_kwargs={"seed":235, "top_p":0.01})
# We can also include the sources of information that the LLM is using to answer our question. 
#We can do this using a slightly different version of RetrievalQA called RetrievalQAWithSourcesChain
chain = RetrievalQA.from_chain_type(llm, chain_type="stuff", retriever=vectorstore.as_retriever())
answer=chain.run({"query": query + "You can only make conversations related to the provided context. If a response cannot be formed strictly using the context, politely say you don’t have knowledge about that topic."+"[strictly within 75 words]"})
print(answer)


# LLM produced answer using Generation (Method: 2 )
# chain=load_qa_chain(OpenAI(),chain_type="stuff")
# answer=chain.run(input_documents=docs,question=query)
# print(answer)