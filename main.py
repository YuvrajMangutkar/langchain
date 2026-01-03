import os
import openai
os.environ.items()
import dotenv
from dotenv import load_dotenv
load_dotenv()
openai.api_key=os.environ.get("OPENAI_API_KEY")

client=openai.OpenAI()
completion=client.chat.completions.create(
    model='gpt-3.5-turbo-0125',
    messages=[{'role':'system','content':'you are the emoyii chatbot which can convert the sentence into the positive,negative and neutral by using the sentiment analysis.'},
    {'role':'user','content':'workout makes you mentally strong.'},
    ]
)
print(completion)





