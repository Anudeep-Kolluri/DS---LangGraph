from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


llm = ChatOllama(model = 'llama3.2')

template = ChatPromptTemplate([
    ('system', 'You are a helpful assistant who answer the question in one word'),
    ('human', 'a for ')
])


chain = template | llm


print(chain.invoke({}))