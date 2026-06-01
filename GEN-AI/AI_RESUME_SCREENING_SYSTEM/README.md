# 🤖 AI Resume Screening System with LangSmith Tracing

## 📌 Project Overview

The AI Resume Screening System is an intelligent recruitment assistant built using **LangChain**, **OpenAI**, and **LangSmith**. It automates the process of analyzing resumes, extracting skills, matching candidates against job requirements, calculating suitability scores, and generating transparent explanations for hiring decisions.

This project was developed as part of the **Innomatics Research Labs – Data Science Internship (February 2026) Task 3**.

---

## 🚀 Features

### ✅ Skill Extraction

Extracts candidate skills, tools, education, experience, and domain expertise directly from resumes.

### ✅ Resume Matching

Compares extracted candidate information against a job description.

### ✅ Candidate Scoring

Generates a suitability score between **0–100** based on:

| Criteria         | Weight |
| ---------------- | ------ |
| Skills Match     | 40%    |
| Experience Match | 30%    |
| Tools Match      | 20%    |
| Education Match  | 10%    |

### ✅ Explainable AI

Provides a clear explanation of why the candidate received a particular score.

### ✅ LangSmith Tracing

Tracks every LangChain invocation for debugging, monitoring, and observability.

### ✅ Few-Shot Prompting

Uses example-driven prompting to improve consistency and output quality.

---

## 🛠️ Technology Stack

* Python
* LangChain
* OpenAI API
* LangSmith
* LCEL (LangChain Expression Language)
* Prompt Engineering
* JSON Parsing

---

## 📂 Project Structure

```text
AI_RESUME_SCREENING_SYSTEM/
│
├── chains/
│   ├── extraction_chain.py
│   ├── matching_chain.py
│   ├── scoring_chain.py
│   ├── explain_chain.py
│   └── llm.py
│
├── prompts/
│   ├── extract_prompt.py
│   ├── match_prompt.py
│   ├── score_prompt.py
│   └── explain_prompt.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd AI_RESUME_SCREENING_SYSTEM
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Set the following environment variables:

```python
import os

os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
os.environ["LANGCHAIN_API_KEY"] = "YOUR_LANGSMITH_API_KEY"

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "resume-screening-system"
```

---

## ▶️ Running the Project

```bash
python main.py
```

---

## 🔄 Workflow

```text
Resume
   ↓
Skill Extraction
   ↓
Candidate Matching
   ↓
Scoring (0–100)
   ↓
Explanation Generation
   ↓
LangSmith Tracing
```

---

## 📊 Sample Output

```json
{
  "candidate": "Priya Sharma",
  "score": 92,
  "matched_skills": [
    "Python",
    "SQL",
    "TensorFlow",
    "Statistics"
  ],
  "experience_match": true
}
```

### Explanation

```text
The candidate demonstrates strong alignment with the job requirements.
They possess the required technical skills including Python, SQL,
TensorFlow, and cloud technologies. Their experience exceeds the
minimum requirement and includes production deployment and NLP
projects.

Strong Fit
```

---

## 📈 LangSmith Observability

This project uses LangSmith tracing to monitor:

* Prompt execution
* LLM calls
* Chain performance
* Debugging workflows
* Token usage

Every `.invoke()` call is automatically recorded in LangSmith.

---

## 🎯 Internship Requirements Covered

| Requirement             | Status |
| ----------------------- | ------ |
| Resume Screening System | ✅      |
| Skill Extraction        | ✅      |
| Candidate Matching      | ✅      |
| Scoring Logic           | ✅      |
| Explanation Generation  | ✅      |
| PromptTemplate Usage    | ✅      |
| LCEL Chains             | ✅      |
| `.invoke()` Method      | ✅      |
| LangSmith Tracing       | ✅      |
| Few-Shot Prompting      | ✅      |
| Structured JSON Output  | ✅      |

---

## 👨‍💻 Author

**Ruturaj Gajanan Tawde**

* B.E. Artificial Intelligence & Data Science
* Babasaheb Naik College of Engineering, Pusad
* Sant Gadge Baba Amravati University

### Connect

* GitHub: https://github.com/ruturaj027
* LinkedIn: https://linkedin.com/in/ruturaj-tawde-a9b054292

---

## 📜 License

This project is developed for educational and internship assessment purposes.
