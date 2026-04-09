def recommend_job(text):
    text = text.lower()

    if "machine learning" in text or "deep learning" in text:
        return "Machine Learning Engineer"
    elif "data science" in text:
        return "Data Scientist"
    elif "html" in text or "css" in text:
        return "Web Developer"
    elif "java" in text:
        return "Java Developer"
    else:
        return "Software Developer"