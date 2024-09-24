from langchain.chains import ConversationalRetrievalChain
from app.chat.chains.streamable import StreamableChain
from .traceable import TraceableChain
class StreamingConversationalRetrievalChain(
    TraceableChain, StreamableChain, ConversationalRetrievalChain
):
    pass