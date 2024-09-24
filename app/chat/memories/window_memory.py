from langchain.memory import ConversationBufferMemory
from app.chat.memories.sql_memory import SqlMessageHistory

def window_buffer_memory_builder(chat_args):
    return ConversationBufferMemory(
        memory_key = "chat_history",
        output_key = "answer",
        return_messages = True,
        chat_memory = SqlMessageHistory(
            conversation_id = chat_args.conversation_id
        ),
        k = 2
    )