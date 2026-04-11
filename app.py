import streamlit as st
from parser import extract_text
from nlp import clean_text
from model import predict_job
from recommender import recommend_job
import os
from groq import Groq

def remove_projects_section(text):
    lines = text.split("\n")
    new_lines = []
    skip = False

    for line in lines:
        line_lower = line.strip().lower()

        if "projects" in line_lower:
            skip = True
            continue

        if skip and (
            "skills" in line_lower
            or "education" in line_lower
            or "experience" in line_lower
            or "certification" in line_lower
        ):
            skip = False

        if not skip:
            new_lines.append(line.strip())  # ✅ remove spaces

    return "\n".join(new_lines)


def extract_projects(text):
    lines = text.split("\n")
    projects = []
    capture = False

    for line in lines:
        line_clean = line.strip()
        line_lower = line_clean.lower()

        if "projects" in line_lower:
            capture = True
            continue

        if capture and ("skills" in line_lower or "education" in line_lower or "experience" in line_lower):
            break

        if capture:
            if ":" in line_clean:
                projects.append(line_clean)

    return projects


# Page config
st.set_page_config(page_title="AI Resume Analyzer", page_icon="🚀", layout="wide")

# 🔥 YOUR SAME CSS (UNCHANGED)
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
    animation: fadeInDown 1s ease-in-out;
}
.subtitle {
    text-align: center;
    color: #cfcfcf;
    animation: fadeIn 2s ease-in-out;
}
.card {
    background: #1e1e2f;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.5);
    margin-bottom: 20px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    animation: fadeInUp 1s ease-in-out;
}
.card:hover {
    transform: translateY(-10px) scale(1.02);
    box-shadow: 0px 8px 25px rgba(0,255,200,0.3);
}
@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}
@keyframes fadeInUp {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}
@keyframes fadeInDown {
    from {opacity: 0; transform: translateY(-20px);}
    to {opacity: 1; transform: translateY(0);}
}
.stProgress > div > div > div > div {
    background-color: #00ffcc;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="title">🚀 AI Resume Analyzer</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Smart AI-powered resume analysis✨</p>', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("⚙️ Settings")
st.sidebar.info("Upload your resume to begin analysis")
st.sidebar.markdown("Built using AI + NLP")

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

        # ✅ FIXED (no overwrite + no grey box)
        clean_resume = remove_projects_section(text)
        clean_resume = "\n".join([line.strip() for line in clean_resume.split("\n")])

        def make_headings_bold(text):
            headings = ["skills", "education", "experience", "certification"]

            formatted_lines = []
            for line in text.split("\n"):
                line_clean = line.strip()

                if line_clean.lower() in headings:
                    formatted_lines.append(f"**{line_clean.upper()}**")
                else:
                    formatted_lines.append(line_clean)

            return "\n\n".join(formatted_lines)

        formatted_resume = make_headings_bold(clean_resume)

        st.markdown(formatted_resume)

        st.markdown('</div>', unsafe_allow_html=True)

    # RIGHT SIDE
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)

        predicted_job = predict_job(cleaned_text)
        rule_job = recommend_job(text)
        score = min(len(cleaned_text.split()) // 5, 100)

        st.markdown("### 🤖 AI Predicted Role")
        st.success(predicted_job)

        st.markdown("### 💼 Suggested Role")
        st.info(rule_job)

        st.markdown("### 📊 Resume Score")

        progress_bar = st.progress(0)
        for i in range(score):
            progress_bar.progress(i + 1)

        st.write(f"{score}/100")

        st.markdown('</div>', unsafe_allow_html=True)

        # PROJECTS
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📁 Projects Found")

        projects = extract_projects(text)

        if projects:
            for i, proj in enumerate(projects, 1):
                st.write(f"{i}. {proj}")
        else:
            st.warning("No projects detected")

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



   # 🤖 GROQ CHATBOT
from groq import Groq

# 🔑 API KEY
client = Groq(api_key = st.secrets["GROQ_API_KEY"])

# CHATBOT UI
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🤖 AI Career Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(f"🧑 {msg['content']}")
    else:
        st.markdown(f"🤖 {msg['content']}")

user_input = st.text_input("Ask about your resume:")

if st.button("Send Chat"):
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        with st.spinner("🤖 Thinking..."):

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
            messages=[
            {   
            "role": "system",
            "content": "You are a professional career assistant. Give short, clear advice."
            },
        {
            "role": "user",
            "content": f"User Resume:\n{text}\n\nUser Question:\n{user_input}"
        },
    ],
)

        reply = response.choices[0].message.content

        st.session_state.chat_history.append({"role": "bot", "content": reply})
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)


# Footer
st.markdown("---")
st.caption("💡 Developed by Rohit Kumar")
