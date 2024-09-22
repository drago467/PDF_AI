from app.chat.models import ChatArgs
from app.chat.vector_scores.pinecone import build_retriever
from langchain.chains import ConversationalRetrievalChain
from app.chat.llms.chatopenai import build_llm
from app.chat.memories.sql_memory import build_memory
from app.chat.chains.retrieval import StreamingConversationalRetrievalChain

def build_chat(chat_args: ChatArgs):
    retriever = build_retriever(chat_args)
    llm = build_llm(chat_args)
    memory = build_memory(chat_args)

    return StreamingConversationalRetrievalChain.from_llm(
        llm = llm,
        memory = memory,
        retriever = retriever
    )