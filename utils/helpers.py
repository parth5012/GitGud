from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
import os

def create_embeddings():
    pass

def store_embeddings():
    pass

def get_llm():
    api_key = os.getenv('GOOGLE_API_KEY')
    return ChatGoogleGenerativeAI(model = 'gemini-2.5-flash',api_key=api_key)