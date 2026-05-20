#system message set the agent personality
#Human message - User query
#Ai Message - model's response
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_groq import ChatGroq
from langchain.messages import HumanMessage,AIMessage,SystemMessage

load_dotenv()
model = ChatGroq(model="llama-3.1-8b-instant")

# system_message = SystemMessage("you are a helpful assistant") #SystemMessage is an object (instance) of a class in LangChain.
# human_msg = HumanMessage("Hello , how to crack AI interview?")

# #use with chat model 

# messages = [system_message,human_msg]
# response = model.invoke(messages) # returning ai message
# #print(response.content)


# #Text prompt
# response_text_prompt = model.invoke("Write a haiku about spring")
# #print(response_text_prompt.content)

messages = [SystemMessage(content="You are a helpful assistant that can answer questions in a funny manner."),
            HumanMessage(content="who is the Prime Minister of India?")]
response = model.invoke(messages)
print(response.content)

#append the response to the messages to include the context
messages.append(response)
query_2= HumanMessage(content="What is his age?")
#append the query to the message to include the context
messages.append(query_2)
#invoke the model with the messages
response2 = model.invoke(messages)
print("----------------------------------------------------")
print(response2.content)

#chat memory
"""
System: be funny
User: who is PM of India?
Assistant: (response)
User: What is his age?

messages → LLM → response
messages + new query → LLM → response
"""


#rag system, every new query triggers retrieval again
"""
query → embedding → vector DB → retrieved docs
                                ↓
                 docs + messages → LLM
"""