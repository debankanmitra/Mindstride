import os
import pinecone
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.vectorstores import Pinecone
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain

load_dotenv()


# APIS
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
PINECONE_ENV=os.getenv("PINECONE_ENV")
PINECONE_INDEX=os.getenv("PINECONE_INDEX")

# initialize pinecone Datastore
pinecone.init(
    api_key=PINECONE_API_KEY,  # find at app.pinecone.io
    environment=PINECONE_ENV,  # next to api key in console
)




# Text embeddings in vector space
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

vectorstore = Pinecone.from_existing_index(PINECONE_INDEX, embeddings)

# Similarity search (retrieval)
query = "what is a tiger?"
docs=vectorstore.similarity_search(query,k=3) # k = 5  => number of documents to retrieve


# LLM produced answer using Generation (Method 1)
llm = ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0.43, max_tokens=50)
# We can also include the sources of information that the LLM is using to answer our question. 
#We can do this using a slightly different version of RetrievalQA called RetrievalQAWithSourcesChain
chain = RetrievalQA.from_chain_type(llm, chain_type="stuff", retriever=vectorstore.as_retriever())
answer=chain.run({"query": query})
print(answer)


# LLM produced answer using Generation (Method: 2 )
# chain=load_qa_chain(OpenAI(),chain_type="stuff")
# answer=chain.run(input_documents=docs,question=query)
# print(answer)