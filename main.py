import os
os.environ.items()
import dotenv
from dotenv import load_dotenv
load_dotenv()
API_KEY=os.environ.get("OPENAI_API_KEY")
print(API_KEY)
