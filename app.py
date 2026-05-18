import streamlit as st

st.title("AI Resume Analyzer")

resume_text = st.text_area("Paste Your Resume")

skills = ["Python", "Java", "C", "HTML", "CSS"]

if st.button("Analyze Resume"):

    st.subheader("Detected Skills")

    score = 0

    for skill in skills:
        if skill.lower() in resume_text.lower():
            st.write(skill)
            score += 20

    st.subheader("Resume Score")
    st.write(score, "/ 100")