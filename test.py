from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(streaming = True)

prompt = ChatPromptTemplate.from_messages([
    ("human", "{content}")
])

chain = LLMChain(llm = chat, prompt = prompt)

for output in chain.stream(input = {"content" : "tell me a joke"}):
    print(output)

# messages = prompt.format_messages(content = "tell me a joke")

# for message in chat.stream(messages):
#     print(message.content)
