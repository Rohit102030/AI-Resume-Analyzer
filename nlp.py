import spacy

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    doc = nlp(text)
    tokens = []

    for token in doc:
        if not token.is_stop and token.is_alpha:
            tokens.append(token.lemma_)

    return " ".join(tokens)