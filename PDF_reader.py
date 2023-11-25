import os
from secret_key import open_api_key
from PyPDF2 import PdfReader
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import elastic_vector_search, pinecone, weaviate, faiss
from langchain.chains.question_answering import load_qa_chain

os.environ['OPENAI_API_KEY'] = open_api_key

reader = PdfReader('/home/ubuntu/Aastha/Code/Python/PythonProjects/LLM/bhagvad_gita_english.pdf')

raw_text = ''
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        raw_text += text

raw_text[:100]

text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 1000,
    chunk_overlap = 200,
    length_function = len
)
text = text_splitter.split_text(raw_text)

embeddings = OpenAIEmbeddings()

docsearch = faiss.from_texts(text, embeddings)

chain = load_qa_chain(OpenAI(), chain_type="stuff")

query = "who are the authors of this article?"
docs = docsearch.similarity_search(query)
chain.run(input_documents=docs, question=query)
