import streamlit as st
from parser import extract_text
from nlp import clean_text
from model import predict_job
from recommender import recommend_job

# Page config
st.set_page_config(page_title="AI Resume Analyzer", page_icon="🚀", layout="wide")

# CSS
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}
.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #00ffcc;
}
.subtitle {
    text-align: center;
    color: #cfcfcf;
}
.card {
    background: #1e1e2f;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.5);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="title">🚀 AI Resume Analyzer</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Smart AI-powered resume analysis✨</p>', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("⚙️ Settings")
st.sidebar.info("Upload your resume to begin analysis")

# Upload
uploaded_file = st.file_uploader("📤 Upload Resume (PDF)", type=["pdf"])

if uploaded_file:

    with st.spinner("🔍 Analyzing Resume..."):
        text = extract_text(uploaded_file)
        cleaned_text = clean_text(text)

    col1, col2 = st.columns([1.2, 1])

    # LEFT SIDE
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📄 Resume Preview")
        st.write(text[:1000])
        st.markdown('</div>', unsafe_allow_html=True)

    # RIGHT SIDE
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)

        predicted_job = predict_job(cleaned_text)
        rule_job = recommend_job(text)

        # 🔥 ATS SCORING
        score = 0
        text_lower = text.lower()

        skills = ["python", "java", "sql", "machine learning", "data science",
                  "html", "css", "javascript", "react", "node"]

        skill_score = sum(1 for skill in skills if skill in text_lower) * 4
        score += min(skill_score, 40)

        if "project" in text_lower:
            score += 15

        if "experience" in text_lower or "internship" in text_lower:
            score += 15

        if "btech" in text_lower or "degree" in text_lower:
            score += 10

        length = len(text.split())
        if length > 300:
            score += 20
        elif length > 200:
            score += 15
        elif length > 100:
            score += 10
        else:
            score += 5

        score = min(score, 100)

        # OUTPUT
        st.markdown("### 🤖 AI Predicted Role")
        st.success(predicted_job)

        st.markdown("### 💼 Suggested Role")
        st.info(rule_job)

        st.markdown("### 📊 Resume Score")

        progress_bar = st.progress(0)
        for i in range(score):
            progress_bar.progress(i + 1)

        st.write(f"{score}/100")

        # Breakdown
        st.subheader("📊 Score Breakdown")
        st.write(f"Skills Score: {skill_score}/40")
        st.write("Projects: ✔️" if "project" in text_lower else "Projects: ❌")
        st.write("Experience: ✔️" if "experience" in text_lower else "Experience: ❌")

        st.markdown('</div>', unsafe_allow_html=True)

    # SKILLS
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧠 Detected Skills")

    skills_list = ["python", "java", "sql", "machine learning", "html", "css", "javascript"]
    found_skills = [s.upper() for s in skills_list if s in text.lower()]

    if found_skills:
        st.write(" ".join([f"`{skill}`" for skill in found_skills]))
    else:
        st.warning("No major skills detected")

    st.markdown('</div>', unsafe_allow_html=True)

    # SUGGESTIONS
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📌 Suggestions")

    if score < 50:
        st.error("Improve your resume by adding more projects & skills")
    elif score < 80:
        st.warning("Good resume, but can be improved")
    else:
        st.success("Excellent resume!")

    if "python" not in text.lower():
        st.warning("👉 Add Python skill")
    if "sql" not in text.lower():
        st.warning("👉 Add SQL skill")

    st.markdown('</div>', unsafe_allow_html=True)

    # DOWNLOAD
    st.download_button(
        "📥 Download Resume Analysis",
        data=text,
        file_name="analysis.txt"
    )

# Footer
st.markdown("---")
st.caption("💡 Developed by Rohit Kumar 🚀")
