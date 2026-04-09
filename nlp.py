def clean_text(text):
    text = text.lower()
    text = text.replace("\n", " ")
    text = text.replace("\r", " ")
    return text
