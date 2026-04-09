import PyPDF2

def extract_text(file):
    pdf = PyPDF2.PdfReader(file)
    text = ""

    for page in pdf.pages:
        if page.extract_text():
            text += page.extract_text()

    return text