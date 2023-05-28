import re


def find_all_words(text, word):
    pattern = re.compile(word, flags=re.IGNORECASE)
    matches = pattern.findall(text)
    return matches

print(find_all_words(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as python 0.9.0.",
    "Python"))