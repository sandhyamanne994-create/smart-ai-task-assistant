import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Please check your .env file.")

# Connect to OpenAI
client = OpenAI(api_key=api_key)

# Send a small test request
response = client.responses.create(
    model="gpt-4.1-mini",
    input="Say hello in Telugu in one short sentence."
)

print("OpenAI Connection Successful!")
print(response.output_text)