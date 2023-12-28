import pandas as pd
import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load your diary entry data
data = pd.read_csv("diary_entries.csv")

# Tokenize and preprocess the text
def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.text.lower() for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

data['processed_text'] = data['text'].apply(preprocess_text)
