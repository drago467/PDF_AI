from app.chat.models import ChatArgs
from app.chat.vector_scores.pinecone import build_retriever

def build_chat(chat_args: ChatArgs):
    retriever = build_retriever(chat_args)