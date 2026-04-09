import streamlit as st
from parser import extract_text
from nlp import clean_text
from model import predict_job
from recommender import recommend_job

# Page config
st.set_page_config(page_title="AI Resume Analyzer", page_icon="🚀", layout="wide")

# 🔥 Advanced Animated CSS
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

/*Title Animation */
.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #00ffcc;
    animation: fadeInDown 1s ease-in-out;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #cfcfcf;
    animation: fadeIn 2s ease-in-out;
}

/* Card Styling */
.card {
    background: #1e1e2f;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.5);
    margin-bottom: 20px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    animation: fadeInUp 1s ease-in-out;
}

/* Hover Effect */
.card:hover {
    transform: translateY(-10px) scale(1.02);
    box-shadow: 0px 8px 25px rgba(0,255,200,0.3);
}

/* Fade Animations */
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

/* Progress Bar Glow */
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
        st.write(text[:1000])
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

        # 🔥 Animated progress
        progress_bar = st.progress(0)
        for i in range(score):
            progress_bar.progress(i + 1)

        st.write(f"{score}/100")

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

# /*import google.generativeai as genai

# # 🔑 API KEY
# genai.configure(api_key="AIzaSyAKlz40lBQMDv2F_9t2t_S75SFwjbzX2zE")

# model = genai.GenerativeModel("gemini-1.5-flash-latest")

# # 🤖 CHATBOT UI
# st.markdown('<div class="card">', unsafe_allow_html=True)
# st.subheader("🤖 AI Career Chatbot")

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # Display chat
# for msg in st.session_state.chat_history:
#     if msg["role"] == "user":
#         st.markdown(f"🧑 {msg['content']}")
#     else:
#         st.markdown(f"🤖 {msg['content']}")

# user_input = st.text_input("Ask about your resume or career:")

# if st.button("Send Chat"):
#     if user_input:
#         st.session_state.chat_history.append({"role": "user", "content": user_input})

#         with st.spinner("🤖 Thinking..."):
#             response = model.generate_content(
#                 f"""
# You are a professional career assistant.

# User Resume:
# {text}

# User Question:
# {user_input}

# Give clear, short, helpful advice.
# """
#             )

#         reply = response.text

#         st.session_state.chat_history.append({"role": "bot", "content": reply})
#         st.rerun()

# st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("💡 Developed by Rohit Kumar ")