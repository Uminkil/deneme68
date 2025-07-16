"""Kullanıcı sorularını vektör veritabanı üzerinden yanıtlar."""

from pathlib import Path
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

DB_PATH = Path('faiss_index')

def load_qa_chain():
    embeddings = HuggingFaceEmbeddings()
    db = FAISS.load_local(str(DB_PATH), embeddings)
    llm = OpenAI(temperature=0.2)
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=db.as_retriever()
    )

_chain = None


def retrieve_answer(query: str) -> str:
    global _chain
    if _chain is None:
        _chain = load_qa_chain()
    result = _chain({"query": query})
    return result['result']
