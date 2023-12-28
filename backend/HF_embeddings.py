import pinecone
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain.vectorstores import Pinecone

from text_processing import extract_text_from_pdf, transform_text

pinecone.init(
    api_key='078c0c2d-f856-4c05-8f89-cb3b5f50b54d', 
    environment='gcp-starter',  
)
# implement the whole without langchain

# First, check if our index already exists. If it doesn't, we create it
if 'legal-gpt' not in pinecone.list_indexes():
    # we create a new index
    pinecone.create_index(
      name='legal-gpt',
      metric='cosine',
      dimension=1024,
)
    

pdf_texts = extract_text_from_pdf("cow.pdf")
texts = transform_text(pdf_texts)

embeddings = HuggingFaceInferenceAPIEmbeddings(api_key='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',model_name="llmrails/ember-v1")
# query_result = embeddings.embed_query(texts[0])
# print(query_result)
#vectorstore = Pinecone.from_texts(texts,embeddings,index_name='legal-gpt')
for text in texts:
    vectorstore = Pinecone.from_texts([text],embeddings,index_name='legal-gpt')

