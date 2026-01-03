from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama

llm = Ollama(
    model="mistral",  # must exist in `ollama list`
    base_url="http://localhost:11434"
)

prompt = PromptTemplate(
    input_variables=["topic"],
    template="determine  {topic} is an positive,negative or neutral senetence"
)

chain = prompt | llm

print(chain.invoke({"topic": "i enjoying solving the leetcode problems daily."}))
