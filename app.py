import streamlit as st
from services.embeddings import score_resume

st.title("Resume Analyzer")

resume_file = st.file_uploader("Upload Resume", type=["pdf"])
job_description = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if not resume_file or not job_description:
        st.warning("Please upload a resume and enter a job description.")
    else:
        with st.spinner("Analyzing..."):
            try:
                score = score_resume(resume_file, job_description)
                st.metric("Similarity Score", f"{score:.2%}")
            except Exception as e:
                st.error(f"Error: {str(e)}")