from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings


load_dotenv()

#model_openai = ChatOpenAI(model="gpt-4.1-nano", seed=6)
model_openai = ChatGroq(model="llama-3.1-8b-instant")

model_google = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

m1="who is the president of the united states?"
m2="what is his age"

response_openai = model_openai.invoke(m1)
response_google = model_google.invoke(m1)


print(f"OpenAI : {response_openai.content}")
print(f"Google :{response_google.content}")



response_openai = model_openai.invoke(m2)
response_google = model_google.invoke(m2)

print(f"OpenAI : {response_openai.content}")
print(f"Google :{response_google.content}")

print("-----------------------------------------")
print("OpenAI: ",response_openai)
print("Goole :", response_google)

print("--------------------------------------------")
print(f"Type of object:{type(response_openai)}")