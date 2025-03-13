from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Gemini model in LangChain
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",  # Update model if needed
    temperature=0,
    google_api_key=os.getenv("GEMINI_API_KEY")  # Fetch API key from .env
)
response = model.invoke("What is the capital of India?")
print(response)