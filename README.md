
# 🌐 Website-Based AI Chatbot (RAG System)

## 📌 Project Overview

This project is a website-based AI chatbot that answers user questions strictly based on the content of a given website.

The chatbot works by:
- Crawling a website
- Cleaning and processing the content
- Converting text into embeddings
- Storing them in a vector database
- Using a local Large Language Model (LLaMA-3) to generate answers only from the retrieved context

If the answer is not present on the website, the chatbot clearly responds that the information is unavailable, avoiding hallucinations.

---

## 🎯 Problem Statement

Most AI chatbots provide answers even when the information is not available in the source, which leads to hallucinations and incorrect responses.

This project solves that problem by implementing a Retrieval Augmented Generation (RAG) pipeline that ensures:
- Answers are grounded in real website data
- No guessing or external knowledge is used
- Safe and controlled AI behavior

---

## 🧠 Key Features

- Website crawling and indexing  
- HTML content cleaning  
- Text chunking with metadata  
- Embedding generation  
- Vector storage using ChromaDB  
- Semantic similarity search  
- Local LLaMA-3 inference via Ollama  
- Hallucination prevention  
- Simple and clean Streamlit UI  

---

## 🏗️ System Architecture

1. User enters a website URL  
2. Website pages are crawled  
3. HTML content is cleaned  
4. Text is split into chunks  
5. Chunks are converted into embeddings  
6. Embeddings are stored in a vector database  
7. User asks a question  
8. Relevant chunks are retrieved using similarity search  
9. LLaMA-3 generates an answer only from retrieved context  
10. If no relevant context exists, a safe fallback response is returned  

---

## 🧰 Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **LLM:** LLaMA-3 (local, via Ollama)  
- **Embeddings:** Local embedding model  
- **Vector Database:** ChromaDB  

Libraries and tools:
- LangChain  
- BeautifulSoup  
- Requests  
- Streamlit  

---

## 🚀 Local Setup & Execution (As Required in PDF)

### 🔹 Prerequisites

- Python 3.10 or higher  
- Git  
- Ollama installed  

---

### 🔹 Step 1: Clone the Repository

```bash
git clone https://github.com/Rajusewda/website-based-ai-chatbot
cd website-based-ai-chatbot


⸻

🔹 Step 2: Create Virtual Environment

python -m venv venv
source venv/bin/activate   # macOS/Linux


⸻

🔹 Step 3: Install Dependencies

pip install -r requirements.txt


⸻

🔹 Step 4: Install & Run Ollama

Download Ollama from:
https://ollama.com/download

Pull the LLaMA-3 model:

ollama pull llama3

Verify installation:

ollama run llama3


⸻

🔹 Step 5: Run the Application

streamlit run app.py

The application will be available at:

http://localhost:8501


⸻

🧪 How to Use the Chatbot
	1.	Enter a valid website URL
	2.	Click Index Website
	3.	Wait for indexing to complete
	4.	Ask questions related only to the indexed website

If the information exists, the chatbot answers it.
If not, it responds safely with a fallback message.

⸻

🚫 Hallucination Control

The chatbot intentionally does not answer:
	•	General knowledge questions
	•	Questions unrelated to the indexed website

Example:
	•	“iPhone 15 price”
	•	“Who is the Prime Minister of India?”

Response:

The answer is not available in the indexed website content.


⸻

🌐 Streamlit Deployment Note

This project uses a locally hosted LLaMA-3 model via Ollama.

Due to Streamlit Cloud limitations (no support for system-level binaries or local LLM runtimes), the full AI pipeline cannot run on Streamlit Cloud.

The project is designed for local execution, and complete local setup steps are provided above.

⸻

📌 Why Local LLaMA-3?
	•	No dependency on paid APIs
	•	No API keys required
	•	Better control over data privacy
	•	Avoids vendor lock-in

The LLM layer is designed to be swappable for hosted models in production environments.

## 📷 Application Screenshots

### 🖥️ Main Interface

<img src="https://raw.githubusercontent.com/Rajusewda/website-based-ai-chatbot/main/screenshots/ui_home.png" width="900"/>

### 💬 Sample Question Answering

<img src="https://raw.githubusercontent.com/Rajusewda/website-based-ai-chatbot/main/screenshots/ui_answer.png" width="900"/>

### Testing
The system was tested using relevant and out-of-scope questions to validate retrieval accuracy and hallucination control.

### Limitations
- Dynamic or JavaScript-heavy pages may require advanced crawling.
- System depends on website content quality.



📄 Conclusion

This project demonstrates a production-style RAG system focused on correctness, explainability, and safe AI behavior.

⸻

👨‍💻 Author

Raju Sewda
B.Tech (CSE/IT)
Website-Based AI Chatbot Project

