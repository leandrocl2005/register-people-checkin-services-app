from unicodedata import normalize
from re import sub

def format_text(txt):
    txt = normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')
    txt = sub('[^A-Za-z0-9 -]+', '', txt).strip()
    return txt.upper()