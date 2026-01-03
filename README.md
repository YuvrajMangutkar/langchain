<h1>LangChain Learning Repository</h1>
<hr>

<p>
This repository is created to learn LangChain concepts step by step using the latest
LangChain architecture and local Large Language Models (LLMs).
</p>

<hr>

<h2>Objective</h2>
<p>
The objective of this repository is to understand how Large Language Models (LLMs)
are used in real-world applications and how LangChain helps in building intelligent,
context-aware, reasoning-based, and deployable AI systems.
</p>

<hr>

<h2>Modules to Learn</h2>
<p>
Model Input<br>
Model Output<br>
Chatbot Memory<br>
Document Retrieval<br>
Agent Tooling<br>
LangChain Expression Language (LCEL)
</p>

<hr>

<h2>LangChain Components Overview</h2>

<h3>1. LangChain Community</h3>
<p>
LangChain Community is used for integrations, model access, retrieval systems,
and agent tooling.
</p>

<h4>Model Input</h4>
<p>
Prompts<br>
PromptTemplate
</p>

<h4>Model Output</h4>
<p>
Output Parsers
</p>

<h4>Retrieval (RAG Components)</h4>
<p>
Context Awareness<br>
Retriever<br>
Document Loader<br>
Text Splitter<br>
Embedding Model<br>
Vector Store
</p>

<h4>Agent Tooling</h4>
<p>
Tool<br>
Toolkit<br>
Reasoning-based execution
</p>

<hr>

<h3>2. LangChain Core</h3>
<p>
LangChain Core contains the core abstractions and execution logic.
</p>

<p>
LangChain Expression Language (LCEL)<br>
Runnable interfaces<br>
Chain composition
</p>

<hr>

<h3>3. LangSmith</h3>
<p>
LangSmith is used for observability and debugging of LangChain applications.
</p>

<p>
Execution tracing<br>
Prompt monitoring<br>
Performance analysis<br>
Error inspection
</p>

<hr>

<h3>4. LangServe</h3>
<p>
LangServe is used for deploying LangChain applications.
</p>

<p>
API-based deployment<br>
Production-ready serving
</p>

<hr>

<h2>Technologies Used</h2>
<p>
Python<br>
LangChain<br>
Ollama (Local LLMs)<br>
Vector Databases (ChromaDB / FAISS)<br>
LangSmith<br>
LangServe
</p>

<hr>

<h2>Example: Simple LangChain Pipeline (LCEL)</h2>

<pre>
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} like I am a beginner."
)

chain = prompt | llm

print(chain.invoke({"topic": "LangChain"}))
</pre>

<hr>

<h2>Setup Instructions</h2>

<p>
Step 1: Create virtual environment<br>
python -m venv venv<br>
venv\Scripts\activate
</p>

<p>
Step 2: Install dependencies<br>
pip install langchain langchain-core langchain-community ollama
</p>

<p>
Step 3: Run local LLM<br>
ollama run llama3
</p>

<hr>

<h2>Learning Outcomes</h2>
<p>
After completing this repository, you will be able to build LLM-powered applications,
implement Retrieval-Augmented Generation (RAG), create reasoning-based AI agents,
deploy LangChain applications, and monitor and debug LLM workflows.
</p>

<hr>


<h2>Author</h2>
<p>
Yuvraj Mangutkar<br>
AI and Data Science Engineering Student
</p>

<hr>
