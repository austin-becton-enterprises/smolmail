import os
from dotenv import load_dotenv
import openai

def setup_openai():
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")