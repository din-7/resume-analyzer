import re
import unicodedata



def clean_resume_text(text: str) -> str:
    if not text or not text.strip():
        raise ValueError("Input text is empty.")
    
    text = unicodedata.normalize("NFKC", text)
    
    text = re.sub(r"[^\w\s,+./#-]", "", text)
    
    text = re.sub(r"\s+", " ", text)
    
    text= text.strip()

    return text




