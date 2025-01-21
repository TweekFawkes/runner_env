import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
secret_key = os.getenv('SECRET_KEY')
database_url = os.getenv('DATABASE_URL')
api_key = os.getenv('API_KEY')
debug = os.getenv('DEBUG')

# Print the values
print(f"Secret Key: {secret_key}")
print(f"Database URL: {database_url}")
print(f"API Key: {api_key}")
print(f"Debug Mode: {debug}")