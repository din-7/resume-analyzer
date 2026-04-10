# 📄 AI Resume Analyzer

An AI-powered web application that evaluates how well a resume matches a job description using modern NLP techniques and transformer-based embeddings.

---

## 🚀 Live Demo

https://resume-analyzer-bwgxpuyuzru4x9bg3pjqku.streamlit.app/

---

## Overview

This project analyzes a resume against a job description and returns a semantic similarity score representing how well the candidate aligns with the role.

Unlike traditional keyword-based systems, this app uses transformer-based embeddings to understand contextual meaning and relationships between skills and experience.

---

## Features

* 📄 Upload resume as PDF
* 📝 Paste job description
* 🤖 Semantic similarity scoring using transformer embeddings
* 📊 Match score with interpretation (Strong / Moderate / Weak)
* ⚡ Fast, interactive UI built with Streamlit

---

## Tech Stack

* Python
* Sentence Transformers (`all-mpnet-base-v2`)
* scikit-learn
* pdfplumber
* Streamlit

---

## ⚙️ How It Works

```text
PDF Resume → Text Extraction → Cleaning → Embedding
Job Description → Cleaning → Embedding
→ Cosine Similarity → Match Score
```

### Key Components

* **Text Extraction**
  Extracts text from PDF resumes using `pdfplumber`

* **Preprocessing**
  Cleans and normalizes text (handles Unicode, bullets, whitespace)

* **Embeddings**
  Uses transformer model (`all-mpnet-base-v2`) to generate semantic representations

* **Similarity Scoring**
  Computes cosine similarity between resume and job description embeddings

---

## 🧪 Example

| Scenario                           | Expected Score |
| ---------------------------------- | -------------- |
| Excellent Match                    | 80–90%         |
| Good match                         | 50–70%         |
| Unrelated roles                    | <40%           |

---

## ▶️ Running Locally

### 1. Clone the repo

```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

---


## 🧠 Design Decisions

* Used transformer embeddings instead of TF-IDF for better semantic understanding
* Avoided aggressive text preprocessing to preserve contextual meaning
* Choose a simple, stateless architecture (no database required)
* Prioritized usability with an interactive web interface

---

## ⚠️ Limitations

* Does not handle image-based (scanned) PDFs (no OCR)
* Score is semantic, not a definitive hiring decision
* No section-specific weighting (e.g., skills vs experience)

---

## 🚀 Future Improvements

* Skill gap detection (“missing skills” suggestions)
* Section-aware analysis (Experience, Skills, Education)
* Highlighting relevant parts of the resume
* Support for multiple file formats

---

## License

MIT License
