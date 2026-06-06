import streamlit as st
import PyPDF2
import re
from sentence_transformers import SentenceTransformer, util
import io

st.set_page_config(page_title="📝 Resume Analyzer", layout="wide")
st.title("📝 AI Resume Analyzer")
st.markdown("Upload your resume and a job description to get your match score and improvement tips")

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    return " ".join(page.extract_text() or "" for page in reader.pages)

def extract_skills(text):
    tech_skills = ["python", "java", "sql", "machine learning", "deep learning", "nlp",
                   "tensorflow", "pytorch", "aws", "docker", "kubernetes", "react", "node",
                   "data analysis", "statistics", "excel", "tableau", "power bi", "git"]
    found = [s for s in tech_skills if s.lower() in text.lower()]
    return found

col1, col2 = st.columns(2)
with col1:
    st.subheader("📄 Upload Resume")
    resume_file = st.file_uploader("Resume (PDF)", type=["pdf"])
with col2:
    st.subheader("💼 Job Description")
    job_desc = st.text_area("Paste job description here:", height=200)

if resume_file and job_desc:
    resume_text = extract_text_from_pdf(resume_file)
    
    emb_resume = model.encode(resume_text, convert_to_tensor=True)
    emb_job = model.encode(job_desc, convert_to_tensor=True)
    score = float(util.cos_sim(emb_resume, emb_job)[0][0]) * 100

    st.markdown("---")
    st.subheader("📊 Analysis Results")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("🎯 Match Score", f"{score:.1f}%")
    
    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_desc))
    matching = resume_skills & job_skills
    missing = job_skills - resume_skills
    
    col2.metric("✅ Matching Skills", len(matching))
    col3.metric("❌ Missing Skills", len(missing))

    if matching:
        st.success(f"**Found Skills:** {', '.join(matching)}")
    if missing:
        st.warning(f"**Missing Skills to Add:** {', '.join(missing)}")
    
    if score >= 75:
        st.balloons()
        st.success("🎉 Excellent match! Your resume is well-aligned with this job.")
    elif score >= 50:
        st.info("👍 Good match! Adding the missing skills will improve your chances.")
    else:
        st.error("⚠️ Low match. Consider tailoring your resume more to this job description.")
