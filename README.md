# 📝 Resume Analyzer

An **AI-powered Resume Analyzer** that parses resumes and scores them against job descriptions.

## ✨ Features
- 📊 **ATS Score** — Applicant Tracking System compatibility
- 🎯 **Job Match %** — semantic similarity to job description
- 💡 **Missing Skills** — actionable improvement suggestions
- 📈 **Experience Timeline** — parsed work history
- 🔤 **Keyword Optimization** — important keyword highlighting

## 🛠️ Tech Stack
- **spaCy / NLTK** – NLP text parsing
- **Sentence-Transformers** – semantic job matching
- **PyPDF2 / python-docx** – document parsing
- **Streamlit** – web interface
- **Pandas** – structured data output

## 🚀 Getting Started
```bash
git clone https://github.com/Varshini487/resume-analyzer
cd resume-analyzer
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py
```

## 💡 Use Cases
- Job seekers optimizing their resumes
- HR teams screening candidates
- Career coaching platforms
- University placement cells
