# Functions to filter text before parsing
import unicodedata
import re


def filter_text(text):
    # Strip accents
    text = ''.join(char for char in unicodedata.normalize('NFD', text)
                   if unicodedata.category(char) != 'Mn')
    # To lowercase
    text = text.lower()
    # Remove all invalid punctuation
    text = re.sub(r"[^ a-z'.,?!\-]", "", text)
    # Return
    return text