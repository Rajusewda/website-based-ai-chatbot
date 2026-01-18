🌐 Website-Based AI Chatbot (RAG System)

📌 Project Overview

This project is a website-based AI chatbot that answers user questions strictly based on the content of a given website.

The chatbot works by:
	•	Crawling a website
	•	Cleaning and processing the content
	•	Converting text into embeddings
	•	Storing them in a vector database
	•	Using a local Large Language Model (LLaMA-3) to generate answers only from the retrieved context

If the answer is not present on the website, the chatbot clearly responds that the information is unavailable, avoiding hallucinations.

⸻

🎯 Problem Statement

Most AI chatbots provide answers even when the information is not available in the source, which leads to hallucinations and incorrect responses.

This project solves that problem by implementing a Retrieval Augmented Generation (RAG) pipeline that ensures:
	•	Answers are grounded in real website data
	•	No guessing or external knowledge is used
	•	Safe and controlled AI behavior

⸻

🧠 Key Features
	•	🌍 Website crawling and indexing
	•	🧹 HTML content cleaning
	•	✂️ Text chunking with metadata
	•	🔢 Embedding generation
	•	🗄️ Vector storage using ChromaDB
	•	🔍 Semantic similarity search
	•	🤖 Local LLaMA-3 inference via Ollama
	•	🚫 Hallucination prevention
	•	🖥️ Simple and clean Streamlit UI

⸻

🏗️ System Architecture
	1.	User enters a website URL
	2.	Website pages are crawled
	3.	HTML content is cleaned
	4.	Text is split into chunks
	5.	Chunks are converted into embeddings
	6.	Embeddings are stored in a vector database
	7.	User asks a question
	8.	Relevant chunks are retrieved using similarity search
	9.	LLaMA-3 generates an answer only from retrieved context
	10.	If no relevant context exists, a safe fallback response is returned

⸻

🧰 Tech Stack
	•	Frontend: Streamlit
	•	Backend: Python
	•	LLM: LLaMA-3 (local, via Ollama)
	•	Embeddings: Local embedding model
	•	Vector Database: ChromaDB
	•	Frameworks/Libraries:
	•	LangChain
	•	BeautifulSoup
	•	Requests
	•	Streamlit

⸻

🚀 Local Setup & Execution (Required as per PDF)

🔹 Prerequisites
	•	Python 3.10+
	•	Git
	•	Ollama installed on system
🔹 Step 1: Clone the Repository
    git clone <your-github-repo-link>
    cd website_chatbot
🔹 Step 2: Create Virtual Environment
    python -m venv venv
    source venv/bin/activate   # macOS/Linux
🔹 Step 3: Install Dependencies
    pip install -r requirements.txt
🔹 Step 4: Install & Run Ollama

Install Ollama from:
https://ollama.com/download

Pull LLaMA-3 model:
                    ollama pull llama3
Verify installation:
                    ollama run llama3
🔹 Step 5: Run the Application
    streamlit run app.py
The app will be available at:
                            http://localhost:8501
🧪 How to Use the Chatbot
	1.	Enter a valid website URL
	2.	Click Index Website
	3.	Wait for indexing to complete
	4.	Ask questions related only to that website
	5.	If the information exists → answer is generated
	6.	If not → chatbot responds safely with a fallback message

🚫 Hallucination Control

The chatbot does not answer:
	•	Questions unrelated to the indexed website
	•	General knowledge questions
	•	Personal or speculative queries

Example:
	•	❌ “iPhone 15 price”
	•	❌ “Who is the Prime Minister of India?”

Response:

“The answer is not available in the indexed website content.”

This behavior is intentional and correct.

⸻

🌐 Streamlit Deployment Note (PDF Requirement)

This project uses a local LLaMA-3 model via Ollama.

Due to Streamlit Cloud limitations (no support for system-level binaries or local LLM runtimes), the full AI pipeline cannot run on Streamlit Cloud.

Therefore, the project is designed for local execution, and all local setup steps are clearly documented above, as allowed by the assignment requirements.

⸻

📌 Why Local LLM (LLaMA-3)?
	•	No dependency on paid APIs
	•	No API key required
	•	Better control over data privacy
	•	Demonstrates real-world AI system design
	•	Avoids vendor lock-in

The LLM layer is swappable, meaning the same architecture can support hosted APIs in production environments if required.

⸻

📄 Conclusion

This project demonstrates a production-ready Retrieval Augmented Generation system with:
	•	Safe AI behavior
	•	Real website grounding
	•	Clear architecture
	•	Practical engineering decisions

It focuses on correctness, explainability, and reliability, which are critical for real-world AI applications.

⸻

👨‍💻 Author

Raju Sewda
B.Tech (CSE/IT)
Website-Based AI Chatbot Project
