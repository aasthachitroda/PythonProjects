import os
from PyPDF2 import PdfReader
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import faiss
from langchain.chains.question_answering import load_qa_chain

from secret_key import open_api_key

os.environ['OPENAI_API_KEY'] = open_api_key

def load_pdf_text(pdf_path):
    reader = PdfReader(pdf_path)
    raw_text = ''
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            raw_text += text
    return raw_text

def search_answer_in_pdf(pdf_text, question):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    text = text_splitter.split_text(pdf_text)

    embeddings = OpenAIEmbeddings()

    docstore = faiss.InMemoryDocstore(embeddings)
    
    for i, t in enumerate(text):
        docstore.add(i, embeddings.embed_query(t))

    query_embedding = embeddings.embed_query(question)
    docs, distances = docstore.search(query_embedding)

    chain = load_qa_chain(OpenAI(), chain_type="stuff")
    result = chain.run(input_documents=docs, question=question)

    return result

if __name__ == "__main__":
    pdf_path = '/home/ubuntu/Aastha/Code/Python/PythonProjects/LLM/bhagvad_gita_english.pdf'
    
    user_question = input("Enter your question: ")
    
    pdf_text = load_pdf_text(pdf_path)
    answer = search_answer_in_pdf(pdf_text, user_question)
    
    print("Answer:", answer)
