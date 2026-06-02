# 🤖 RAG-Based Customer Support Assistant using LangGraph & Human-in-the-Loop

## 📌 Project Overview

The RAG-Based Customer Support Assistant is an intelligent AI application designed to answer customer queries using information retrieved from a knowledge base. The system leverages Retrieval-Augmented Generation (RAG) to provide accurate, context-aware responses while incorporating Human-in-the-Loop (HITL) support for handling complex, sensitive, or low-confidence queries.

By combining semantic search, vector databases, large language models, and workflow orchestration, the solution delivers reliable and scalable customer support automation.

---

## 🚀 Key Features

* 📄 Knowledge retrieval from PDF documents
* 🔍 Semantic search using vector embeddings
* 🤖 AI-powered context-aware response generation
* 🔄 Workflow orchestration with LangGraph
* 👨‍💻 Human-in-the-Loop (HITL) escalation mechanism
* ⚡ Fast LLM inference using Groq API
* 📊 Confidence-based response validation
* 🗄️ ChromaDB vector database integration

---

## 🧠 Working Principle

The system follows the Retrieval-Augmented Generation (RAG) workflow:

1. Load and process PDF documents.
2. Split documents into smaller text chunks.
3. Generate vector embeddings for each chunk.
4. Store embeddings in ChromaDB.
5. Convert the user's query into embeddings.
6. Retrieve the most relevant document chunks.
7. Generate an answer using the Groq LLM.
8. Evaluate response confidence.
9. Return the answer or escalate to a human agent if required.

---

## 🏗️ System Architecture

```text
User Query
     │
     ▼
LangGraph Workflow
     │
     ▼
Query Processing
     │
     ▼
ChromaDB Retriever
     │
     ▼
Relevant Context Retrieval
     │
     ▼
Groq LLM
     │
     ▼
Confidence Evaluation
     │
 ┌───┴───┐
 │       │
 ▼       ▼
Answer   HITL Escalation
```

---

## 🛠️ Technology Stack

| Technology             | Purpose                        |
| ---------------------- | ------------------------------ |
| Python                 | Core Development               |
| LangChain              | RAG Pipeline                   |
| LangGraph              | Workflow Management            |
| ChromaDB               | Vector Database                |
| HuggingFace Embeddings | Text Embedding Generation      |
| Groq API               | Large Language Model Inference |

---

## ⚙️ Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/RAG-Based-Customer-Support-Assistant.git
cd RAG-Based-Customer-Support-Assistant
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file and add:

```env
GROQ_API_KEY=your_api_key_here
```

### Run the Application

```bash
python main.py
```

---

## 🧪 Example Queries

* What is the refund policy?
* How can I cancel my order?
* How do I track my shipment?
* I would like to file a complaint.
* What support services are available?

---

## 🔁 Human-in-the-Loop (HITL)

The system automatically escalates queries to a human support representative when:

* Response confidence falls below a predefined threshold.
* The query involves sensitive or critical information.
* Relevant information cannot be found in the knowledge base.

This ensures higher reliability and improved customer experience.

---

## ⚠️ Challenges Faced

* Selecting an optimal document chunk size.
* Improving retrieval relevance and ranking.
* Managing workflow states effectively.
* Handling ambiguous user queries.

---

## 🚀 Future Enhancements

* Multi-document knowledge base support
* Conversational memory integration
* Streamlit-based web interface
* User feedback learning system
* Advanced evaluation and monitoring
* Cloud deployment support

---

## 📚 Learning Outcomes

Through this project, the following concepts were explored:

* Retrieval-Augmented Generation (RAG)
* Vector Databases and Embeddings
* LangChain Framework
* LangGraph Workflow Design
* Human-in-the-Loop Systems
* Large Language Model Integration

---

## 👨‍💻 Author

**Ruturaj Gajanan Tawde**

B.E. – Artificial Intelligence & Data Science
Babasaheb Naik College of Engineering, Pusad

GitHub: github.com/ruturaj027
LinkedIn: linkedin.com/in/ruturaj-tawde-a9b054292

---

## 📌 Conclusion

This project demonstrates the integration of Retrieval-Augmented Generation (RAG), vector databases, workflow orchestration, and Human-in-the-Loop mechanisms to build an intelligent customer support solution. The system improves response accuracy, enhances reliability, and provides a practical foundation for real-world AI-powered support applications.
