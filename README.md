# 🩺 End-to-End Medical AI Assistant

An end-to-end Medical AI Assistant that integrates Clinical NLP, Machine Learning, Retrieval-Augmented Generation (RAG), and Llama 3.2 to analyze patient symptoms, predict disease risk, and generate AI-powered medical explanations.

---

# Features

- Clinical NLP pipeline
- Biomedical Named Entity Recognition (NER)
- Symptom normalization
- Negation detection
- Severity extraction
- Duration extraction
- Ontology mapping (SNOMED)
- Disease risk prediction
- Confidence score estimation
- Risk categorization
- Specialist recommendation
- Retrieval-Augmented Generation (RAG)
- FAISS vector database
- Llama 3.2 medical explanation generation
- Interactive FastAPI web application

---

# Technologies Used

### Backend
- Python
- FastAPI
- Jinja2

### Frontend
- HTML
- CSS
- JavaScript

### AI & NLP
- Hugging Face Transformers
- Biomedical NER
- Sentence Transformers
- Llama 3.2

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### Retrieval
- FAISS

---

# System Architecture

```text
                    User
                      │
                      ▼
            FastAPI Web Application
                      │
        ┌─────────────┼──────────────┐
        │             │              │
        ▼             ▼              ▼
  Clinical NLP   Machine Learning    RAG
        │             │              │
        └─────────────┼──────────────┘
                      ▼
             Structured Medical Data
                      │
                      ▼
                Llama 3.2 Response
                      │
                      ▼
            Medical Decision Support
```

---

# Clinical NLP Pipeline

```text
Patient Symptoms
        │
        ▼
Text Cleaning
        │
        ▼
Biomedical NER
        │
        ▼
Phrase Merging
        │
        ▼
Symptom Normalization
        │
        ▼
Negation Detection
        │
        ▼
Severity Detection
        │
        ▼
Duration Extraction
        │
        ▼
Ontology Mapping
        │
        ▼
Structured Clinical Output
```

---

# Machine Learning Pipeline

```text
Symptoms
    │
    ▼
Feature Engineering
    │
    ▼
Random Forest Classifier
    │
    ▼
Disease Prediction
    │
    ▼
Confidence Score
    │
    ▼
Risk Assessment
    │
    ▼
Specialist Recommendation
```

---

# RAG Pipeline

```text
Patient Query
      │
      ▼
Embedding Model
      │
      ▼
FAISS Vector Search
      │
      ▼
Relevant Medical Knowledge
      │
      ▼
Llama 3.2
      │
      ▼
Medical Explanation
```

---

# Project Structure

```text
medical-ai-assistant/
│
├── frontend/
│   ├── static/
│   └── templates/
│
├── knowledge_base/
│
├── services/
│   ├── ml/
│   ├── nlp/
│   └── rag/
│
├── app.py
├── requirements.tx
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/LabXsra/medical-ai-assistant.git
```

Navigate into the project

```bash
cd medical-ai-assistant
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python -m uvicorn app:app --reload
```

Open

```
http://127.0.0.1:8000
```

---

# Screenshots

### Home Page

<img width="1552" height="815" alt="project_img" src="https://github.com/user-attachments/assets/99678b1a-e7e0-4e97-94af-7166bf6d506b" />
<img width="1567" height="882" alt="project_img2" src="https://github.com/user-attachments/assets/a100d582-857d-4fe4-8c63-6883ccecedfa" />
<img width="1470" height="865" alt="project_img3" src="https://github.com/user-attachments/assets/bbd8e8db-1161-472a-b562-ecc47d76792e" />
<img width="1240" height="837" alt="project_img4" src="https://github.com/user-attachments/assets/555e5fe2-2037-4608-b02a-0a6de10014f2" />
<img width="1402" height="352" alt="project_img5" src="https://github.com/user-attachments/assets/c53f1915-8b53-4e6c-a977-8b9328786627" />


# Future Improvements

- PDF medical report generation
- Electronic Health Record (EHR) integration
- Voice symptom input
- Drug interaction checking
- Medical image analysis
- Multi-language support

---
# Author

**Asra**

Computer Science Engineering 


---

> **Disclaimer:** This project is developed for educational and research purposes only. It is not intended to replace professional medical diagnosis or treatment.
