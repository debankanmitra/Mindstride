import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
#from langchain.vectorstores import FAISS
from langchain.vectorstores import Pinecone
import pinecone


from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# from langchain.llms import OpenAI
# from langchain.chains.question_answering import load_qa_chain



# APIS
os.environ['OPENAI_API_KEY'] = "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"
os.environ["PINECONE_API_KEY"] = "2672f1e3-68be-4a5f-a00f-a53428cf43e9"
os.environ["PINECONE_ENV"] = "gcp-starter"

# initialize pinecone Datastore
pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),  # find at app.pinecone.io
    environment=os.getenv("PINECONE_ENV"),  # next to api key in console
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
loader = PdfReader("constitution.pdf")

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
embeddings = OpenAIEmbeddings()
#vectorstore = FAISS.from_texts(texts, embeddings)
vectorstore = Pinecone.from_texts(texts,embeddings,index_name="langchain-demo")

# Similarity search (retrieval)
query = "why a lion roar?"
docs = vectorstore.similarity_search(query)
# print(docs[0].page_content)


# LLM produced answer using Generation (Method 1)
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
chain = RetrievalQA.from_chain_type(llm,retriever=vectorstore.as_retriever())
answer=chain({"query": query})
print(answer["result"])


# LLM produced answer using Generation (Method: 2 )
# chain=load_qa_chain(OpenAI(),chain_type="stuff")
# answer=chain.run(input_documents=docs,question=query)
# print(answer)