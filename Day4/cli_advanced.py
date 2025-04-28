import os

def get_api_key():
    return os.getenv("API_KEY", "No API Key Found")

print(get_api_key())  # Run after setting API_KEY