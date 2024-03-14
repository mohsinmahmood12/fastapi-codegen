import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()
#========================================================================================================================================================================================================================================================================================================================
# Application settings
REDIS_URL = os.getenv('REDIS_URL')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

if not OPENAI_API_KEY:
    raise EnvironmentError("OPENAI_API_KEY is not set in the environment variables")
