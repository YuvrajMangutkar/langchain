from langchain.messages import HumanMessage
from langchain_core.messages import ChatMessage
from langchain_ollama import ChatOllama

llm = ChatOllama(model="Mistral")

messages = [
    ChatMessage(role="control", content="thinking"),
    HumanMessage("229+130=?"),
]

response = llm.invoke(messages)
print(response.content)