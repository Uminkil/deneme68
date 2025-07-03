"""PDF dosyalarını vektör veritabanına eklemek için yardımcı fonksiyonlar."""

from pathlib import Path
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader

DATA_DIR = Path('data')
DB_PATH = Path('faiss_index')


def build_vector_db():
    docs = []
    for pdf_path in DATA_DIR.glob('*.pdf'):
        loader = PyPDFLoader(str(pdf_path))
        docs.extend(loader.load())
    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_documents(docs, embeddings)
    db.save_local(str(DB_PATH))

if __name__ == '__main__':
    build_vector_db()
