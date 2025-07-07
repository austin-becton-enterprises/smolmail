import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

##API KEYS 
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")
GMAIL_CLIENT_ID = os.getenv("GMAIL_CLIENT_ID", "")
GMAIL_CLIENT_SECRET = os.getenv("GMAIL_CLIENT_SECRET", "")
GMAIL_TOKEN_PATH = os.getenv("GMAIL_TOKEN_PATH", "token.json")

## MAIL SETTINGS
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "example@gmail.com")

#APP SETTINGS 
ENV = os.getenv("ENV", "development")
ENABLE_LOGGING = os.getenv("ENABLE_LOGGING", "true").lower() == "true"
LOG_PATH = os.getenv("LOG_PATH", "logs/app.log")

# Example usage for debugging
if __name__ == "__main__":
    print("ENV:", Config.ENV)
    print("OpenAI Key:", Config.OPENAI_API_KEY[:4] + "..." if Config.OPENAI_API_KEY else "Missing")
    print("Logging Enabled:", Config.ENABLE_LOGGING)