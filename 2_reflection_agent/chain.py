from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import ChatOllama


# Generator Chain
generation_prompt = ChatPromptTemplate.from_messages([
    ("system",  "You are a twitter techie influencer assitant tasked with writing excellent twitter posts."
                "Generate the best twitter post possible for user's request."
                "If the user provides critique, respond with a revised version of you previous attemps."),
    MessagesPlaceholder(variable_name="messages")
])


# Reflector Chain
reflecton_prompt = ChatPromptTemplate.from_messages([
    (
        'system',   'You are a viral twitter influencer grading a tweet. Generate critique and recommendations for the users tweet.'
                    'Always provide detailed recommendations, including requests for length, virality, style, etc'
    ),
    MessagesPlaceholder(variable_name="messages")
])

llm = ChatOllama(model='llama3.2')

generation_chain = generation_prompt | llm
reflection_chain = reflecton_prompt | llm

# print(
#     generation_chain.invoke(
#         [
#             'Trump'
#         ]
#     ).content
# )